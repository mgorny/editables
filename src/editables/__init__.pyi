import os
from pathlib import Path
from typing import Union

__version__: str

# Note, the operator version of this using | does not work for some reason...
_StrOrPath = Union[str, os.PathLike[str]]

class EditableProject:
    project_name: str
    project_dir: Path
    redirections: dict[str, str]
    path_entries: list[Path]

    def __init__(self, project_name: str, project_dir: _StrOrPath) -> None:
        ...

    def make_absolute(self, path: _StrOrPath) -> Path:
        ...

    def map(self, name: str, target: _StrOrPath) -> None:
        ...

    def add_to_path(self, dirname: _StrOrPath) -> None:
        ...

    def dependencies(self) -> list[str]:
        ...

    def pth_file(self) -> str:
        ...

    def bootstrap_file(self) -> str:
        ...
