from __future__ import annotations
from typing import Literal, List, Optional

import dataclasses
import dataclasses_json

from . import _run, _property_bag, _external_properties


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL, undefined=dataclasses_json.Undefined.EXCLUDE)
@dataclasses.dataclass
class SarifLog(object):
    """Static Analysis Results Format (SARIF) Version 2.1.0 JSON Schema: a standard format for the output of static analysis tools."""

    runs: List[_run.Run] = dataclasses.field()
    """The set of runs contained in this log file."""
    version: Literal['2.1.0'] = dataclasses.field()
    """The SARIF format version of this log file."""
    schema: Optional[str] = dataclasses.field(default=None)
    """The URI of the JSON schema corresponding to the version."""
    inline_external_properties: Optional[List[_external_properties.ExternalProperties]] = dataclasses.field(default=None)
    """References to external property files that share data between runs."""
    properties: Optional[_property_bag.PropertyBag] = dataclasses.field(default=None)
    """Key/value pairs that provide additional information about the log file."""
