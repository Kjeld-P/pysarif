from __future__ import annotations
from typing import List, Optional, Any

import dataclasses
import dataclasses_json

from . import _property_bag, _edge_traversal, _message


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL, undefined=dataclasses_json.Undefined.EXCLUDE)
@dataclasses.dataclass
class GraphTraversal(object):
    """Represents a path through a graph."""

    description: Optional[_message.Message] = dataclasses.field(default=None)
    """A description of this graph traversal."""
    edge_traversals: Optional[List[_edge_traversal.EdgeTraversal]] = dataclasses.field(default=None)
    """The sequences of edges traversed by this graph traversal."""
    immutable_state: Any = dataclasses.field(default=None)
    """Values of relevant expressions at the start of the graph traversal that remain constant for the graph traversal."""
    initial_state: Any = dataclasses.field(default=None)
    """Values of relevant expressions at the start of the graph traversal that may change during graph traversal."""
    properties: Optional[_property_bag.PropertyBag] = dataclasses.field(default=None)
    """Key/value pairs that provide additional information about the graph traversal."""
    result_graph_index: int = dataclasses.field(default=-1)
    """The index within the result.graphs to be associated with the result."""
    run_graph_index: int = dataclasses.field(default=-1)
    """The index within the run.graphs to be associated with the result."""
