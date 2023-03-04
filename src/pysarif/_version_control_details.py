from __future__ import annotations
from typing import Optional

import dataclasses
import dataclasses_json

from . import _property_bag, _artifact_location


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL, undefined=dataclasses_json.Undefined.EXCLUDE)
@dataclasses.dataclass
class VersionControlDetails(object):
    """Specifies the information necessary to retrieve a desired revision from a version control system."""

    repository_uri: str = dataclasses.field()
    """The absolute URI of the repository."""
    as_of_time_utc: Optional[str] = dataclasses.field(default=None)
    """A Coordinated Universal Time (UTC) date and time that can be used to synchronize an enlistment to the state of the repository at that time."""
    branch: Optional[str] = dataclasses.field(default=None)
    """The name of a branch containing the revision."""
    mapped_to: Optional[_artifact_location.ArtifactLocation] = dataclasses.field(default=None)
    """The location in the local file system to which the root of the repository was mapped at the time of the analysis."""
    properties: Optional[_property_bag.PropertyBag] = dataclasses.field(default=None)
    """Key/value pairs that provide additional information about the version control details."""
    revision_id: Optional[str] = dataclasses.field(default=None)
    """A string that uniquely and permanently identifies the revision within the repository."""
    revision_tag: Optional[str] = dataclasses.field(default=None)
    """A tag that has been applied to the revision."""
