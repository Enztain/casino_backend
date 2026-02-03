import pytest
from casino_core.bets.bet import Bet
from casino_core.errors import InvalidBetError
from casino_core.outcome import Outcome
from casino_core.bets.bet_type import Bet_Type

bet = Outcome(31)
bet_type = Bet_Type(1)

def test_accepts_positive_bet():
    assert Bet(bet, bet_type, 1)._stake == 1


def test_accepts_0():
    with pytest.raises(InvalidBetError):
        Bet(bet, bet_type, 0)

def test_accepts_negative_bet():
    with pytest.raises(InvalidBetError):
        Bet(bet, bet_type, -1)

