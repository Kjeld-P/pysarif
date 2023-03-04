from __future__ import annotations
from typing import Optional

import dataclasses
import dataclasses_json

from . import _property_bag, _message, _artifact_content


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL, undefined=dataclasses_json.Undefined.EXCLUDE)
@dataclasses.dataclass
class Region(object):
    """A region within an artifact where a result was detected."""

    byte_length: Optional[int] = dataclasses.field(default=None)
    """The length of the region in bytes."""
    byte_offset: int = dataclasses.field(default=-1)
    """The zero-based offset from the beginning of the artifact of the first byte in the region."""
    char_length: Optional[int] = dataclasses.field(default=None)
    """The length of the region in characters."""
    char_offset: int = dataclasses.field(default=-1)
    """The zero-based offset from the beginning of the artifact of the first character in the region."""
    end_column: Optional[int] = dataclasses.field(default=None)
    """The column number of the character following the end of the region."""
    end_line: Optional[int] = dataclasses.field(default=None)
    """The line number of the last character in the region."""
    message: Optional[_message.Message] = dataclasses.field(default=None)
    """A message relevant to the region."""
    properties: Optional[_property_bag.PropertyBag] = dataclasses.field(default=None)
    """Key/value pairs that provide additional information about the region."""
    snippet: Optional[_artifact_content.ArtifactContent] = dataclasses.field(default=None)
    """The portion of the artifact contents within the specified region."""
    source_language: Optional[str] = dataclasses.field(default=None)
    """Specifies the source language, if any, of the portion of the artifact specified by the region object."""
    start_column: Optional[int] = dataclasses.field(default=None)
    """The column number of the first character in the region."""
    start_line: Optional[int] = dataclasses.field(default=None)
    """The line number of the first character in the region."""
