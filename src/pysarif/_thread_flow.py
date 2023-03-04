from __future__ import annotations
from typing import List, Optional, Any

import dataclasses
import dataclasses_json

from . import _thread_flow_location, _property_bag, _message


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL, undefined=dataclasses_json.Undefined.EXCLUDE)
@dataclasses.dataclass
class ThreadFlow(object):
    locations: List[_thread_flow_location.ThreadFlowLocation] = dataclasses.field()
    """A temporally ordered array of 'threadFlowLocation' objects, each of which describes a location visited by the tool while producing the result."""
    id: Optional[str] = dataclasses.field(default=None)
    """An string that uniquely identifies the threadFlow within the codeFlow in which it occurs."""
    immutable_state: Any = dataclasses.field(default=None)
    """Values of relevant expressions at the start of the thread flow that remain constant."""
    initial_state: Any = dataclasses.field(default=None)
    """Values of relevant expressions at the start of the thread flow that may change during thread flow execution."""
    message: Optional[_message.Message] = dataclasses.field(default=None)
    """A message relevant to the thread flow."""
    properties: Optional[_property_bag.PropertyBag] = dataclasses.field(default=None)
    """Key/value pairs that provide additional information about the thread flow."""
