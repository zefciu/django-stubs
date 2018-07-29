# Stubs for django.contrib.staticfiles.finders (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

from django.contrib.staticfiles.storage import StaticFilesStorage
from django.core.checks.messages import Error
from django.core.files.storage import DefaultStorage, FileSystemStorage
from typing import Iterator, List, Optional, Tuple, Union
searched_locations: Any

class BaseFinder:
    def check(self, **kwargs: Any) -> None: ...
    def find(self, path: Any, all: bool = ...) -> None: ...
    def list(self, ignore_patterns: Any) -> None: ...

class FileSystemFinder(BaseFinder):
    locations: Any = ...
    storages: Any = ...
    def __init__(self, app_names: None = ..., *args: Any, **kwargs: Any) -> None: ...
    def check(self, **kwargs: Any) -> List[Error]: ...
    def find(self, path: str, all: bool = ...) -> Union[str, List[str]]: ...
    def find_location(self, root: str, path: str, prefix: str = ...) -> Optional[str]: ...
    def list(self, ignore_patterns: List[str]) -> Iterator[Tuple[str, FileSystemStorage]]: ...

class AppDirectoriesFinder(BaseFinder):
    storage_class: Any = ...
    source_dir: str = ...
    apps: Any = ...
    storages: Any = ...
    def __init__(self, app_names: None = ..., *args: Any, **kwargs: Any) -> None: ...
    def list(self, ignore_patterns: List[str]) -> Iterator[Tuple[str, FileSystemStorage]]: ...
    def find(self, path: str, all: bool = ...) -> str: ...
    def find_in_app(self, app: str, path: str) -> Optional[str]: ...

class BaseStorageFinder(BaseFinder):
    storage: Any = ...
    def __init__(self, storage: Optional[StaticFilesStorage] = ..., *args: Any, **kwargs: Any) -> None: ...
    def find(self, path: Any, all: bool = ...): ...
    def list(self, ignore_patterns: List[str]) -> Iterator[Tuple[str, DefaultStorage]]: ...

class DefaultStorageFinder(BaseStorageFinder):
    storage: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

def find(path: str, all: bool = ...) -> Optional[str]: ...
def get_finders() -> Iterator[BaseFinder]: ...
def get_finder(import_path: str) -> BaseFinder: ...