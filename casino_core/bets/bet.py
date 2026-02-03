from casino_core.errors import InvalidBetError
from casino_core.outcome import Outcome
from casino_core.bets.bet_type import Bet_Type


class Bet:
    def __init__(self, bet_value: Outcome, bet_type: Bet_Type, stake: int):
        # type check (bool is subclass of int!)
        if not isinstance(stake, int) or isinstance(stake, bool):
            raise InvalidBetError("Bet must be an integer")
        if stake <= 0:
            raise InvalidBetError("Stake must be positive")
        if not isinstance(bet_type, Bet_Type):
            raise InvalidBetError("Bet type must be an instance of BetType")
        if not isinstance(bet_value, Outcome):
            raise InvalidBetError("Bet value must be an instance of Outcome")

        self._stake = stake

