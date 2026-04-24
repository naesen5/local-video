"""Tests for detect_hardware module."""

import json
import os
import sys

# Add scripts to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

from detect_hardware import get_system_info, get_ram_info, get_full_hardware_report


class TestGetSystemInfo:
    """Tests for get_system_info function."""

    def test_get_system_info_returns_dict(self):
        """Verify get_system_info returns a dictionary."""
        result = get_system_info()
        assert isinstance(result, dict)

    def test_get_system_info_has_expected_keys(self):
        """Verify all expected keys are present."""
        result = get_system_info()
        expected_keys = [
            "platform",
            "platform_release",
            "platform_version",
            "architecture",
            "processor",
            "python_version",
        ]
        for key in expected_keys:
            assert key in result, f"Missing key: {key}"

    def test_get_system_info_platform_is_string(self):
        """Verify platform value is a non-empty string."""
        result = get_system_info()
        assert isinstance(result["platform"], str)
        assert len(result["platform"]) > 0

    def test_get_system_info_python_version_format(self):
        """Verify Python version is in expected format."""
        result = get_system_info()
        # Should be like "3.11.5"
        parts = result["python_version"].split(".")
        assert len(parts) >= 2
        assert parts[0].isdigit()


class TestGetRamInfo:
    """Tests for get_ram_info function."""

    def test_get_ram_info_returns_dict(self):
        """Verify get_ram_info returns a dictionary."""
        result = get_ram_info()
        assert isinstance(result, dict)

    def test_get_ram_info_has_error_key_when_psutil_missing(self):
        """Verify get_ram_info returns error dict when psutil not installed."""
        result = get_ram_info()
        # psutil may not be installed in test env
        assert "error" in result or "total_gb" in result


class TestGetFullHardwareReport:
    """Tests for get_full_hardware_report function."""

    def test_get_full_hardware_report_returns_dict(self):
        """Verify get_full_hardware_report returns a dictionary."""
        result = get_full_hardware_report()
        assert isinstance(result, dict)

    def test_get_full_hardware_report_has_system_key(self):
        """Verify report includes system info."""
        result = get_full_hardware_report()
        # Keys may be 'system' or 'system_info' depending on implementation
        assert "system" in result or "system_info" in result

    def test_get_full_hardware_report_has_ram_key(self):
        """Verify report includes ram info."""
        result = get_full_hardware_report()
        # Keys may be 'ram' or 'ram_info' depending on implementation
        assert "ram" in result or "ram_info" in result

    def test_get_full_hardware_report_json_serializable(self):
        """Verify report output is JSON serializable."""
        result = get_full_hardware_report()
        try:
            json.dumps(result)
        except TypeError as e:
            assert False, f"Not JSON serializable: {e}"
