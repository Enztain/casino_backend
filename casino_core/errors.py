class DomainError(Exception):
    """Base class for all domain-level errors."""
    pass


class InvalidOutcomeError(DomainError):
    """Raised when roulette outcome value is invalid."""
    pass
