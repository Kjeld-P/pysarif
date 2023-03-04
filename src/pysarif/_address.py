from __future__ import annotations
from typing import Optional

import dataclasses
import dataclasses_json

from . import _property_bag


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL, undefined=dataclasses_json.Undefined.EXCLUDE)
@dataclasses.dataclass
class Address(object):
    """A physical or virtual address, or a range of addresses, in an 'addressable region' (memory or a binary file)."""

    absolute_address: int = dataclasses.field(default=-1)
    """The address expressed as a byte offset from the start of the addressable region."""
    fully_qualified_name: Optional[str] = dataclasses.field(default=None)
    """A human-readable fully qualified name that is associated with the address."""
    index: int = dataclasses.field(default=-1)
    """The index within run.addresses of the cached object for this address."""
    kind: Optional[str] = dataclasses.field(default=None)
    """An open-ended string that identifies the address kind. 'data', 'function', 'header','instruction', 'module', 'page', 'section', 'segment', 'stack', 'stackFrame', 'table' are well-known values."""
    length: Optional[int] = dataclasses.field(default=None)
    """The number of bytes in this range of addresses."""
    name: Optional[str] = dataclasses.field(default=None)
    """A name that is associated with the address, e.g., '.text'."""
    offset_from_parent: Optional[int] = dataclasses.field(default=None)
    """The byte offset of this address from the absolute or relative address of the parent object."""
    parent_index: int = dataclasses.field(default=-1)
    """The index within run.addresses of the parent object."""
    properties: Optional[_property_bag.PropertyBag] = dataclasses.field(default=None)
    """Key/value pairs that provide additional information about the address."""
    relative_address: Optional[int] = dataclasses.field(default=None)
    """The address expressed as a byte offset from the absolute address of the top-most parent object."""
