import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from fair_sharer import fair_sharer

def test_fair_sharer():
    # Test 1: Single iteration
    values = [0, 1000, 800, 0]
    result = fair_sharer(values, 1)
    assert result == [100, 800, 900, 0], f"Unexpected result: {result}"

    # Test 2: Multiple iterations
    values = [0, 1000, 800, 0]
    result = fair_sharer(values, 2)
    assert result == [100, 890, 720, 90], f"Unexpected result: {result}"

    # Test 3: Edge case with all zeros
    values = [0, 0, 0, 0]
    result = fair_sharer(values, 1)
    assert result == [0, 0, 0, 0], f"Unexpected result: {result}"


