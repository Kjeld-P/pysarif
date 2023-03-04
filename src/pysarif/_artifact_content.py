from __future__ import annotations
from typing import Optional

import dataclasses
import dataclasses_json

from . import _property_bag, _multiformat_message_string


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL, undefined=dataclasses_json.Undefined.EXCLUDE)
@dataclasses.dataclass
class ArtifactContent(object):
    """Represents the contents of an artifact."""

    binary: Optional[str] = dataclasses.field(default=None)
    """MIME Base64-encoded content from a binary artifact, or from a text artifact in its original encoding."""
    properties: Optional[_property_bag.PropertyBag] = dataclasses.field(default=None)
    """Key/value pairs that provide additional information about the artifact content."""
    rendered: Optional[_multiformat_message_string.MultiformatMessageString] = dataclasses.field(default=None)
    """An alternate rendered representation of the artifact (e.g., a decompiled representation of a binary region)."""
    text: Optional[str] = dataclasses.field(default=None)
    """UTF-8-encoded content from a text artifact."""
