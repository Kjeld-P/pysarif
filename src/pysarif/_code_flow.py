from __future__ import annotations
from typing import List, Optional

import dataclasses
import dataclasses_json

from . import _property_bag, _message, _thread_flow


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL, undefined=dataclasses_json.Undefined.EXCLUDE)
@dataclasses.dataclass
class CodeFlow(object):
    """A set of threadFlows which together describe a pattern of code execution relevant to detecting a result."""

    thread_flows: List[_thread_flow.ThreadFlow] = dataclasses.field()
    """An array of one or more unique threadFlow objects, each of which describes the progress of a program through a thread of execution."""
    message: Optional[_message.Message] = dataclasses.field(default=None)
    """A message relevant to the code flow."""
    properties: Optional[_property_bag.PropertyBag] = dataclasses.field(default=None)
    """Key/value pairs that provide additional information about the code flow."""
