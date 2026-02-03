class DomainError(Exception):
    """Base class for all domain-level errors."""
    pass


class InvalidOutcomeError(DomainError):
    """Raised when roulette outcome value is invalid."""
    pass

class InvalidBetError(DomainError):
    """Raised when roulette bet value is invalid."""
    pass