from __future__ import annotations
from typing import Any, Literal, List, Optional

import dataclasses
import dataclasses_json

from . import _message, _stack, _suppression, _graph, _fix, _artifact_location, _property_bag, _reporting_descriptor_reference, _graph_traversal, _web_request, _web_response, _result_provenance, _location, _code_flow, _attachment


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL, undefined=dataclasses_json.Undefined.EXCLUDE)
@dataclasses.dataclass
class Result(object):
    """A result produced by an analysis tool."""

    message: _message.Message = dataclasses.field()
    """A message that describes the result. The first sentence of the message only will be displayed when visible space is limited."""
    analysis_target: Optional[_artifact_location.ArtifactLocation] = dataclasses.field(default=None)
    """Identifies the artifact that the analysis tool was instructed to scan. This need not be the same as the artifact where the result actually occurred."""
    attachments: Optional[List[_attachment.Attachment]] = dataclasses.field(default=None)
    """A set of artifacts relevant to the result."""
    baseline_state: Optional[Literal['new', 'unchanged', 'updated', 'absent']] = dataclasses.field(default=None)
    """The state of a result relative to a baseline of a previous run."""
    code_flows: Optional[List[_code_flow.CodeFlow]] = dataclasses.field(default=None)
    """An array of 'codeFlow' objects relevant to the result."""
    correlation_guid: Optional[str] = dataclasses.field(default=None)
    """A stable, unique identifier for the equivalence class of logically identical results to which this result belongs, in the form of a GUID."""
    fingerprints: Any = dataclasses.field(default=None)
    """A set of strings each of which individually defines a stable, unique identity for the result."""
    fixes: Optional[List[_fix.Fix]] = dataclasses.field(default=None)
    """An array of 'fix' objects, each of which represents a proposed fix to the problem indicated by the result."""
    graph_traversals: Optional[List[_graph_traversal.GraphTraversal]] = dataclasses.field(default=None)
    """An array of one or more unique 'graphTraversal' objects."""
    graphs: Optional[List[_graph.Graph]] = dataclasses.field(default=None)
    """An array of zero or more unique graph objects associated with the result."""
    guid: Optional[str] = dataclasses.field(default=None)
    """A stable, unique identifer for the result in the form of a GUID."""
    hosted_viewer_uri: Optional[str] = dataclasses.field(default=None)
    """An absolute URI at which the result can be viewed."""
    kind: Literal['notApplicable', 'pass', 'fail', 'review', 'open', 'informational'] = dataclasses.field(default="fail")
    """A value that categorizes results by evaluation state."""
    level: Literal['none', 'note', 'warning', 'error'] = dataclasses.field(default="warning")
    """A value specifying the severity level of the result."""
    locations: Optional[List[_location.Location]] = dataclasses.field(default=None)
    """The set of locations where the result was detected. Specify only one location unless the problem indicated by the result can only be corrected by making a change at every specified location."""
    occurrence_count: Optional[int] = dataclasses.field(default=None)
    """A positive integer specifying the number of times this logically unique result was observed in this run."""
    partial_fingerprints: Any = dataclasses.field(default=None)
    """A set of strings that contribute to the stable, unique identity of the result."""
    properties: Optional[_property_bag.PropertyBag] = dataclasses.field(default=None)
    """Key/value pairs that provide additional information about the result."""
    provenance: Optional[_result_provenance.ResultProvenance] = dataclasses.field(default=None)
    """Information about how and when the result was detected."""
    rank: float = dataclasses.field(default=-1.0)
    """A number representing the priority or importance of the result."""
    related_locations: Optional[List[_location.Location]] = dataclasses.field(default=None)
    """A set of locations relevant to this result."""
    rule: Optional[_reporting_descriptor_reference.ReportingDescriptorReference] = dataclasses.field(default=None)
    """A reference used to locate the rule descriptor relevant to this result."""
    rule_id: Optional[str] = dataclasses.field(default=None)
    """The stable, unique identifier of the rule, if any, to which this notification is relevant. This member can be used to retrieve rule metadata from the rules dictionary, if it exists."""
    rule_index: int = dataclasses.field(default=-1)
    """The index within the tool component rules array of the rule object associated with this result."""
    stacks: Optional[List[_stack.Stack]] = dataclasses.field(default=None)
    """An array of 'stack' objects relevant to the result."""
    suppressions: Optional[List[_suppression.Suppression]] = dataclasses.field(default=None)
    """A set of suppressions relevant to this result."""
    taxa: Optional[List[_reporting_descriptor_reference.ReportingDescriptorReference]] = dataclasses.field(default=None)
    """An array of references to taxonomy reporting descriptors that are applicable to the result."""
    web_request: Optional[_web_request.WebRequest] = dataclasses.field(default=None)
    """A web request associated with this result."""
    web_response: Optional[_web_response.WebResponse] = dataclasses.field(default=None)
    """A web response associated with this result."""
    work_item_uris: Optional[List[str]] = dataclasses.field(default=None)
    """The URIs of the work items associated with this result."""
