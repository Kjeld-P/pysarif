from __future__ import annotations
from typing import Literal, Optional

import dataclasses
import dataclasses_json

from . import _property_bag


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL, undefined=dataclasses_json.Undefined.EXCLUDE)
@dataclasses.dataclass
class ReportingConfiguration(object):
    """Information about a rule or notification that can be configured at runtime."""

    enabled: bool = dataclasses.field(default=True)
    """Specifies whether the report may be produced during the scan."""
    level: Literal['none', 'note', 'warning', 'error'] = dataclasses.field(default="warning")
    """Specifies the failure level for the report."""
    parameters: Optional[_property_bag.PropertyBag] = dataclasses.field(default=None)
    """Contains configuration information specific to a report."""
    properties: Optional[_property_bag.PropertyBag] = dataclasses.field(default=None)
    """Key/value pairs that provide additional information about the reporting configuration."""
    rank: float = dataclasses.field(default=-1.0)
    """Specifies the relative priority of the report. Used for analysis output only."""
