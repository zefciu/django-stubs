# Stubs for django.db.migrations.operations.fields (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .base import Operation
from .utils import is_referenced_by_foreign_key
from typing import Any, Optional

from django.db.backends.sqlite3.schema import DatabaseSchemaEditor
from django.db.migrations.operations.models import AlterUniqueTogether, CreateModel, DeleteModel, FieldRelatedOptionOperation, ModelOperation
from django.db.migrations.state import ProjectState
from django.db.models.fields import CharField, Field, IntegerField, SlugField
from typing import Any, Dict, List, Optional, Tuple, Union
class FieldOperation(Operation):
    model_name: Any = ...
    name: Any = ...
    def __init__(self, model_name: str, name: str) -> None: ...
    def model_name_lower(self) -> str: ...
    def name_lower(self) -> str: ...
    def is_same_model_operation(self, operation: FieldOperation) -> bool: ...
    def is_same_field_operation(self, operation: FieldOperation) -> bool: ...
    def references_model(self, name: str, app_label: Optional[str] = ...) -> bool: ...
    def references_field(self, model_name: str, name: str, app_label: Optional[str] = ...) -> bool: ...
    def reduce(self, operation: Union[ModelOperation, FieldOperation], in_between: Any, app_label: str = ...) -> bool: ...

class AddField(FieldOperation):
    field: Any = ...
    preserve_default: Any = ...
    def __init__(self, model_name: str, name: str, field: Field, preserve_default: bool = ...) -> None: ...
    def deconstruct(self) -> Any: ...
    def state_forwards(self, app_label: str, state: ProjectState) -> None: ...
    def database_forwards(self, app_label: str, schema_editor: DatabaseSchemaEditor, from_state: ProjectState, to_state: ProjectState) -> None: ...
    def database_backwards(self, app_label: str, schema_editor: DatabaseSchemaEditor, from_state: ProjectState, to_state: ProjectState) -> None: ...
    def describe(self) -> str: ...
    def reduce(self, operation: Union[FieldOperation, CreateModel, FieldRelatedOptionOperation], in_between: List[AddField], app_label: Optional[str] = ...) -> Union[bool, List[AddField]]: ...

class RemoveField(FieldOperation):
    def deconstruct(self) -> Tuple[str, List[Any], Dict[str, str]]: ...
    def state_forwards(self, app_label: str, state: ProjectState) -> None: ...
    def database_forwards(self, app_label: str, schema_editor: DatabaseSchemaEditor, from_state: ProjectState, to_state: ProjectState) -> None: ...
    def database_backwards(self, app_label: str, schema_editor: DatabaseSchemaEditor, from_state: ProjectState, to_state: ProjectState) -> None: ...
    def describe(self) -> str: ...

class AlterField(FieldOperation):
    field: Any = ...
    preserve_default: Any = ...
    def __init__(self, model_name: str, name: str, field: Field, preserve_default: bool = ...) -> None: ...
    def deconstruct(self) -> Union[Tuple[str, List[Any], Dict[str, Union[str, SlugField]]], Tuple[str, List[Any], Dict[str, Union[str, CharField]]], Tuple[str, List[Any], Dict[str, Union[str, IntegerField]]]]: ...
    def state_forwards(self, app_label: str, state: ProjectState) -> None: ...
    def database_forwards(self, app_label: str, schema_editor: DatabaseSchemaEditor, from_state: ProjectState, to_state: ProjectState) -> None: ...
    def database_backwards(self, app_label: str, schema_editor: DatabaseSchemaEditor, from_state: ProjectState, to_state: ProjectState) -> None: ...
    def describe(self) -> str: ...
    def reduce(self, operation: Union[AlterField, DeleteModel, AlterUniqueTogether], in_between: List[Any], app_label: str = ...) -> bool: ...

class RenameField(FieldOperation):
    old_name: Any = ...
    new_name: Any = ...
    def __init__(self, model_name: str, old_name: str, new_name: str) -> None: ...
    def old_name_lower(self) -> str: ...
    def new_name_lower(self): ...
    def deconstruct(self) -> Tuple[str, List[Any], Dict[str, str]]: ...
    def state_forwards(self, app_label: str, state: ProjectState) -> None: ...
    def database_forwards(self, app_label: Any, schema_editor: Any, from_state: Any, to_state: Any) -> None: ...
    def database_backwards(self, app_label: Any, schema_editor: Any, from_state: Any, to_state: Any) -> None: ...
    def describe(self): ...
    def references_field(self, model_name: Any, name: Any, app_label: Optional[Any] = ...): ...
    def reduce(self, operation: Union[FieldOperation, AlterUniqueTogether], in_between: List[Any], app_label: Optional[str] = ...) -> Union[bool, List[RenameField]]: ...