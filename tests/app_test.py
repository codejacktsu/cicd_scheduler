import pytest
import logging
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from src.app import main

def test_logger(caplog):
    with caplog.at_level(logging.DEBUG):
        main()
        assert "debug message" in caplog.text
        assert "info message" in caplog.text
        assert "warning message" in caplog.text
        assert "error message" in caplog.text
        assert "critical message" in caplog.text
        