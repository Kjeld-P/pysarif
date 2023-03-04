from __future__ import annotations
from typing import Optional

import dataclasses
import dataclasses_json

from . import _property_bag, _message


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL, undefined=dataclasses_json.Undefined.EXCLUDE)
@dataclasses.dataclass
class Edge(object):
    """Represents a directed edge in a graph."""

    id: str = dataclasses.field()
    """A string that uniquely identifies the edge within its graph."""
    source_node_id: str = dataclasses.field()
    """Identifies the source node (the node at which the edge starts)."""
    target_node_id: str = dataclasses.field()
    """Identifies the target node (the node at which the edge ends)."""
    label: Optional[_message.Message] = dataclasses.field(default=None)
    """A short description of the edge."""
    properties: Optional[_property_bag.PropertyBag] = dataclasses.field(default=None)
    """Key/value pairs that provide additional information about the edge."""
