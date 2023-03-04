from __future__ import annotations
from typing import Optional

import dataclasses
import dataclasses_json

from . import _property_bag


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL, undefined=dataclasses_json.Undefined.EXCLUDE)
@dataclasses.dataclass
class ToolComponentReference(object):
    guid: Optional[str] = dataclasses.field(default=None)
    """The 'guid' property of the referenced toolComponent."""
    index: int = dataclasses.field(default=-1)
    """An index into the referenced toolComponent in tool.extensions."""
    name: Optional[str] = dataclasses.field(default=None)
    """The 'name' property of the referenced toolComponent."""
    properties: Optional[_property_bag.PropertyBag] = dataclasses.field(default=None)
    """Key/value pairs that provide additional information about the toolComponentReference."""
