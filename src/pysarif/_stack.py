from __future__ import annotations
from typing import List, Optional

import dataclasses
import dataclasses_json

from . import _property_bag, _message, _stack_frame


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL, undefined=dataclasses_json.Undefined.EXCLUDE)
@dataclasses.dataclass
class Stack(object):
    """A call stack that is relevant to a result."""

    frames: List[_stack_frame.StackFrame] = dataclasses.field()
    """An array of stack frames that represents a sequence of calls, rendered in reverse chronological order, that comprise the call stack."""
    message: Optional[_message.Message] = dataclasses.field(default=None)
    """A message relevant to this call stack."""
    properties: Optional[_property_bag.PropertyBag] = dataclasses.field(default=None)
    """Key/value pairs that provide additional information about the stack."""
