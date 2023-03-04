from __future__ import annotations
from typing import List, Optional

import dataclasses
import dataclasses_json

from . import _property_bag, _invocation, _tool, _artifact_location


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL, undefined=dataclasses_json.Undefined.EXCLUDE)
@dataclasses.dataclass
class Conversion(object):
    """Describes how a converter transformed the output of a static analysis tool from the analysis tool's native output format into the SARIF format."""

    tool: _tool.Tool = dataclasses.field()
    """A tool object that describes the converter."""
    analysis_tool_log_files: Optional[List[_artifact_location.ArtifactLocation]] = dataclasses.field(default=None)
    """The locations of the analysis tool's per-run log files."""
    invocation: Optional[_invocation.Invocation] = dataclasses.field(default=None)
    """An invocation object that describes the invocation of the converter."""
    properties: Optional[_property_bag.PropertyBag] = dataclasses.field(default=None)
    """Key/value pairs that provide additional information about the conversion."""
