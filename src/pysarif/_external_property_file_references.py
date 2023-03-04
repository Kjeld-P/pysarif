from __future__ import annotations
from typing import List, Optional

import dataclasses
import dataclasses_json

from . import _property_bag, _external_property_file_reference


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL, undefined=dataclasses_json.Undefined.EXCLUDE)
@dataclasses.dataclass
class ExternalPropertyFileReferences(object):
    """References to external property files that should be inlined with the content of a root log file."""

    addresses: Optional[List[_external_property_file_reference.ExternalPropertyFileReference]] = dataclasses.field(default=None)
    """An array of external property files containing run.addresses arrays to be merged with the root log file."""
    artifacts: Optional[List[_external_property_file_reference.ExternalPropertyFileReference]] = dataclasses.field(default=None)
    """An array of external property files containing run.artifacts arrays to be merged with the root log file."""
    conversion: Optional[_external_property_file_reference.ExternalPropertyFileReference] = dataclasses.field(default=None)
    """An external property file containing a run.conversion object to be merged with the root log file."""
    driver: Optional[_external_property_file_reference.ExternalPropertyFileReference] = dataclasses.field(default=None)
    """An external property file containing a run.driver object to be merged with the root log file."""
    extensions: Optional[List[_external_property_file_reference.ExternalPropertyFileReference]] = dataclasses.field(default=None)
    """An array of external property files containing run.extensions arrays to be merged with the root log file."""
    externalized_properties: Optional[_external_property_file_reference.ExternalPropertyFileReference] = dataclasses.field(default=None)
    """An external property file containing a run.properties object to be merged with the root log file."""
    graphs: Optional[List[_external_property_file_reference.ExternalPropertyFileReference]] = dataclasses.field(default=None)
    """An array of external property files containing a run.graphs object to be merged with the root log file."""
    invocations: Optional[List[_external_property_file_reference.ExternalPropertyFileReference]] = dataclasses.field(default=None)
    """An array of external property files containing run.invocations arrays to be merged with the root log file."""
    logical_locations: Optional[List[_external_property_file_reference.ExternalPropertyFileReference]] = dataclasses.field(default=None)
    """An array of external property files containing run.logicalLocations arrays to be merged with the root log file."""
    policies: Optional[List[_external_property_file_reference.ExternalPropertyFileReference]] = dataclasses.field(default=None)
    """An array of external property files containing run.policies arrays to be merged with the root log file."""
    properties: Optional[_property_bag.PropertyBag] = dataclasses.field(default=None)
    """Key/value pairs that provide additional information about the external property files."""
    results: Optional[List[_external_property_file_reference.ExternalPropertyFileReference]] = dataclasses.field(default=None)
    """An array of external property files containing run.results arrays to be merged with the root log file."""
    taxonomies: Optional[List[_external_property_file_reference.ExternalPropertyFileReference]] = dataclasses.field(default=None)
    """An array of external property files containing run.taxonomies arrays to be merged with the root log file."""
    thread_flow_locations: Optional[List[_external_property_file_reference.ExternalPropertyFileReference]] = dataclasses.field(default=None)
    """An array of external property files containing run.threadFlowLocations arrays to be merged with the root log file."""
    translations: Optional[List[_external_property_file_reference.ExternalPropertyFileReference]] = dataclasses.field(default=None)
    """An array of external property files containing run.translations arrays to be merged with the root log file."""
    web_requests: Optional[List[_external_property_file_reference.ExternalPropertyFileReference]] = dataclasses.field(default=None)
    """An array of external property files containing run.requests arrays to be merged with the root log file."""
    web_responses: Optional[List[_external_property_file_reference.ExternalPropertyFileReference]] = dataclasses.field(default=None)
    """An array of external property files containing run.responses arrays to be merged with the root log file."""
