import pytest
import pythings

def test_thingy():
  message = "Hello"
  result = pythings.thingy(message)
  assert message in result
