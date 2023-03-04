from __future__ import annotations
from typing import Optional, Any

import dataclasses
import dataclasses_json

from . import _artifact_content, _property_bag


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL, undefined=dataclasses_json.Undefined.EXCLUDE)
@dataclasses.dataclass
class WebRequest(object):
    """A web request object."""

    body: Optional[_artifact_content.ArtifactContent] = dataclasses.field(default=None)
    """The body of the request."""
    headers: Any = dataclasses.field(default=None)
    """The request headers."""
    index: int = dataclasses.field(default=-1)
    """The index within the run.webRequests array of the request object associated with this result."""
    method: Optional[str] = dataclasses.field(default=None)
    """The HTTP method. Well-known values are 'GET', 'PUT', 'POST', 'DELETE', 'PATCH', 'HEAD', 'OPTIONS', 'TRACE', 'CONNECT'."""
    parameters: Any = dataclasses.field(default=None)
    """The request parameters."""
    properties: Optional[_property_bag.PropertyBag] = dataclasses.field(default=None)
    """Key/value pairs that provide additional information about the request."""
    protocol: Optional[str] = dataclasses.field(default=None)
    """The request protocol. Example: 'http'."""
    target: Optional[str] = dataclasses.field(default=None)
    """The target of the request."""
    version: Optional[str] = dataclasses.field(default=None)
    """The request version. Example: '1.1'."""
