#!/usr/bin/env python
import plac
import re
import random
from pathlib import Path
import thinc.extra.datasets
import spacy
from spacy.util import minibatch, compounding


@plac.annotations(
    model=("Model name", "positional", None, str),
    output_dir=("Optional output directory", "option", "o", Path),
    n_texts=("Number of texts to train from", "option", "t", int),
    n_iter=("Number of training iterations", "option", "n", int),
)
def main(model, output_dir=None, n_iter=20, n_texts=100):
    random.seed(0)
    if output_dir is not None:
        output_dir = Path(output_dir)
        if not output_dir.exists():
            output_dir.mkdir()

    nlp = spacy.load(model)
    print(f"Loaded model '{model}'")
    textcat = nlp.create_pipe(
        "pytt_textcat",
        config={
            "exclusive_classes": True,
            "token_vector_width": nlp.get_pipe("pytt_tok2vec").model.nO,
        },
    )
    # add label to text classifier
    textcat.add_label("POSITIVE")
    textcat.add_label("NEGATIVE")
    textcat.begin_training()
    nlp.add_pipe(textcat, last=True)

    # load the IMDB dataset
    print("Loading IMDB data...")
    (train_texts, train_cats), (dev_texts, dev_cats) = load_data(limit=n_texts)
    train_texts = train_texts[:n_texts]
    train_cats = train_cats[:n_texts]
    print(
        f"Using {n_texts} examples ({len(train_texts)} training, {len(dev_texts)} evaluation)"
    )
    train_data = list(zip(train_texts, [{"cats": cats} for cats in train_cats]))

    optimizer = nlp.resume_training()
    print("Training the model...")
    print("{:^5}\t{:^5}\t{:^5}\t{:^5}".format("LOSS", "P", "R", "F"))
    batch_sizes = compounding(4.0, 32.0, 1.001)
    for i in range(n_iter):
        losses = {}
        # batch up the examples using spaCy's minibatch
        random.shuffle(train_data)
        batches = minibatch(train_data, size=batch_sizes)
        for batch in batches:
            texts, annotations = zip(*batch)
            texts = (text[:50] for text in texts)
            nlp.update(texts, annotations, sgd=optimizer, drop=0.2, losses=losses)
        # evaluate on the dev data split off in load_data()
        scores = evaluate(nlp, dev_texts, dev_cats)
        print(
            "{0:.3f}\t{1:.3f}\t{2:.3f}\t{3:.3f}".format(
                losses["textcat"],
                scores["textcat_p"],
                scores["textcat_r"],
                scores["textcat_f"],
            )
        )

    # Test the trained model
    test_text = "This movie sucked"
    doc = nlp(test_text)
    print(test_text, doc.cats)

    if output_dir is not None:
        nlp.to_disk(output_dir)
        print("Saved model to", output_dir)
        # test the saved model
        print("Loading from", output_dir)
        nlp2 = spacy.load(output_dir)
        doc2 = nlp2(test_text)
        print(test_text, doc2.cats)


white_re = re.compile(r"\s\s+")
def load_data(limit=0, split=0.8):
    """Load data from the IMDB dataset."""
    # Partition off part of the train data for evaluation
    train_data, _ = thinc.extra.datasets.imdb(limit=limit)
    random.shuffle(train_data)
    train_data = train_data[-limit:]
    texts, labels = zip(*train_data)
    texts = [white_re.sub(" ", text) for text in texts]
    cats = [{"POSITIVE": bool(y), "NEGATIVE": not bool(y)} for y in labels]
    split = int(len(train_data) * split)
    return (texts[:split], cats[:split]), (texts[split:], cats[split:])


def evaluate(nlp, textcat, texts, cats):
    tp = 0.0  # True positives
    fp = 1e-8  # False positives
    fn = 1e-8  # False negatives
    tn = 0.0  # True negatives
    for i, doc in nlp.pipe(texts):
        gold = cats[i]
        for label, score in doc.cats.items():
            if label not in gold:
                continue
            if label == "NEGATIVE":
                continue
            if score >= 0.5 and gold[label] >= 0.5:
                tp += 1.0
            elif score >= 0.5 and gold[label] < 0.5:
                fp += 1.0
            elif score < 0.5 and gold[label] < 0.5:
                tn += 1
            elif score < 0.5 and gold[label] >= 0.5:
                fn += 1
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    if (precision + recall) == 0:
        f_score = 0.0
    else:
        f_score = 2 * (precision * recall) / (precision + recall)
    return {"textcat_p": precision, "textcat_r": recall, "textcat_f": f_score}


if __name__ == "__main__":
    plac.call(main)
