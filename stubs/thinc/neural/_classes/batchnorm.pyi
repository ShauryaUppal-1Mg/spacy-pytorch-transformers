# Stubs for thinc.neural._classes.batchnorm (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .model import Model
from typing import Any

class BatchNorm(Model):
    name: str = ...
    child: Any = ...
    nO: Any = ...
    nr_upd: int = ...
    eps: Any = ...
    alpha: Any = ...
    rmax: Any = ...
    dmax: Any = ...
    def __init__(self, child: Any, **kwargs: Any) -> None: ...
    def predict(self, X: Any): ...
    def begin_update(self, X: Any, drop: float = ...): ...
