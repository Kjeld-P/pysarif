from __future__ import annotations
from typing import List, Optional

import dataclasses
import dataclasses_json

from . import _property_bag, _message


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL, undefined=dataclasses_json.Undefined.EXCLUDE)
@dataclasses.dataclass
class LocationRelationship(object):
    """Information about the relation of one location to another."""

    target: int = dataclasses.field()
    """A reference to the related location."""
    description: Optional[_message.Message] = dataclasses.field(default=None)
    """A description of the location relationship."""
    kinds: List[str] = dataclasses.field(default_factory=lambda: ['relevant'])
    """A set of distinct strings that categorize the relationship. Well-known kinds include 'includes', 'isIncludedBy' and 'relevant'."""
    properties: Optional[_property_bag.PropertyBag] = dataclasses.field(default=None)
    """Key/value pairs that provide additional information about the location relationship."""
