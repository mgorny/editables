from importlib.machinery import ModuleSpec
import types
from pathlib import Path
from typing import Sequence

class RedirectingFinder:
    _redirections: dict[str, str]

    def map_module(cls, name: str, path: str) -> None:
        ...

    # Match the ABC definition from typeshed
    def find_spec(cls, fullname: str, path: Sequence[bytes|str] | None = ..., target: types.ModuleType | None = ...) -> ModuleSpec | None:
        ...

    def install(cls) -> None:
        ...
