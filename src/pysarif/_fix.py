from __future__ import annotations
from typing import List, Optional

import dataclasses
import dataclasses_json

from . import _property_bag, _artifact_change, _message


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL, undefined=dataclasses_json.Undefined.EXCLUDE)
@dataclasses.dataclass
class Fix(object):
    """A proposed fix for the problem represented by a result object. A fix specifies a set of artifacts to modify. For each artifact, it specifies a set of bytes to remove, and provides a set of new bytes to replace them."""

    artifact_changes: List[_artifact_change.ArtifactChange] = dataclasses.field()
    """One or more artifact changes that comprise a fix for a result."""
    description: Optional[_message.Message] = dataclasses.field(default=None)
    """A message that describes the proposed fix, enabling viewers to present the proposed change to an end user."""
    properties: Optional[_property_bag.PropertyBag] = dataclasses.field(default=None)
    """Key/value pairs that provide additional information about the fix."""
