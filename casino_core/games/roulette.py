from decimal import Decimal
from casino_core.bets.bet import Bet
from casino_core.bets.bet_types import BetType
from casino_core.outcome import Outcome


def calculate_straight_payout(bet: Bet, outcome: Outcome) -> Decimal:
    if bet.bet_value.value == outcome.value:
        return Decimal(bet.stake) * Decimal(36)
    return Decimal(0)



def calculate_red_black_payout(bet: Bet, outcome: Outcome) -> Decimal:
    if outcome.value == 0:
        return Decimal(0)

    if bet.bet_type == BetType.RED and outcome.value in RED_NUMBERS:
        return bet.stake * Decimal(2)

    if bet.bet_type == BetType.BLACK and outcome.value in BLACK_NUMBERS:
        return bet.stake * Decimal(2)

    return Decimal(0)






RED_NUMBERS = {
    1, 3, 5, 7, 9,
    12, 14, 16, 18,
    19, 21, 23, 25, 27,
    30, 32, 34, 36
}

BLACK_NUMBERS = {
    2, 4, 6, 8, 10,
    11, 13, 15, 17,
    20, 22, 24, 26, 28,
    29, 31, 33, 35
}