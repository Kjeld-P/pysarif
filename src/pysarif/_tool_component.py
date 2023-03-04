from __future__ import annotations
from typing import Any, Literal, List, Optional

import dataclasses
import dataclasses_json

from . import _property_bag, _multiformat_message_string, _reporting_descriptor, _tool_component_reference, _artifact_location, _translation_metadata


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL, undefined=dataclasses_json.Undefined.EXCLUDE)
@dataclasses.dataclass
class ToolComponent(object):
    """A component, such as a plug-in or the driver, of the analysis tool that was run."""

    name: str = dataclasses.field()
    """The name of the tool component."""
    associated_component: Optional[_tool_component_reference.ToolComponentReference] = dataclasses.field(default=None)
    """The component which is strongly associated with this component. For a translation, this refers to the component which has been translated. For an extension, this is the driver that provides the extension's plugin model."""
    contents: List[Literal['localizedData', 'nonLocalizedData']] = dataclasses.field(default_factory=lambda: ['localizedData', 'nonLocalizedData'])
    """The kinds of data contained in this object."""
    dotted_quad_file_version: Optional[str] = dataclasses.field(default=None)
    """The binary version of the tool component's primary executable file expressed as four non-negative integers separated by a period (for operating systems that express file versions in this way)."""
    download_uri: Optional[str] = dataclasses.field(default=None)
    """The absolute URI from which the tool component can be downloaded."""
    full_description: Optional[_multiformat_message_string.MultiformatMessageString] = dataclasses.field(default=None)
    """A comprehensive description of the tool component."""
    full_name: Optional[str] = dataclasses.field(default=None)
    """The name of the tool component along with its version and any other useful identifying information, such as its locale."""
    global_message_strings: Any = dataclasses.field(default=None)
    """A dictionary, each of whose keys is a resource identifier and each of whose values is a multiformatMessageString object, which holds message strings in plain text and (optionally) Markdown format. The strings can include placeholders, which can be used to construct a message in combination with an arbitrary number of additional string arguments."""
    guid: Optional[str] = dataclasses.field(default=None)
    """A unique identifer for the tool component in the form of a GUID."""
    information_uri: Optional[str] = dataclasses.field(default=None)
    """The absolute URI at which information about this version of the tool component can be found."""
    is_comprehensive: Optional[bool] = dataclasses.field(default=None)
    """Specifies whether this object contains a complete definition of the localizable and/or non-localizable data for this component, as opposed to including only data that is relevant to the results persisted to this log file."""
    language: str = dataclasses.field(default="en-US")
    """The language of the messages emitted into the log file during this run (expressed as an ISO 639-1 two-letter lowercase language code) and an optional region (expressed as an ISO 3166-1 two-letter uppercase subculture code associated with a country or region). The casing is recommended but not required (in order for this data to conform to RFC5646)."""
    localized_data_semantic_version: Optional[str] = dataclasses.field(default=None)
    """The semantic version of the localized strings defined in this component; maintained by components that provide translations."""
    locations: Optional[List[_artifact_location.ArtifactLocation]] = dataclasses.field(default=None)
    """An array of the artifactLocation objects associated with the tool component."""
    minimum_required_localized_data_semantic_version: Optional[str] = dataclasses.field(default=None)
    """The minimum value of localizedDataSemanticVersion required in translations consumed by this component; used by components that consume translations."""
    notifications: Optional[List[_reporting_descriptor.ReportingDescriptor]] = dataclasses.field(default=None)
    """An array of reportingDescriptor objects relevant to the notifications related to the configuration and runtime execution of the tool component."""
    organization: Optional[str] = dataclasses.field(default=None)
    """The organization or company that produced the tool component."""
    product: Optional[str] = dataclasses.field(default=None)
    """A product suite to which the tool component belongs."""
    product_suite: Optional[str] = dataclasses.field(default=None)
    """A localizable string containing the name of the suite of products to which the tool component belongs."""
    properties: Optional[_property_bag.PropertyBag] = dataclasses.field(default=None)
    """Key/value pairs that provide additional information about the tool component."""
    release_date_utc: Optional[str] = dataclasses.field(default=None)
    """A string specifying the UTC date (and optionally, the time) of the component's release."""
    rules: Optional[List[_reporting_descriptor.ReportingDescriptor]] = dataclasses.field(default=None)
    """An array of reportingDescriptor objects relevant to the analysis performed by the tool component."""
    semantic_version: Optional[str] = dataclasses.field(default=None)
    """The tool component version in the format specified by Semantic Versioning 2.0."""
    short_description: Optional[_multiformat_message_string.MultiformatMessageString] = dataclasses.field(default=None)
    """A brief description of the tool component."""
    supported_taxonomies: Optional[List[_tool_component_reference.ToolComponentReference]] = dataclasses.field(default=None)
    """An array of toolComponentReference objects to declare the taxonomies supported by the tool component."""
    taxa: Optional[List[_reporting_descriptor.ReportingDescriptor]] = dataclasses.field(default=None)
    """An array of reportingDescriptor objects relevant to the definitions of both standalone and tool-defined taxonomies."""
    translation_metadata: Optional[_translation_metadata.TranslationMetadata] = dataclasses.field(default=None)
    """Translation metadata, required for a translation, not populated by other component types."""
    version: Optional[str] = dataclasses.field(default=None)
    """The tool component version, in whatever format the component natively provides."""
