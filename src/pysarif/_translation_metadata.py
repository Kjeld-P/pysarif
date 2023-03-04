from __future__ import annotations
from typing import Optional

import dataclasses
import dataclasses_json

from . import _property_bag, _multiformat_message_string


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL, undefined=dataclasses_json.Undefined.EXCLUDE)
@dataclasses.dataclass
class TranslationMetadata(object):
    """Provides additional metadata related to translation."""

    name: str = dataclasses.field()
    """The name associated with the translation metadata."""
    download_uri: Optional[str] = dataclasses.field(default=None)
    """The absolute URI from which the translation metadata can be downloaded."""
    full_description: Optional[_multiformat_message_string.MultiformatMessageString] = dataclasses.field(default=None)
    """A comprehensive description of the translation metadata."""
    full_name: Optional[str] = dataclasses.field(default=None)
    """The full name associated with the translation metadata."""
    information_uri: Optional[str] = dataclasses.field(default=None)
    """The absolute URI from which information related to the translation metadata can be downloaded."""
    properties: Optional[_property_bag.PropertyBag] = dataclasses.field(default=None)
    """Key/value pairs that provide additional information about the translation metadata."""
    short_description: Optional[_multiformat_message_string.MultiformatMessageString] = dataclasses.field(default=None)
    """A brief description of the translation metadata."""
