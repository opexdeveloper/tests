"""
Pretend API - An asynchronous wrapper for interacting with the Pretend API.

This package provides an easy-to-use interface for accessing various social media user information
through the Pretend API with rate limiting and dot notation access to JSON responses.
"""

from .pretend import PretendAPI
from .exceptions import PretendNeededValue, PretendUnexpectedException, PretendValueError
from .ratelimiter import RateLimiter

__all__ = ['PretendAPI']
__title__ = "pretendapi"
__author__ = "Claqz"
__license__ = "Apache"
__path__ = __import__('pkgutil').extend_path(__path__, __name__)