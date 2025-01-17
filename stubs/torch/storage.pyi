# Stubs for torch.storage (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from ._utils import _cuda, _type
from typing import Any

class _StorageBase:
    is_cuda: bool = ...
    is_sparse: bool = ...
    def __iter__(self): ...
    def __copy__(self): ...
    def __deepcopy__(self, memo: Any): ...
    def __reduce__(self): ...
    def __sizeof__(self): ...
    def clone(self): ...
    def tolist(self): ...
    def cpu(self): ...
    def double(self): ...
    def float(self): ...
    def half(self): ...
    def long(self): ...
    def int(self): ...
    def short(self): ...
    def char(self): ...
    def byte(self): ...
    def bool(self): ...
    def pin_memory(self): ...
    def share_memory_(self): ...
