import aiohttp
import asyncio
from .exceptions import PretendNeededValue, PretendUnexpectedException, PretendValueError
from .ratelimiter import RateLimiter

class DataObject:
    def __init__(self, **entries):
        self.__dict__.update(entries)

class PretendAPI:
    def __init__(self, api_key: str):
        """
        Initializes the asynchronous API wrapper with the provided API key and rate limiter.

        :param api_key: Your API key as a string
        :param rate_limit: Maximum number of requests allowed in a given period
        :param period: Time period in seconds for the rate limit
        """
        self.api_key = api_key
        self.base_url = "https://api.pretend.rip/en/"
        self.headers = {
            'Authorization': self.api_key
        }
        self.rate_limiter = RateLimiter(rate_limit=5, period=5)

    async def _request(self, url: str):
        """
        Sends an asynchronous GET request to the specified URL with rate limiting.

        :param url: The URL to send the request to
        :return: Parsed response as a DataObject
        :raises: Exception if the response status is not 200
        """
        await self.rate_limiter.acquire()

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, headers=self.headers) as response:
                    if response.status != 200:
                        text = await response.text()
                        raise Exception(f"Failed to fetch data: {response.status}, {text}")
                    json_response = await response.json()
                    return DataObject(**json_response)
        finally:
            await self.rate_limiter.release()

    async def get_userinfo(self, user_id: int = None):
        """
        Get userinfo about a Discord user.

        :param user_id: The user id of the user as an integer
        :raises PretendNeededValue: If user_id is not provided
        :return: Parsed response as a DataObject containing user info
        """
        if user_id is None:
            raise PretendNeededValue("User ID is required to fetch user information.")
        
        if not isinstance(user_id, int):
            raise PretendValueError("bro wtf you doing the user_id needs to be a number")
        
        endpoint = f"userinfo/{user_id}"
        url = f"{self.base_url}{endpoint}"
        return await self._request(url)

    async def get_tiktok_user(self, username: str = None):
        """
        Get information about a TikTok user.

        :param username: The TikTok username as a string
        :raises PretendNeededValue: If username is not provided
        :return: Parsed response as a DataObject containing TikTok user info
        """
        if username is None:
            raise PretendNeededValue("TikTok username is required to fetch user information.")
        
        if not isinstance(username, str):
            raise PretendValueError("bro wtf you doing the username needs to be a string")
        
        endpoint = f"tiktok/{username}"
        url = f"{self.base_url}{endpoint}"
        return await self._request(url)

    async def get_instagram_user(self, username: str = None):
        """
        Get information about an Instagram user.

        :param username: The Instagram username as a string
        :raises PretendNeededValue: If username is not provided
        :return: Parsed response as a DataObject containing Instagram user info
        """
        if username is None:
            raise PretendNeededValue("Instagram username is required to fetch user information.")
        
        if not isinstance(username, str):
            raise PretendValueError("bro wtf you doing the username needs to be a string")
        
        endpoint = f"instagram/{username}"
        url = f"{self.base_url}{endpoint}"
        return await self._request(url)

    async def get_twitter_user(self, username: str = None):
        """
        Get information about a Twitter user.

        :param username: Twitter username as a string
        :raises PretendNeededValue: If username is not provided
        :return: Parsed response as a DataObject containing Twitter user info
        """
        if username is None:
            raise PretendNeededValue("Twitter username is required to fetch user information.")
        
        if not isinstance(username, str):
            raise PretendValueError("bro wtf you doing the username needs to be a string")
        
        endpoint = f"twitter/{username}"
        url = f"{self.base_url}{endpoint}"
        return await self._request(url)

    async def get_roblox_user(self, username: str = None):
        """
        Get information about a Roblox user.

        :param username: Roblox username as a string
        :raises PretendNeededValue: If username is not provided
        :return: Parsed response as a DataObject containing Roblox user info
        """
        if username is None:
            raise PretendNeededValue("Roblox username is required to fetch user information.")
        
        if not isinstance(username, str):
            raise PretendValueError("bro wtf you doing the username needs to be a string")
        
        endpoint = f"roblox/{username}"
        url = f"{self.base_url}{endpoint}"
        return await self._request(url)

    async def get_signed_biolink(self, username: str = None):
        """
        Get information about a signed.bio user.

        :param username: signed.bio username as a string
        :raises PretendNeededValue: If username is not provided
        :return: Parsed response as a DataObject containing signed.bio user info
        """
        if username is None:
            raise PretendNeededValue("signed.bio username is required to fetch user information.")
        
        if not isinstance(username, str):
            raise PretendValueError("bro wtf you doing the username needs to be a string")
        
        endpoint = f"signed/{username}"
        url = f"{self.base_url}{endpoint}"
        return await self._request(url)
