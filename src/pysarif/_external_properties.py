from __future__ import annotations
from typing import Literal, List, Optional

import dataclasses
import dataclasses_json

from . import _tool_component, _logical_location, _artifact, _graph, _invocation, _thread_flow_location, _property_bag, _address, _result, _web_request, _web_response, _conversion


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL, undefined=dataclasses_json.Undefined.EXCLUDE)
@dataclasses.dataclass
class ExternalProperties(object):
    addresses: Optional[List[_address.Address]] = dataclasses.field(default=None)
    """Addresses that will be merged with a separate run."""
    artifacts: Optional[List[_artifact.Artifact]] = dataclasses.field(default=None)
    """An array of artifact objects that will be merged with a separate run."""
    conversion: Optional[_conversion.Conversion] = dataclasses.field(default=None)
    """A conversion object that will be merged with a separate run."""
    driver: Optional[_tool_component.ToolComponent] = dataclasses.field(default=None)
    """The analysis tool object that will be merged with a separate run."""
    extensions: Optional[List[_tool_component.ToolComponent]] = dataclasses.field(default=None)
    """Tool extensions that will be merged with a separate run."""
    externalized_properties: Optional[_property_bag.PropertyBag] = dataclasses.field(default=None)
    """Key/value pairs that provide additional information that will be merged with a separate run."""
    graphs: Optional[List[_graph.Graph]] = dataclasses.field(default=None)
    """An array of graph objects that will be merged with a separate run."""
    guid: Optional[str] = dataclasses.field(default=None)
    """A stable, unique identifer for this external properties object, in the form of a GUID."""
    invocations: Optional[List[_invocation.Invocation]] = dataclasses.field(default=None)
    """Describes the invocation of the analysis tool that will be merged with a separate run."""
    logical_locations: Optional[List[_logical_location.LogicalLocation]] = dataclasses.field(default=None)
    """An array of logical locations such as namespaces, types or functions that will be merged with a separate run."""
    policies: Optional[List[_tool_component.ToolComponent]] = dataclasses.field(default=None)
    """Tool policies that will be merged with a separate run."""
    properties: Optional[_property_bag.PropertyBag] = dataclasses.field(default=None)
    """Key/value pairs that provide additional information about the external properties."""
    results: Optional[List[_result.Result]] = dataclasses.field(default=None)
    """An array of result objects that will be merged with a separate run."""
    run_guid: Optional[str] = dataclasses.field(default=None)
    """A stable, unique identifer for the run associated with this external properties object, in the form of a GUID."""
    schema: Optional[str] = dataclasses.field(default=None)
    """The URI of the JSON schema corresponding to the version of the external property file format."""
    taxonomies: Optional[List[_tool_component.ToolComponent]] = dataclasses.field(default=None)
    """Tool taxonomies that will be merged with a separate run."""
    thread_flow_locations: Optional[List[_thread_flow_location.ThreadFlowLocation]] = dataclasses.field(default=None)
    """An array of threadFlowLocation objects that will be merged with a separate run."""
    translations: Optional[List[_tool_component.ToolComponent]] = dataclasses.field(default=None)
    """Tool translations that will be merged with a separate run."""
    version: Optional[Literal['2.1.0']] = dataclasses.field(default=None)
    """The SARIF format version of this external properties object."""
    web_requests: Optional[List[_web_request.WebRequest]] = dataclasses.field(default=None)
    """Requests that will be merged with a separate run."""
    web_responses: Optional[List[_web_response.WebResponse]] = dataclasses.field(default=None)
    """Responses that will be merged with a separate run."""
