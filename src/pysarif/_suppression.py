from __future__ import annotations
from typing import Literal, Optional

import dataclasses
import dataclasses_json

from . import _property_bag, _location


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL, undefined=dataclasses_json.Undefined.EXCLUDE)
@dataclasses.dataclass
class Suppression(object):
    """A suppression that is relevant to a result."""

    kind: Literal['inSource', 'external'] = dataclasses.field()
    """A string that indicates where the suppression is persisted."""
    guid: Optional[str] = dataclasses.field(default=None)
    """A stable, unique identifer for the suprression in the form of a GUID."""
    justification: Optional[str] = dataclasses.field(default=None)
    """A string representing the justification for the suppression."""
    location: Optional[_location.Location] = dataclasses.field(default=None)
    """Identifies the location associated with the suppression."""
    properties: Optional[_property_bag.PropertyBag] = dataclasses.field(default=None)
    """Key/value pairs that provide additional information about the suppression."""
    state: Optional[Literal['accepted', 'underReview', 'rejected']] = dataclasses.field(default=None)
    """A string that indicates the state of the suppression."""
