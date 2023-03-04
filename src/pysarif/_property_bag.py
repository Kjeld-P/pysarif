from __future__ import annotations
from typing import List, Optional

import dataclasses
import dataclasses_json


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL, undefined=dataclasses_json.Undefined.EXCLUDE)
@dataclasses.dataclass
class PropertyBag(object):
    """Key/value pairs that provide additional information about the object."""

    tags: Optional[List[str]] = dataclasses.field(default=None)
    """A set of distinct strings that provide additional information."""
