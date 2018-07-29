# Stubs for django.dispatch.dispatcher (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

from django.db.models.base import Model
from functools import partial
from typing import Any, Callable, List, Optional, Tuple, Type, Union
def _make_id(target: Any): ...

NONE_ID: Any
NO_RECEIVERS: Any

class Signal:
    receivers: Any = ...
    providing_args: Any = ...
    lock: Any = ...
    use_caching: Any = ...
    sender_receivers_cache: Any = ...
    _dead_receivers: bool = ...
    def __init__(self, providing_args: List[str] = ..., use_caching: bool = ...) -> None: ...
    def connect(self, receiver: Callable, sender: Any = ..., weak: bool = ..., dispatch_uid: Optional[str] = ...) -> None: ...
    def disconnect(self, receiver: Optional[Callable] = ..., sender: Any = ..., dispatch_uid: Optional[str] = ...) -> bool: ...
    def has_listeners(self, sender: object = ...) -> bool: ...
    def send(self, sender: Type[Model], **named: Any) -> Union[List[Tuple[object, None]], List[Tuple[Callable, None]]]: ...
    def send_robust(self, sender: Any, **named: Any): ...
    def _clear_dead_receivers(self) -> None: ...
    def _live_receivers(self, sender: object) -> Union[List[partial], List[Callable], List[object]]: ...
    def _remove_receiver(self, receiver: None = ...) -> None: ...

def receiver(signal: Any, **kwargs: Any): ...