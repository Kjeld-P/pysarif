from __future__ import annotations
from typing import List, Optional

import dataclasses
import dataclasses_json

from . import _property_bag, _tool_component


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL, undefined=dataclasses_json.Undefined.EXCLUDE)
@dataclasses.dataclass
class Tool(object):
    """The analysis tool that was run."""

    driver: _tool_component.ToolComponent = dataclasses.field()
    """The analysis tool that was run."""
    extensions: Optional[List[_tool_component.ToolComponent]] = dataclasses.field(default=None)
    """Tool extensions that contributed to or reconfigured the analysis tool that was run."""
    properties: Optional[_property_bag.PropertyBag] = dataclasses.field(default=None)
    """Key/value pairs that provide additional information about the tool."""
