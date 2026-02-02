from casino_core.errors import InvalidOutcomeError


class Outcome:
    def __init__(self, value: int):
        # type check (bool is subclass of int!)
        if not isinstance(value, int) or isinstance(value, bool):
            raise InvalidOutcomeError("Outcome must be an integer")

        # range check
        if value < 0 or value > 36:
            raise InvalidOutcomeError("Outcome must be between 0 and 36")

        self._value = value

    @property
    def value(self) -> int:
        return self._value


