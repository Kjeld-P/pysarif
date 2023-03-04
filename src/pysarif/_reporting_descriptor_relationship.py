from __future__ import annotations
from typing import List, Optional

import dataclasses
import dataclasses_json

from . import _property_bag, _reporting_descriptor_reference, _message


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL, undefined=dataclasses_json.Undefined.EXCLUDE)
@dataclasses.dataclass
class ReportingDescriptorRelationship(object):
    """Information about the relation of one reporting descriptor to another."""

    target: _reporting_descriptor_reference.ReportingDescriptorReference = dataclasses.field()
    """A reference to the related reporting descriptor."""
    description: Optional[_message.Message] = dataclasses.field(default=None)
    """A description of the reporting descriptor relationship."""
    kinds: List[str] = dataclasses.field(default_factory=lambda: ['relevant'])
    """A set of distinct strings that categorize the relationship. Well-known kinds include 'canPrecede', 'canFollow', 'willPrecede', 'willFollow', 'superset', 'subset', 'equal', 'disjoint', 'relevant', and 'incomparable'."""
    properties: Optional[_property_bag.PropertyBag] = dataclasses.field(default=None)
    """Key/value pairs that provide additional information about the reporting descriptor reference."""
