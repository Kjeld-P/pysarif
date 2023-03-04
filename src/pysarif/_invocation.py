from __future__ import annotations
from typing import Any, List, Optional

import dataclasses
import dataclasses_json

from . import _property_bag, _configuration_override, _artifact_location, _notification


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL, undefined=dataclasses_json.Undefined.EXCLUDE)
@dataclasses.dataclass
class Invocation(object):
    """The runtime environment of the analysis tool run."""

    execution_successful: bool = dataclasses.field()
    """Specifies whether the tool's execution completed successfully."""
    account: Optional[str] = dataclasses.field(default=None)
    """The account that ran the analysis tool."""
    arguments: Optional[List[str]] = dataclasses.field(default=None)
    """An array of strings, containing in order the command line arguments passed to the tool from the operating system."""
    command_line: Optional[str] = dataclasses.field(default=None)
    """The command line used to invoke the tool."""
    end_time_utc: Optional[str] = dataclasses.field(default=None)
    """The Coordinated Universal Time (UTC) date and time at which the run ended. See "Date/time properties" in the SARIF spec for the required format."""
    environment_variables: Any = dataclasses.field(default=None)
    """The environment variables associated with the analysis tool process, expressed as key/value pairs."""
    executable_location: Optional[_artifact_location.ArtifactLocation] = dataclasses.field(default=None)
    """An absolute URI specifying the location of the analysis tool's executable."""
    exit_code: Optional[int] = dataclasses.field(default=None)
    """The process exit code."""
    exit_code_description: Optional[str] = dataclasses.field(default=None)
    """The reason for the process exit."""
    exit_signal_name: Optional[str] = dataclasses.field(default=None)
    """The name of the signal that caused the process to exit."""
    exit_signal_number: Optional[int] = dataclasses.field(default=None)
    """The numeric value of the signal that caused the process to exit."""
    machine: Optional[str] = dataclasses.field(default=None)
    """The machine that hosted the analysis tool run."""
    notification_configuration_overrides: Optional[List[_configuration_override.ConfigurationOverride]] = dataclasses.field(default=None)
    """An array of configurationOverride objects that describe notifications related runtime overrides."""
    process_id: Optional[int] = dataclasses.field(default=None)
    """The process id for the analysis tool run."""
    process_start_failure_message: Optional[str] = dataclasses.field(default=None)
    """The reason given by the operating system that the process failed to start."""
    properties: Optional[_property_bag.PropertyBag] = dataclasses.field(default=None)
    """Key/value pairs that provide additional information about the invocation."""
    response_files: Optional[List[_artifact_location.ArtifactLocation]] = dataclasses.field(default=None)
    """The locations of any response files specified on the tool's command line."""
    rule_configuration_overrides: Optional[List[_configuration_override.ConfigurationOverride]] = dataclasses.field(default=None)
    """An array of configurationOverride objects that describe rules related runtime overrides."""
    start_time_utc: Optional[str] = dataclasses.field(default=None)
    """The Coordinated Universal Time (UTC) date and time at which the run started. See "Date/time properties" in the SARIF spec for the required format."""
    stderr: Optional[_artifact_location.ArtifactLocation] = dataclasses.field(default=None)
    """A file containing the standard error stream from the process that was invoked."""
    stdin: Optional[_artifact_location.ArtifactLocation] = dataclasses.field(default=None)
    """A file containing the standard input stream to the process that was invoked."""
    stdout: Optional[_artifact_location.ArtifactLocation] = dataclasses.field(default=None)
    """A file containing the standard output stream from the process that was invoked."""
    stdout_stderr: Optional[_artifact_location.ArtifactLocation] = dataclasses.field(default=None)
    """A file containing the interleaved standard output and standard error stream from the process that was invoked."""
    tool_configuration_notifications: Optional[List[_notification.Notification]] = dataclasses.field(default=None)
    """A list of conditions detected by the tool that are relevant to the tool's configuration."""
    tool_execution_notifications: Optional[List[_notification.Notification]] = dataclasses.field(default=None)
    """A list of runtime conditions detected by the tool during the analysis."""
    working_directory: Optional[_artifact_location.ArtifactLocation] = dataclasses.field(default=None)
    """The working directory for the analysis tool run."""
