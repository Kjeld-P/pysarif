from __future__ import annotations
from typing import List, Optional

import dataclasses
import dataclasses_json

from . import _property_bag, _stack, _exception


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL, undefined=dataclasses_json.Undefined.EXCLUDE)
@dataclasses.dataclass
class Exception(object):
    inner_exceptions: Optional[List[_exception.Exception]] = dataclasses.field(default=None)
    """An array of exception objects each of which is considered a cause of this exception."""
    kind: Optional[str] = dataclasses.field(default=None)
    """A string that identifies the kind of exception, for example, the fully qualified type name of an object that was thrown, or the symbolic name of a signal."""
    message: Optional[str] = dataclasses.field(default=None)
    """A message that describes the exception."""
    properties: Optional[_property_bag.PropertyBag] = dataclasses.field(default=None)
    """Key/value pairs that provide additional information about the exception."""
    stack: Optional[_stack.Stack] = dataclasses.field(default=None)
    """The sequence of function calls leading to the exception."""
