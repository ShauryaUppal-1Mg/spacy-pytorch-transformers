# Stubs for pytorch_transformers.modeling_transfo_xl (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import torch.nn.functional as nn
from .modeling_transfo_xl_utilities import ProjectedAdaptiveLogSoftmax, sample_logits
from .modeling_utils import PreTrainedModel, PretrainedConfig, add_start_docstrings
from typing import Any, Optional

logger: Any
TRANSFO_XL_PRETRAINED_MODEL_ARCHIVE_MAP: Any
TRANSFO_XL_PRETRAINED_CONFIG_ARCHIVE_MAP: Any

def build_tf_to_pytorch_map(model: Any, config: Any): ...
def load_tf_weights_in_transfo_xl(model: Any, config: Any, tf_path: Any): ...

class TransfoXLConfig(PretrainedConfig):
    pretrained_config_archive_map: Any = ...
    n_token: Any = ...
    cutoffs: Any = ...
    tie_weight: Any = ...
    tie_projs: Any = ...
    d_model: Any = ...
    d_embed: Any = ...
    d_head: Any = ...
    d_inner: Any = ...
    div_val: Any = ...
    pre_lnorm: Any = ...
    n_layer: Any = ...
    n_head: Any = ...
    tgt_len: Any = ...
    ext_len: Any = ...
    mem_len: Any = ...
    same_length: Any = ...
    attn_type: Any = ...
    clamp_len: Any = ...
    sample_softmax: Any = ...
    adaptive: Any = ...
    dropout: Any = ...
    dropatt: Any = ...
    untie_r: Any = ...
    init: Any = ...
    init_range: Any = ...
    proj_init_std: Any = ...
    init_std: Any = ...
    def __init__(self, vocab_size_or_config_json_file: int = ..., cutoffs: Any = ..., d_model: int = ..., d_embed: int = ..., n_head: int = ..., d_head: int = ..., d_inner: int = ..., div_val: int = ..., pre_lnorm: bool = ..., n_layer: int = ..., tgt_len: int = ..., ext_len: int = ..., mem_len: int = ..., clamp_len: int = ..., same_length: bool = ..., proj_share_all_but_first: bool = ..., attn_type: int = ..., sample_softmax: int = ..., adaptive: bool = ..., tie_weight: bool = ..., dropout: float = ..., dropatt: float = ..., untie_r: bool = ..., init: str = ..., init_range: float = ..., proj_init_std: float = ..., init_std: float = ..., **kwargs: Any) -> None: ...
    @property
    def max_position_embeddings(self): ...
    @property
    def vocab_size(self): ...
    @vocab_size.setter
    def vocab_size(self, value: Any) -> None: ...
    @property
    def hidden_size(self): ...
    @property
    def num_attention_heads(self): ...
    @property
    def num_hidden_layers(self): ...

class PositionalEmbedding(nn.Module):
    demb: Any = ...
    def __init__(self, demb: Any) -> None: ...
    def forward(self, pos_seq: Any, bsz: Optional[Any] = ...): ...

class PositionwiseFF(nn.Module):
    d_model: Any = ...
    d_inner: Any = ...
    dropout: Any = ...
    CoreNet: Any = ...
    layer_norm: Any = ...
    pre_lnorm: Any = ...
    def __init__(self, d_model: Any, d_inner: Any, dropout: Any, pre_lnorm: bool = ...) -> None: ...
    def forward(self, inp: Any): ...

class MultiHeadAttn(nn.Module):
    output_attentions: Any = ...
    n_head: Any = ...
    d_model: Any = ...
    d_head: Any = ...
    dropout: Any = ...
    q_net: Any = ...
    kv_net: Any = ...
    drop: Any = ...
    dropatt: Any = ...
    o_net: Any = ...
    layer_norm: Any = ...
    scale: Any = ...
    pre_lnorm: Any = ...
    r_r_bias: Any = ...
    r_w_bias: Any = ...
    def __init__(self, n_head: Any, d_model: Any, d_head: Any, dropout: Any, dropatt: int = ..., pre_lnorm: bool = ..., r_r_bias: Optional[Any] = ..., r_w_bias: Optional[Any] = ..., output_attentions: bool = ...) -> None: ...
    def forward(self, h: Any, attn_mask: Optional[Any] = ..., mems: Optional[Any] = ..., head_mask: Optional[Any] = ...): ...

class RelMultiHeadAttn(nn.Module):
    output_attentions: Any = ...
    n_head: Any = ...
    d_model: Any = ...
    d_head: Any = ...
    dropout: Any = ...
    qkv_net: Any = ...
    drop: Any = ...
    dropatt: Any = ...
    o_net: Any = ...
    layer_norm: Any = ...
    scale: Any = ...
    pre_lnorm: Any = ...
    r_r_bias: Any = ...
    r_w_bias: Any = ...
    def __init__(self, n_head: Any, d_model: Any, d_head: Any, dropout: Any, dropatt: int = ..., tgt_len: Optional[Any] = ..., ext_len: Optional[Any] = ..., mem_len: Optional[Any] = ..., pre_lnorm: bool = ..., r_r_bias: Optional[Any] = ..., r_w_bias: Optional[Any] = ..., output_attentions: bool = ...) -> None: ...
    def forward(self, w: Any, r: Any, attn_mask: Optional[Any] = ..., mems: Optional[Any] = ...) -> None: ...

class RelPartialLearnableMultiHeadAttn(RelMultiHeadAttn):
    r_net: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def forward(self, w: Any, r: Any, attn_mask: Optional[Any] = ..., mems: Optional[Any] = ..., head_mask: Optional[Any] = ...): ...

class RelLearnableMultiHeadAttn(RelMultiHeadAttn):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def forward(self, w: Any, r_emb: Any, r_w_bias: Any, r_bias: Any, attn_mask: Optional[Any] = ..., mems: Optional[Any] = ..., head_mask: Optional[Any] = ...): ...

class DecoderLayer(nn.Module):
    dec_attn: Any = ...
    pos_ff: Any = ...
    def __init__(self, n_head: Any, d_model: Any, d_head: Any, d_inner: Any, dropout: Any, **kwargs: Any) -> None: ...
    def forward(self, dec_inp: Any, dec_attn_mask: Optional[Any] = ..., mems: Optional[Any] = ..., head_mask: Optional[Any] = ...): ...

class RelLearnableDecoderLayer(nn.Module):
    dec_attn: Any = ...
    pos_ff: Any = ...
    def __init__(self, n_head: Any, d_model: Any, d_head: Any, d_inner: Any, dropout: Any, **kwargs: Any) -> None: ...
    def forward(self, dec_inp: Any, r_emb: Any, r_w_bias: Any, r_bias: Any, dec_attn_mask: Optional[Any] = ..., mems: Optional[Any] = ..., head_mask: Optional[Any] = ...): ...

class RelPartialLearnableDecoderLayer(nn.Module):
    dec_attn: Any = ...
    pos_ff: Any = ...
    def __init__(self, n_head: Any, d_model: Any, d_head: Any, d_inner: Any, dropout: Any, **kwargs: Any) -> None: ...
    def forward(self, dec_inp: Any, r: Any, dec_attn_mask: Optional[Any] = ..., mems: Optional[Any] = ..., head_mask: Optional[Any] = ...): ...

class AdaptiveEmbedding(nn.Module):
    n_token: Any = ...
    d_embed: Any = ...
    cutoffs: Any = ...
    div_val: Any = ...
    d_proj: Any = ...
    emb_scale: Any = ...
    cutoff_ends: Any = ...
    emb_layers: Any = ...
    emb_projs: Any = ...
    def __init__(self, n_token: Any, d_embed: Any, d_proj: Any, cutoffs: Any, div_val: int = ..., sample_softmax: bool = ...) -> None: ...
    def forward(self, inp: Any): ...

class TransfoXLPreTrainedModel(PreTrainedModel):
    config_class: Any = ...
    pretrained_model_archive_map: Any = ...
    load_tf_weights: Any = ...
    base_model_prefix: str = ...
    def __init__(self, *inputs: Any, **kwargs: Any) -> None: ...
    def init_weights(self, m: Any) -> None: ...
    def set_num_special_tokens(self, num_special_tokens: Any) -> None: ...

TRANSFO_XL_START_DOCSTRING: str
TRANSFO_XL_INPUTS_DOCSTRING: str

class TransfoXLModel(TransfoXLPreTrainedModel):
    output_attentions: Any = ...
    output_hidden_states: Any = ...
    n_token: Any = ...
    d_embed: Any = ...
    d_model: Any = ...
    n_head: Any = ...
    d_head: Any = ...
    word_emb: Any = ...
    drop: Any = ...
    n_layer: Any = ...
    tgt_len: Any = ...
    mem_len: Any = ...
    ext_len: Any = ...
    max_klen: Any = ...
    attn_type: Any = ...
    r_w_bias: Any = ...
    r_r_bias: Any = ...
    layers: Any = ...
    same_length: Any = ...
    clamp_len: Any = ...
    pos_emb: Any = ...
    r_emb: Any = ...
    r_bias: Any = ...
    def __init__(self, config: Any) -> None: ...
    sample_softmax: int = ...
    def backward_compatible(self) -> None: ...
    def reset_length(self, tgt_len: Any, ext_len: Any, mem_len: Any) -> None: ...
    def init_mems(self, data: Any): ...
    def forward(self, input_ids: Any, mems: Optional[Any] = ..., head_mask: Optional[Any] = ...): ...

class TransfoXLLMHeadModel(TransfoXLPreTrainedModel):
    transformer: Any = ...
    sample_softmax: Any = ...
    out_layer: Any = ...
    sampler: Any = ...
    crit: Any = ...
    def __init__(self, config: Any) -> None: ...
    def tie_weights(self) -> None: ...
    def reset_length(self, tgt_len: Any, ext_len: Any, mem_len: Any) -> None: ...
    def init_mems(self, data: Any): ...
    def forward(self, input_ids: Any, labels: Optional[Any] = ..., mems: Optional[Any] = ..., head_mask: Optional[Any] = ...): ...