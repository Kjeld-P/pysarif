from __future__ import annotations
from typing import Optional

import dataclasses
import dataclasses_json

from . import _property_bag, _tool_component_reference


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL, undefined=dataclasses_json.Undefined.EXCLUDE)
@dataclasses.dataclass
class ReportingDescriptorReference(object):
    """Information about how to locate a relevant reporting descriptor."""

    guid: Optional[str] = dataclasses.field(default=None)
    """A guid that uniquely identifies the descriptor."""
    id: Optional[str] = dataclasses.field(default=None)
    """The id of the descriptor."""
    index: int = dataclasses.field(default=-1)
    """The index into an array of descriptors in toolComponent.ruleDescriptors, toolComponent.notificationDescriptors, or toolComponent.taxonomyDescriptors, depending on context."""
    properties: Optional[_property_bag.PropertyBag] = dataclasses.field(default=None)
    """Key/value pairs that provide additional information about the reporting descriptor reference."""
    tool_component: Optional[_tool_component_reference.ToolComponentReference] = dataclasses.field(default=None)
    """A reference used to locate the toolComponent associated with the descriptor."""
