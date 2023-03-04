from __future__ import annotations
from typing import Any, Literal, List, Optional

import dataclasses
import dataclasses_json

from . import _external_property_file_references, _tool_component, _tool, _logical_location, _version_control_details, _artifact, _graph, _invocation, _special_locations, _thread_flow_location, _property_bag, _address, _result, _web_request, _web_response, _conversion, _run_automation_details


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL, undefined=dataclasses_json.Undefined.EXCLUDE)
@dataclasses.dataclass
class Run(object):
    """Describes a single run of an analysis tool, and contains the reported output of that run."""

    tool: _tool.Tool = dataclasses.field()
    """Information about the tool or tool pipeline that generated the results in this run. A run can only contain results produced by a single tool or tool pipeline. A run can aggregate results from multiple log files, as long as context around the tool run (tool command-line arguments and the like) is identical for all aggregated files."""
    addresses: Optional[List[_address.Address]] = dataclasses.field(default=None)
    """Addresses associated with this run instance, if any."""
    artifacts: Optional[List[_artifact.Artifact]] = dataclasses.field(default=None)
    """An array of artifact objects relevant to the run."""
    automation_details: Optional[_run_automation_details.RunAutomationDetails] = dataclasses.field(default=None)
    """Automation details that describe this run."""
    baseline_guid: Optional[str] = dataclasses.field(default=None)
    """The 'guid' property of a previous SARIF 'run' that comprises the baseline that was used to compute result 'baselineState' properties for the run."""
    column_kind: Optional[Literal['utf16CodeUnits', 'unicodeCodePoints']] = dataclasses.field(default=None)
    """Specifies the unit in which the tool measures columns."""
    conversion: Optional[_conversion.Conversion] = dataclasses.field(default=None)
    """A conversion object that describes how a converter transformed an analysis tool's native reporting format into the SARIF format."""
    default_encoding: Optional[str] = dataclasses.field(default=None)
    """Specifies the default encoding for any artifact object that refers to a text file."""
    default_source_language: Optional[str] = dataclasses.field(default=None)
    """Specifies the default source language for any artifact object that refers to a text file that contains source code."""
    external_property_file_references: Optional[_external_property_file_references.ExternalPropertyFileReferences] = dataclasses.field(default=None)
    """References to external property files that should be inlined with the content of a root log file."""
    graphs: Optional[List[_graph.Graph]] = dataclasses.field(default=None)
    """An array of zero or more unique graph objects associated with the run."""
    invocations: Optional[List[_invocation.Invocation]] = dataclasses.field(default=None)
    """Describes the invocation of the analysis tool."""
    language: str = dataclasses.field(default="en-US")
    """The language of the messages emitted into the log file during this run (expressed as an ISO 639-1 two-letter lowercase culture code) and an optional region (expressed as an ISO 3166-1 two-letter uppercase subculture code associated with a country or region). The casing is recommended but not required (in order for this data to conform to RFC5646)."""
    logical_locations: Optional[List[_logical_location.LogicalLocation]] = dataclasses.field(default=None)
    """An array of logical locations such as namespaces, types or functions."""
    newline_sequences: List[str] = dataclasses.field(default_factory=lambda: ['\r\n', '\n'])
    """An ordered list of character sequences that were treated as line breaks when computing region information for the run."""
    original_uri_base_ids: Any = dataclasses.field(default=None)
    """The artifact location specified by each uriBaseId symbol on the machine where the tool originally ran."""
    policies: Optional[List[_tool_component.ToolComponent]] = dataclasses.field(default=None)
    """Contains configurations that may potentially override both reportingDescriptor.defaultConfiguration (the tool's default severities) and invocation.configurationOverrides (severities established at run-time from the command line)."""
    properties: Optional[_property_bag.PropertyBag] = dataclasses.field(default=None)
    """Key/value pairs that provide additional information about the run."""
    redaction_tokens: Optional[List[str]] = dataclasses.field(default=None)
    """An array of strings used to replace sensitive information in a redaction-aware property."""
    results: Optional[List[_result.Result]] = dataclasses.field(default=None)
    """The set of results contained in an SARIF log. The results array can be omitted when a run is solely exporting rules metadata. It must be present (but may be empty) if a log file represents an actual scan."""
    run_aggregates: Optional[List[_run_automation_details.RunAutomationDetails]] = dataclasses.field(default=None)
    """Automation details that describe the aggregate of runs to which this run belongs."""
    special_locations: Optional[_special_locations.SpecialLocations] = dataclasses.field(default=None)
    """A specialLocations object that defines locations of special significance to SARIF consumers."""
    taxonomies: Optional[List[_tool_component.ToolComponent]] = dataclasses.field(default=None)
    """An array of toolComponent objects relevant to a taxonomy in which results are categorized."""
    thread_flow_locations: Optional[List[_thread_flow_location.ThreadFlowLocation]] = dataclasses.field(default=None)
    """An array of threadFlowLocation objects cached at run level."""
    translations: Optional[List[_tool_component.ToolComponent]] = dataclasses.field(default=None)
    """The set of available translations of the localized data provided by the tool."""
    version_control_provenance: Optional[List[_version_control_details.VersionControlDetails]] = dataclasses.field(default=None)
    """Specifies the revision in version control of the artifacts that were scanned."""
    web_requests: Optional[List[_web_request.WebRequest]] = dataclasses.field(default=None)
    """An array of request objects cached at run level."""
    web_responses: Optional[List[_web_response.WebResponse]] = dataclasses.field(default=None)
    """An array of response objects cached at run level."""
