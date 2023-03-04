from __future__ import annotations
from typing import Optional

import dataclasses
import dataclasses_json

from . import _property_bag


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL, undefined=dataclasses_json.Undefined.EXCLUDE)
@dataclasses.dataclass
class LogicalLocation(object):
    """A logical location of a construct that produced a result."""

    decorated_name: Optional[str] = dataclasses.field(default=None)
    """The machine-readable name for the logical location, such as a mangled function name provided by a C++ compiler that encodes calling convention, return type and other details along with the function name."""
    fully_qualified_name: Optional[str] = dataclasses.field(default=None)
    """The human-readable fully qualified name of the logical location."""
    index: int = dataclasses.field(default=-1)
    """The index within the logical locations array."""
    kind: Optional[str] = dataclasses.field(default=None)
    """The type of construct this logical location component refers to. Should be one of 'function', 'member', 'module', 'namespace', 'parameter', 'resource', 'returnType', 'type', 'variable', 'object', 'array', 'property', 'value', 'element', 'text', 'attribute', 'comment', 'declaration', 'dtd' or 'processingInstruction', if any of those accurately describe the construct."""
    name: Optional[str] = dataclasses.field(default=None)
    """Identifies the construct in which the result occurred. For example, this property might contain the name of a class or a method."""
    parent_index: int = dataclasses.field(default=-1)
    """Identifies the index of the immediate parent of the construct in which the result was detected. For example, this property might point to a logical location that represents the namespace that holds a type."""
    properties: Optional[_property_bag.PropertyBag] = dataclasses.field(default=None)
    """Key/value pairs that provide additional information about the logical location."""
