from __future__ import annotations
from typing import Optional

import dataclasses
import dataclasses_json

from . import _property_bag, _artifact_location


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL, undefined=dataclasses_json.Undefined.EXCLUDE)
@dataclasses.dataclass
class SpecialLocations(object):
    """Defines locations of special significance to SARIF consumers."""

    display_base: Optional[_artifact_location.ArtifactLocation] = dataclasses.field(default=None)
    """Provides a suggestion to SARIF consumers to display file paths relative to the specified location."""
    properties: Optional[_property_bag.PropertyBag] = dataclasses.field(default=None)
    """Key/value pairs that provide additional information about the special locations."""
