from __future__ import annotations
from typing import List, Optional

import dataclasses
import dataclasses_json

from . import _property_bag


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL, undefined=dataclasses_json.Undefined.EXCLUDE)
@dataclasses.dataclass
class Message(object):
    """Encapsulates a message intended to be read by the end user."""

    arguments: Optional[List[str]] = dataclasses.field(default=None)
    """An array of strings to substitute into the message string."""
    id: Optional[str] = dataclasses.field(default=None)
    """The identifier for this message."""
    markdown: Optional[str] = dataclasses.field(default=None)
    """A Markdown message string."""
    properties: Optional[_property_bag.PropertyBag] = dataclasses.field(default=None)
    """Key/value pairs that provide additional information about the message."""
    text: Optional[str] = dataclasses.field(default=None)
    """A plain text message string."""
