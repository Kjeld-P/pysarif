from __future__ import annotations
from typing import Optional

import dataclasses
import dataclasses_json

from . import _property_bag, _message


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL, undefined=dataclasses_json.Undefined.EXCLUDE)
@dataclasses.dataclass
class RunAutomationDetails(object):
    """Information that describes a run's identity and role within an engineering system process."""

    correlation_guid: Optional[str] = dataclasses.field(default=None)
    """A stable, unique identifier for the equivalence class of runs to which this object's containing run object belongs in the form of a GUID."""
    description: Optional[_message.Message] = dataclasses.field(default=None)
    """A description of the identity and role played within the engineering system by this object's containing run object."""
    guid: Optional[str] = dataclasses.field(default=None)
    """A stable, unique identifer for this object's containing run object in the form of a GUID."""
    id: Optional[str] = dataclasses.field(default=None)
    """A hierarchical string that uniquely identifies this object's containing run object."""
    properties: Optional[_property_bag.PropertyBag] = dataclasses.field(default=None)
    """Key/value pairs that provide additional information about the run automation details."""
