from __future__ import annotations
from typing import Any, Literal, List, Optional

import dataclasses
import dataclasses_json

from . import _property_bag, _reporting_descriptor_reference, _web_request, _web_response, _location, _stack


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL, undefined=dataclasses_json.Undefined.EXCLUDE)
@dataclasses.dataclass
class ThreadFlowLocation(object):
    """A location visited by an analysis tool while simulating or monitoring the execution of a program."""

    execution_order: int = dataclasses.field(default=-1)
    """An integer representing the temporal order in which execution reached this location."""
    execution_time_utc: Optional[str] = dataclasses.field(default=None)
    """The Coordinated Universal Time (UTC) date and time at which this location was executed."""
    importance: Literal['important', 'essential', 'unimportant'] = dataclasses.field(default="important")
    """Specifies the importance of this location in understanding the code flow in which it occurs. The order from most to least important is "essential", "important", "unimportant". Default: "important"."""
    index: int = dataclasses.field(default=-1)
    """The index within the run threadFlowLocations array."""
    kinds: Optional[List[str]] = dataclasses.field(default=None)
    """A set of distinct strings that categorize the thread flow location. Well-known kinds include 'acquire', 'release', 'enter', 'exit', 'call', 'return', 'branch', 'implicit', 'false', 'true', 'caution', 'danger', 'unknown', 'unreachable', 'taint', 'function', 'handler', 'lock', 'memory', 'resource', 'scope' and 'value'."""
    location: Optional[_location.Location] = dataclasses.field(default=None)
    """The code location."""
    module: Optional[str] = dataclasses.field(default=None)
    """The name of the module that contains the code that is executing."""
    nesting_level: Optional[int] = dataclasses.field(default=None)
    """An integer representing a containment hierarchy within the thread flow."""
    properties: Optional[_property_bag.PropertyBag] = dataclasses.field(default=None)
    """Key/value pairs that provide additional information about the threadflow location."""
    stack: Optional[_stack.Stack] = dataclasses.field(default=None)
    """The call stack leading to this location."""
    state: Any = dataclasses.field(default=None)
    """A dictionary, each of whose keys specifies a variable or expression, the associated value of which represents the variable or expression value. For an annotation of kind 'continuation', for example, this dictionary might hold the current assumed values of a set of global variables."""
    taxa: Optional[List[_reporting_descriptor_reference.ReportingDescriptorReference]] = dataclasses.field(default=None)
    """An array of references to rule or taxonomy reporting descriptors that are applicable to the thread flow location."""
    web_request: Optional[_web_request.WebRequest] = dataclasses.field(default=None)
    """A web request associated with this thread flow location."""
    web_response: Optional[_web_response.WebResponse] = dataclasses.field(default=None)
    """A web response associated with this thread flow location."""
