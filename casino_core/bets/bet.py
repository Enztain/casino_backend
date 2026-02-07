from casino_core.errors import InvalidBetError
from casino_core.outcome import Outcome
from casino_core.bets.bet_types import BetType



class Bet:
    def __init__(self, bet_value: Outcome, bet_type: BetType, stake: int):
        if not isinstance(stake, int) or isinstance(stake, bool):
            raise InvalidBetError("Bet must be an integer")
        if stake <= 0:
            raise InvalidBetError("Stake must be positive")
        if not isinstance(bet_type, BetType):
            raise InvalidBetError("Bet type must be an instance of BetType")
        if not isinstance(bet_value, Outcome):
            raise InvalidBetError("Bet value must be an instance of Outcome")

        self._stake = stake
        self._bet_type = bet_type
        self._bet_value = bet_value

    @property
    def stake(self) -> int:
        return self._stake

    @property
    def bet_type(self) -> BetType:
        return self._bet_type

    @property
    def bet_value(self) -> Outcome:
        return self._bet_value
