# Stubs for torch.optim.rprop (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .optimizer import Optimizer
from typing import Any, Optional

class Rprop(Optimizer):
    def __init__(self, params: Any, lr: float = ..., etas: Any = ..., step_sizes: Any = ...) -> None: ...
    def step(self, closure: Optional[Any] = ...): ...
