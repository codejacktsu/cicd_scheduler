import pytest
import logging
from src.app import main


def test_logger(caplog):
    with caplog.at_level(logging.DEBUG):
        main()
        assert "Debug message" in caplog.text
        assert "Info message" in caplog.text
        assert "Warning message" in caplog.text
        assert "Error message" in caplog.text
        assert "Critical message" in caplog.text
        