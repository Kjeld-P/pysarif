from __future__ import annotations
from typing import Any, Literal, List, Optional

import dataclasses
import dataclasses_json

from . import _artifact_content, _property_bag, _message, _artifact_location


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL, undefined=dataclasses_json.Undefined.EXCLUDE)
@dataclasses.dataclass
class Artifact(object):
    """A single artifact. In some cases, this artifact might be nested within another artifact."""

    contents: Optional[_artifact_content.ArtifactContent] = dataclasses.field(default=None)
    """The contents of the artifact."""
    description: Optional[_message.Message] = dataclasses.field(default=None)
    """A short description of the artifact."""
    encoding: Optional[str] = dataclasses.field(default=None)
    """Specifies the encoding for an artifact object that refers to a text file."""
    hashes: Any = dataclasses.field(default=None)
    """A dictionary, each of whose keys is the name of a hash function and each of whose values is the hashed value of the artifact produced by the specified hash function."""
    last_modified_time_utc: Optional[str] = dataclasses.field(default=None)
    """The Coordinated Universal Time (UTC) date and time at which the artifact was most recently modified. See "Date/time properties" in the SARIF spec for the required format."""
    length: int = dataclasses.field(default=-1)
    """The length of the artifact in bytes."""
    location: Optional[_artifact_location.ArtifactLocation] = dataclasses.field(default=None)
    """The location of the artifact."""
    mime_type: Optional[str] = dataclasses.field(default=None)
    """The MIME type (RFC 2045) of the artifact."""
    offset: Optional[int] = dataclasses.field(default=None)
    """The offset in bytes of the artifact within its containing artifact."""
    parent_index: int = dataclasses.field(default=-1)
    """Identifies the index of the immediate parent of the artifact, if this artifact is nested."""
    properties: Optional[_property_bag.PropertyBag] = dataclasses.field(default=None)
    """Key/value pairs that provide additional information about the artifact."""
    roles: Optional[List[Literal['analysisTarget', 'attachment', 'responseFile', 'resultFile', 'standardStream', 'tracedFile', 'unmodified', 'modified', 'added', 'deleted', 'renamed', 'uncontrolled', 'driver', 'extension', 'translation', 'taxonomy', 'policy', 'referencedOnCommandLine', 'memoryContents', 'directory', 'userSpecifiedConfiguration', 'toolSpecifiedConfiguration', 'debugOutputFile']]] = dataclasses.field(default=None)
    """The role or roles played by the artifact in the analysis."""
    source_language: Optional[str] = dataclasses.field(default=None)
    """Specifies the source language for any artifact object that refers to a text file that contains source code."""
