from __future__ import annotations
from typing import List, Optional

import dataclasses
import dataclasses_json

from . import _property_bag, _replacement, _artifact_location


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL, undefined=dataclasses_json.Undefined.EXCLUDE)
@dataclasses.dataclass
class ArtifactChange(object):
    """A change to a single artifact."""

    artifact_location: _artifact_location.ArtifactLocation = dataclasses.field()
    """The location of the artifact to change."""
    replacements: List[_replacement.Replacement] = dataclasses.field()
    """An array of replacement objects, each of which represents the replacement of a single region in a single artifact specified by 'artifactLocation'."""
    properties: Optional[_property_bag.PropertyBag] = dataclasses.field(default=None)
    """Key/value pairs that provide additional information about the change."""
