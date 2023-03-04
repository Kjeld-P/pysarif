from __future__ import annotations
from typing import Optional

import dataclasses
import dataclasses_json

from . import _property_bag, _artifact_location


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL, undefined=dataclasses_json.Undefined.EXCLUDE)
@dataclasses.dataclass
class ExternalPropertyFileReference(object):
    guid: Optional[str] = dataclasses.field(default=None)
    """A stable, unique identifer for the external property file in the form of a GUID."""
    item_count: int = dataclasses.field(default=-1)
    """A non-negative integer specifying the number of items contained in the external property file."""
    location: Optional[_artifact_location.ArtifactLocation] = dataclasses.field(default=None)
    """The location of the external property file."""
    properties: Optional[_property_bag.PropertyBag] = dataclasses.field(default=None)
    """Key/value pairs that provide additional information about the external property file."""
