from decimal import Decimal

from casino_core.bets.bet import Bet
from casino_core.bets.bet_types import BetType
from casino_core.outcome import Outcome
from casino_core.games.roulette import (
    calculate_straight_payout,
    calculate_red_black_payout,
)


# ---------- STRAIGHT BET TESTS ----------

def test_straight_win():
    bet = Bet(
        bet_value=Outcome(7),
        bet_type=BetType.STRAIGHT,
        stake=10,
    )
    outcome = Outcome(7)

    payout = calculate_straight_payout(bet, outcome)

    assert payout == Decimal(360)


def test_straight_loss():
    bet = Bet(
        bet_value=Outcome(7),
        bet_type=BetType.STRAIGHT,
        stake=10,
    )
    outcome = Outcome(8)

    payout = calculate_straight_payout(bet, outcome)

    assert payout == Decimal(0)


def test_straight_zero_win():
    bet = Bet(
        bet_value=Outcome(0),
        bet_type=BetType.STRAIGHT,
        stake=5,
    )
    outcome = Outcome(0)

    payout = calculate_straight_payout(bet, outcome)

    assert payout == Decimal(180)


# ---------- RED / BLACK BET TESTS ----------

def test_red_win():
    bet = Bet(
        bet_value=Outcome(0),
        bet_type=BetType.RED,
        stake=10,
    )
    outcome = Outcome(3)  # red

    payout = calculate_red_black_payout(bet, outcome)

    assert payout == Decimal(20)


def test_black_win():
    bet = Bet(
        bet_value=Outcome(0),
        bet_type=BetType.BLACK,
        stake=10,
    )
    outcome = Outcome(8)  # black

    payout = calculate_red_black_payout(bet, outcome)

    assert payout == Decimal(20)


def test_red_loss_on_black():
    bet = Bet(
        bet_value=Outcome(0),
        bet_type=BetType.RED,
        stake=10,
    )
    outcome = Outcome(8)  # black

    payout = calculate_red_black_payout(bet, outcome)

    assert payout == Decimal(0)


def test_black_loss_on_red():
    bet = Bet(
        bet_value=Outcome(0),
        bet_type=BetType.BLACK,
        stake=10,
    )
    outcome = Outcome(3)  # red

    payout = calculate_red_black_payout(bet, outcome)

    assert payout == Decimal(0)


def test_red_black_zero_always_loses():
    bet_red = Bet(
        bet_value=Outcome(0),
        bet_type=BetType.RED,
        stake=10,
    )
    bet_black = Bet(
        bet_value=Outcome(0),
        bet_type=BetType.BLACK,
        stake=10,
    )
    outcome = Outcome(0)

    assert calculate_red_black_payout(bet_red, outcome) == Decimal(0)
    assert calculate_red_black_payout(bet_black, outcome) == Decimal(0)
