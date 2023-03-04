from __future__ import annotations
from typing import List, Optional

import dataclasses
import dataclasses_json

from . import _property_bag, _message, _physical_location, _logical_location, _region, _location_relationship


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL, undefined=dataclasses_json.Undefined.EXCLUDE)
@dataclasses.dataclass
class Location(object):
    """A location within a programming artifact."""

    annotations: Optional[List[_region.Region]] = dataclasses.field(default=None)
    """A set of regions relevant to the location."""
    id: int = dataclasses.field(default=-1)
    """Value that distinguishes this location from all other locations within a single result object."""
    logical_locations: Optional[List[_logical_location.LogicalLocation]] = dataclasses.field(default=None)
    """The logical locations associated with the result."""
    message: Optional[_message.Message] = dataclasses.field(default=None)
    """A message relevant to the location."""
    physical_location: Optional[_physical_location.PhysicalLocation] = dataclasses.field(default=None)
    """Identifies the artifact and region."""
    properties: Optional[_property_bag.PropertyBag] = dataclasses.field(default=None)
    """Key/value pairs that provide additional information about the location."""
    relationships: Optional[List[_location_relationship.LocationRelationship]] = dataclasses.field(default=None)
    """An array of objects that describe relationships between this location and others."""
