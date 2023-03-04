from __future__ import annotations
from typing import List, Optional

import dataclasses
import dataclasses_json

from . import _property_bag, _message, _region, _artifact_location, _rectangle


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL, undefined=dataclasses_json.Undefined.EXCLUDE)
@dataclasses.dataclass
class Attachment(object):
    """An artifact relevant to a result."""

    artifact_location: _artifact_location.ArtifactLocation = dataclasses.field()
    """The location of the attachment."""
    description: Optional[_message.Message] = dataclasses.field(default=None)
    """A message describing the role played by the attachment."""
    properties: Optional[_property_bag.PropertyBag] = dataclasses.field(default=None)
    """Key/value pairs that provide additional information about the attachment."""
    rectangles: Optional[List[_rectangle.Rectangle]] = dataclasses.field(default=None)
    """An array of rectangles specifying areas of interest within the image."""
    regions: Optional[List[_region.Region]] = dataclasses.field(default=None)
    """An array of regions of interest within the attachment."""
