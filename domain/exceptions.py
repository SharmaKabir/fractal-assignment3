class DuplicateRequestIdError(Exception):
    """Raised when a request ID has already been used."""


class RequestNotFoundError(Exception):
    """Raised when a request ID cannot be found."""


class InvalidPriorityError(Exception):
    """Raised when a priority is not LOW, MEDIUM, or HIGH."""


class RequestAlreadyResolvedError(Exception):
    """Raised when an already resolved request is resolved again."""


class InvalidMenuChoiceError(Exception):
    """Raised when a menu choice is not between 1 and 5."""
