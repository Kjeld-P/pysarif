from __future__ import annotations
from typing import Optional

import dataclasses
import dataclasses_json

from . import _property_bag, _reporting_descriptor_reference, _reporting_configuration


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL, undefined=dataclasses_json.Undefined.EXCLUDE)
@dataclasses.dataclass
class ConfigurationOverride(object):
    """Information about how a specific rule or notification was reconfigured at runtime."""

    configuration: _reporting_configuration.ReportingConfiguration = dataclasses.field()
    """Specifies how the rule or notification was configured during the scan."""
    descriptor: _reporting_descriptor_reference.ReportingDescriptorReference = dataclasses.field()
    """A reference used to locate the descriptor whose configuration was overridden."""
    properties: Optional[_property_bag.PropertyBag] = dataclasses.field(default=None)
    """Key/value pairs that provide additional information about the configuration override."""
