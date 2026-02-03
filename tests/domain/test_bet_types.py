from casino_core.bets.bet_types import BetType


def test_bet_type_is_enum():
    assert isinstance(BetType.RED, BetType)
    assert isinstance(BetType.BLACK, BetType)
    assert isinstance(BetType.STRAIGHT, BetType)


def test_bet_type_values_are_strings():
    assert BetType.RED.value == "red"
    assert BetType.BLACK.value == "black"
    assert BetType.STRAIGHT.value == "straight"


def test_bet_type_names():
    assert BetType.RED.name == "RED"
    assert BetType.BLACK.name == "BLACK"
    assert BetType.STRAIGHT.name == "STRAIGHT"
