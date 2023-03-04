from __future__ import annotations
from typing import List, Optional

import dataclasses
import dataclasses_json

from . import _property_bag, _location


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL, undefined=dataclasses_json.Undefined.EXCLUDE)
@dataclasses.dataclass
class StackFrame(object):
    """A function call within a stack trace."""

    location: Optional[_location.Location] = dataclasses.field(default=None)
    """The location to which this stack frame refers."""
    module: Optional[str] = dataclasses.field(default=None)
    """The name of the module that contains the code of this stack frame."""
    parameters: Optional[List[str]] = dataclasses.field(default=None)
    """The parameters of the call that is executing."""
    properties: Optional[_property_bag.PropertyBag] = dataclasses.field(default=None)
    """Key/value pairs that provide additional information about the stack frame."""
    thread_id: Optional[int] = dataclasses.field(default=None)
    """The thread identifier of the stack frame."""
