from __future__ import annotations
from typing import Optional, Any

import dataclasses
import dataclasses_json

from . import _property_bag, _message


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL, undefined=dataclasses_json.Undefined.EXCLUDE)
@dataclasses.dataclass
class EdgeTraversal(object):
    """Represents the traversal of a single edge during a graph traversal."""

    edge_id: str = dataclasses.field()
    """Identifies the edge being traversed."""
    final_state: Any = dataclasses.field(default=None)
    """The values of relevant expressions after the edge has been traversed."""
    message: Optional[_message.Message] = dataclasses.field(default=None)
    """A message to display to the user as the edge is traversed."""
    properties: Optional[_property_bag.PropertyBag] = dataclasses.field(default=None)
    """Key/value pairs that provide additional information about the edge traversal."""
    step_over_edge_count: Optional[int] = dataclasses.field(default=None)
    """The number of edge traversals necessary to return from a nested graph."""
