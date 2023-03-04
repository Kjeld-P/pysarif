from __future__ import annotations
from typing import List, Optional

import dataclasses
import dataclasses_json

from . import _property_bag, _physical_location


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL, undefined=dataclasses_json.Undefined.EXCLUDE)
@dataclasses.dataclass
class ResultProvenance(object):
    """Contains information about how and when a result was detected."""

    conversion_sources: Optional[List[_physical_location.PhysicalLocation]] = dataclasses.field(default=None)
    """An array of physicalLocation objects which specify the portions of an analysis tool's output that a converter transformed into the result."""
    first_detection_run_guid: Optional[str] = dataclasses.field(default=None)
    """A GUID-valued string equal to the automationDetails.guid property of the run in which the result was first detected."""
    first_detection_time_utc: Optional[str] = dataclasses.field(default=None)
    """The Coordinated Universal Time (UTC) date and time at which the result was first detected. See "Date/time properties" in the SARIF spec for the required format."""
    invocation_index: int = dataclasses.field(default=-1)
    """The index within the run.invocations array of the invocation object which describes the tool invocation that detected the result."""
    last_detection_run_guid: Optional[str] = dataclasses.field(default=None)
    """A GUID-valued string equal to the automationDetails.guid property of the run in which the result was most recently detected."""
    last_detection_time_utc: Optional[str] = dataclasses.field(default=None)
    """The Coordinated Universal Time (UTC) date and time at which the result was most recently detected. See "Date/time properties" in the SARIF spec for the required format."""
    properties: Optional[_property_bag.PropertyBag] = dataclasses.field(default=None)
    """Key/value pairs that provide additional information about the result."""
