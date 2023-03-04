from __future__ import annotations
from typing import Any, List, Optional

import dataclasses
import dataclasses_json

from . import _property_bag, _multiformat_message_string, _reporting_descriptor_relationship, _reporting_configuration


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL, undefined=dataclasses_json.Undefined.EXCLUDE)
@dataclasses.dataclass
class ReportingDescriptor(object):
    """Metadata that describes a specific report produced by the tool, as part of the analysis it provides or its runtime reporting."""

    id: str = dataclasses.field()
    """A stable, opaque identifier for the report."""
    default_configuration: Optional[_reporting_configuration.ReportingConfiguration] = dataclasses.field(default=None)
    """Default reporting configuration information."""
    deprecated_guids: Optional[List[str]] = dataclasses.field(default=None)
    """An array of unique identifies in the form of a GUID by which this report was known in some previous version of the analysis tool."""
    deprecated_ids: Optional[List[str]] = dataclasses.field(default=None)
    """An array of stable, opaque identifiers by which this report was known in some previous version of the analysis tool."""
    deprecated_names: Optional[List[str]] = dataclasses.field(default=None)
    """An array of readable identifiers by which this report was known in some previous version of the analysis tool."""
    full_description: Optional[_multiformat_message_string.MultiformatMessageString] = dataclasses.field(default=None)
    """A description of the report. Should, as far as possible, provide details sufficient to enable resolution of any problem indicated by the result."""
    guid: Optional[str] = dataclasses.field(default=None)
    """A unique identifer for the reporting descriptor in the form of a GUID."""
    help: Optional[_multiformat_message_string.MultiformatMessageString] = dataclasses.field(default=None)
    """Provides the primary documentation for the report, useful when there is no online documentation."""
    help_uri: Optional[str] = dataclasses.field(default=None)
    """A URI where the primary documentation for the report can be found."""
    message_strings: Any = dataclasses.field(default=None)
    """A set of name/value pairs with arbitrary names. Each value is a multiformatMessageString object, which holds message strings in plain text and (optionally) Markdown format. The strings can include placeholders, which can be used to construct a message in combination with an arbitrary number of additional string arguments."""
    name: Optional[str] = dataclasses.field(default=None)
    """A report identifier that is understandable to an end user."""
    properties: Optional[_property_bag.PropertyBag] = dataclasses.field(default=None)
    """Key/value pairs that provide additional information about the report."""
    relationships: Optional[List[_reporting_descriptor_relationship.ReportingDescriptorRelationship]] = dataclasses.field(default=None)
    """An array of objects that describe relationships between this reporting descriptor and others."""
    short_description: Optional[_multiformat_message_string.MultiformatMessageString] = dataclasses.field(default=None)
    """A concise description of the report. Should be a single sentence that is understandable when visible space is limited to a single line of text."""
