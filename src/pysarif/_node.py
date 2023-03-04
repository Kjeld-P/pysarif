from __future__ import annotations
from typing import List, Optional

import dataclasses
import dataclasses_json

from . import _property_bag, _node, _message, _location


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL, undefined=dataclasses_json.Undefined.EXCLUDE)
@dataclasses.dataclass
class Node(object):
    """Represents a node in a graph."""

    id: str = dataclasses.field()
    """A string that uniquely identifies the node within its graph."""
    children: Optional[List[_node.Node]] = dataclasses.field(default=None)
    """Array of child nodes."""
    label: Optional[_message.Message] = dataclasses.field(default=None)
    """A short description of the node."""
    location: Optional[_location.Location] = dataclasses.field(default=None)
    """A code location associated with the node."""
    properties: Optional[_property_bag.PropertyBag] = dataclasses.field(default=None)
    """Key/value pairs that provide additional information about the node."""
