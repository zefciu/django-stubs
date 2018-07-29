# Stubs for django.template.loader_tags (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .base import Node, Template, TemplateSyntaxError, TextNode, Variable, token_kwargs
from .library import Library
from typing import Any, Optional

from django.template.base import FilterExpression, NodeList, Parser, Template, Token
from django.template.context import Context
from django.utils.safestring import SafeText
from typing import Dict, Optional
register: Any
BLOCK_CONTEXT_KEY: str

class BlockContext:
    blocks: Any = ...
    def __init__(self) -> None: ...
    def add_blocks(self, blocks: Dict[str, BlockNode]) -> None: ...
    def pop(self, name: str) -> BlockNode: ...
    def push(self, name: str, block: BlockNode) -> None: ...
    def get_block(self, name: str) -> BlockNode: ...

class BlockNode(Node):
    def __init__(self, name: str, nodelist: NodeList, parent: None = ...) -> None: ...
    def __repr__(self) -> str: ...
    def render(self, context: Context) -> SafeText: ...
    def super(self) -> SafeText: ...

class ExtendsNode(Node):
    must_be_first: bool = ...
    context_key: str = ...
    nodelist: Any = ...
    parent_name: Any = ...
    template_dirs: Any = ...
    blocks: Any = ...
    def __init__(self, nodelist: NodeList, parent_name: FilterExpression, template_dirs: None = ...) -> None: ...
    def __repr__(self) -> str: ...
    def find_template(self, template_name: str, context: Context) -> Template: ...
    def get_parent(self, context: Context) -> Template: ...
    def render(self, context: Context): ...

class IncludeNode(Node):
    context_key: str = ...
    template: Any = ...
    extra_context: Any = ...
    isolated_context: Any = ...
    def __init__(self, template: FilterExpression, *args: Any, extra_context: Optional[Any] = ..., isolated_context: bool = ..., **kwargs: Any) -> None: ...
    def render(self, context: Context) -> SafeText: ...

def do_block(parser: Parser, token: Token) -> BlockNode: ...
def construct_relative_path(current_template_name: Optional[str], relative_name: str) -> str: ...
def do_extends(parser: Parser, token: Token) -> ExtendsNode: ...
def do_include(parser: Parser, token: Token) -> IncludeNode: ...