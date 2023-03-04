from __future__ import annotations
from typing import Optional

import dataclasses
import dataclasses_json

from . import _property_bag


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL, undefined=dataclasses_json.Undefined.EXCLUDE)
@dataclasses.dataclass
class MultiformatMessageString(object):
    """A message string or message format string rendered in multiple formats."""

    text: str = dataclasses.field()
    """A plain text message string or format string."""
    markdown: Optional[str] = dataclasses.field(default=None)
    """A Markdown message string or format string."""
    properties: Optional[_property_bag.PropertyBag] = dataclasses.field(default=None)
    """Key/value pairs that provide additional information about the message."""
