from __future__ import annotations
from typing import Optional

import dataclasses
import dataclasses_json

from . import _property_bag, _address, _region, _artifact_location


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL, undefined=dataclasses_json.Undefined.EXCLUDE)
@dataclasses.dataclass
class PhysicalLocation(object):
    """A physical location relevant to a result. Specifies a reference to a programming artifact together with a range of bytes or characters within that artifact."""

    address: Optional[_address.Address] = dataclasses.field(default=None)
    """The address of the location."""
    artifact_location: Optional[_artifact_location.ArtifactLocation] = dataclasses.field(default=None)
    """The location of the artifact."""
    context_region: Optional[_region.Region] = dataclasses.field(default=None)
    """Specifies a portion of the artifact that encloses the region. Allows a viewer to display additional context around the region."""
    properties: Optional[_property_bag.PropertyBag] = dataclasses.field(default=None)
    """Key/value pairs that provide additional information about the physical location."""
    region: Optional[_region.Region] = dataclasses.field(default=None)
    """Specifies a portion of the artifact."""
