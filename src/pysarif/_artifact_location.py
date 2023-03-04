from __future__ import annotations
from typing import Optional

import dataclasses
import dataclasses_json

from . import _property_bag, _message


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL, undefined=dataclasses_json.Undefined.EXCLUDE)
@dataclasses.dataclass
class ArtifactLocation(object):
    """Specifies the location of an artifact."""

    description: Optional[_message.Message] = dataclasses.field(default=None)
    """A short description of the artifact location."""
    index: int = dataclasses.field(default=-1)
    """The index within the run artifacts array of the artifact object associated with the artifact location."""
    properties: Optional[_property_bag.PropertyBag] = dataclasses.field(default=None)
    """Key/value pairs that provide additional information about the artifact location."""
    uri: Optional[str] = dataclasses.field(default=None)
    """A string containing a valid relative or absolute URI."""
    uri_base_id: Optional[str] = dataclasses.field(default=None)
    """A string which indirectly specifies the absolute URI with respect to which a relative URI in the "uri" property is interpreted."""
