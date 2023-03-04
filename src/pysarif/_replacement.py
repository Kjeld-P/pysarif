from __future__ import annotations
from typing import Optional

import dataclasses
import dataclasses_json

from . import _artifact_content, _property_bag, _region


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL, undefined=dataclasses_json.Undefined.EXCLUDE)
@dataclasses.dataclass
class Replacement(object):
    """The replacement of a single region of an artifact."""

    deleted_region: _region.Region = dataclasses.field()
    """The region of the artifact to delete."""
    inserted_content: Optional[_artifact_content.ArtifactContent] = dataclasses.field(default=None)
    """The content to insert at the location specified by the 'deletedRegion' property."""
    properties: Optional[_property_bag.PropertyBag] = dataclasses.field(default=None)
    """Key/value pairs that provide additional information about the replacement."""
