
import json
from pathlib import Path

REPORT = Path("/app/report.json")


def test_report_exists():
    """Success Criterion 4: report.json is created."""
    assert REPORT.exists()


def test_total_requests():
    """Success Criterion 1."""
    data = json.loads(REPORT.read_text())
    assert data["total_requests"] == 6


def test_unique_ips():
    """Success Criterion 2."""
    data = json.loads(REPORT.read_text())
    assert data["unique_ips"] == 3


def test_top_path():
    """Success Criterion 3."""
    data = json.loads(REPORT.read_text())
    assert data["top_path"] == "/index.html"