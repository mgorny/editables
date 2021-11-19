from importlib.machinery import ModuleSpec
import importlib.abc
import types
from pathlib import Path
from typing import Sequence

class RedirectingFinder(importlib.abc.MetaPathFinder):
    _redirections: dict[str, str]

    @classmethod
    def map_module(cls, name: str, path: str) -> None:
        ...

    # Match the ABC definition from typeshed
    @classmethod
    def find_spec(cls, fullname: str, path: Sequence[bytes|str] | None = ..., target: types.ModuleType | None = ...) -> ModuleSpec | None:
        ...

    @classmethod
    def install(cls) -> None:
        ...
