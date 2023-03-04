from __future__ import annotations
from typing import List, Optional

import dataclasses
import dataclasses_json

from . import _edge, _node, _message, _property_bag


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL, undefined=dataclasses_json.Undefined.EXCLUDE)
@dataclasses.dataclass
class Graph(object):
    """A network of nodes and directed edges that describes some aspect of the structure of the code (for example, a call graph)."""

    description: Optional[_message.Message] = dataclasses.field(default=None)
    """A description of the graph."""
    edges: Optional[List[_edge.Edge]] = dataclasses.field(default=None)
    """An array of edge objects representing the edges of the graph."""
    nodes: Optional[List[_node.Node]] = dataclasses.field(default=None)
    """An array of node objects representing the nodes of the graph."""
    properties: Optional[_property_bag.PropertyBag] = dataclasses.field(default=None)
    """Key/value pairs that provide additional information about the graph."""
