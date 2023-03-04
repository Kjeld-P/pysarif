from __future__ import annotations
from typing import Optional

import dataclasses
import dataclasses_json

from . import _property_bag, _message


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL, undefined=dataclasses_json.Undefined.EXCLUDE)
@dataclasses.dataclass
class Rectangle(object):
    """An area within an image."""

    bottom: Optional[float] = dataclasses.field(default=None)
    """The Y coordinate of the bottom edge of the rectangle, measured in the image's natural units."""
    left: Optional[float] = dataclasses.field(default=None)
    """The X coordinate of the left edge of the rectangle, measured in the image's natural units."""
    message: Optional[_message.Message] = dataclasses.field(default=None)
    """A message relevant to the rectangle."""
    properties: Optional[_property_bag.PropertyBag] = dataclasses.field(default=None)
    """Key/value pairs that provide additional information about the rectangle."""
    right: Optional[float] = dataclasses.field(default=None)
    """The X coordinate of the right edge of the rectangle, measured in the image's natural units."""
    top: Optional[float] = dataclasses.field(default=None)
    """The Y coordinate of the top edge of the rectangle, measured in the image's natural units."""
