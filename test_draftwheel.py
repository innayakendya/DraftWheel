# test_draftwheel.py
"""
Tests for DraftWheel module.
"""

import unittest
from draftwheel import DraftWheel

class TestDraftWheel(unittest.TestCase):
    """Test cases for DraftWheel class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DraftWheel()
        self.assertIsInstance(instance, DraftWheel)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DraftWheel()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
