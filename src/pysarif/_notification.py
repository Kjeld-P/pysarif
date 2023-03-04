from __future__ import annotations
from typing import Literal, List, Optional

import dataclasses
import dataclasses_json

from . import _property_bag, _message, _reporting_descriptor_reference, _location, _exception


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL, undefined=dataclasses_json.Undefined.EXCLUDE)
@dataclasses.dataclass
class Notification(object):
    """Describes a condition relevant to the tool itself, as opposed to being relevant to a target being analyzed by the tool."""

    message: _message.Message = dataclasses.field()
    """A message that describes the condition that was encountered."""
    associated_rule: Optional[_reporting_descriptor_reference.ReportingDescriptorReference] = dataclasses.field(default=None)
    """A reference used to locate the rule descriptor associated with this notification."""
    descriptor: Optional[_reporting_descriptor_reference.ReportingDescriptorReference] = dataclasses.field(default=None)
    """A reference used to locate the descriptor relevant to this notification."""
    exception: Optional[_exception.Exception] = dataclasses.field(default=None)
    """The runtime exception, if any, relevant to this notification."""
    level: Literal['none', 'note', 'warning', 'error'] = dataclasses.field(default="warning")
    """A value specifying the severity level of the notification."""
    locations: Optional[List[_location.Location]] = dataclasses.field(default=None)
    """The locations relevant to this notification."""
    properties: Optional[_property_bag.PropertyBag] = dataclasses.field(default=None)
    """Key/value pairs that provide additional information about the notification."""
    thread_id: Optional[int] = dataclasses.field(default=None)
    """The thread identifier of the code that generated the notification."""
    time_utc: Optional[str] = dataclasses.field(default=None)
    """The Coordinated Universal Time (UTC) date and time at which the analysis tool generated the notification."""
