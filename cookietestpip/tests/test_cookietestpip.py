"""
Unit and regression test for the cookietestpip package.
"""

# Import package, test suite, and other packages as needed
import cookietestpip
import pytest
import sys

def test_cookietestpip_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "cookietestpip" in sys.modules
