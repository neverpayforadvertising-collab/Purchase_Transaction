class DomainError(Exception):
    pass


class NotFoundError(DomainError):
    pass


class ConversionError(DomainError):
    pass


class ExternalAPIError(DomainError):
    pass