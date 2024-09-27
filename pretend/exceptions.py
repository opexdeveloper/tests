class PretendRaise(Exception):
    """Base class for custom exceptions"""
    pass

class PretendNeededValue(PretendRaise):
    """Exception raised when a needed value is missing"""
    pass

class PretendValueError(ValueError, PretendRaise):
    """Exception raised for invalid values"""
    pass

class PretendUnexpectedException(Exception):
    pass

