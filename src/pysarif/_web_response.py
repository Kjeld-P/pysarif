from __future__ import annotations
from typing import Optional, Any

import dataclasses
import dataclasses_json

from . import _artifact_content, _property_bag


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL, undefined=dataclasses_json.Undefined.EXCLUDE)
@dataclasses.dataclass
class WebResponse(object):
    """A web response object."""

    body: Optional[_artifact_content.ArtifactContent] = dataclasses.field(default=None)
    """The body of the response."""
    headers: Any = dataclasses.field(default=None)
    """The response headers."""
    index: int = dataclasses.field(default=-1)
    """The index within the run.webResponses array of the response object associated with this result."""
    no_response_received: Optional[bool] = dataclasses.field(default=None)
    """Specifies whether a response was received from the server."""
    properties: Optional[_property_bag.PropertyBag] = dataclasses.field(default=None)
    """Key/value pairs that provide additional information about the response."""
    protocol: Optional[str] = dataclasses.field(default=None)
    """The response protocol. Example: 'http'."""
    reason_phrase: Optional[str] = dataclasses.field(default=None)
    """The response reason. Example: 'Not found'."""
    status_code: Optional[int] = dataclasses.field(default=None)
    """The response status code. Example: 451."""
    version: Optional[str] = dataclasses.field(default=None)
    """The response version. Example: '1.1'."""
