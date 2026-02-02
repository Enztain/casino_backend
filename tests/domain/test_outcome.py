import pytest
from casino_core.outcome import Outcome
from casino_core.errors import InvalidOutcomeError


def test_accepts_zero():
    assert Outcome(0).value == 0

def test_accepts_36():
    assert Outcome(36).value == 36

def test_rejects_below_range():
    with pytest.raises(InvalidOutcomeError):
        Outcome(-1)

def test_rejects_above_range():
    with pytest.raises(InvalidOutcomeError):
        Outcome(37)

def test_rejects_non_integer():
    with pytest.raises(InvalidOutcomeError):
        Outcome("7")

def test_rejects_bool():
    with pytest.raises(InvalidOutcomeError):
        Outcome(True)
