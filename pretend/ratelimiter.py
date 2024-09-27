import asyncio

class RateLimiter:
    def __init__(self, rate_limit: int, period: float):
        """
        Initializes the rate limiter.

        :param rate_limit: Maximum number of requests allowed in a given period.
        :param period: Time period in seconds in which the rate limit is enforced.
        """
        self.rate_limit = rate_limit
        self.period = period
        self.semaphore = asyncio.Semaphore(rate_limit)
        self.lock = asyncio.Lock()
        self.requests_made = 0
        self.start_time = asyncio.get_event_loop().time()

    async def acquire(self):
        """
        Acquires permission to make a request, enforcing the rate limit.
        """
        async with self.lock:
            current_time = asyncio.get_event_loop().time()
            elapsed_time = current_time - self.start_time

            
            if elapsed_time > self.period:
                self.requests_made = 0
                self.start_time = current_time

            
            if self.requests_made >= self.rate_limit:
                wait_time = self.period - elapsed_time
                await asyncio.sleep(wait_time)
                self.requests_made = 0
                self.start_time = asyncio.get_event_loop().time()

            
            self.requests_made += 1
            await self.semaphore.acquire()

    async def release(self):
        """
        Releases the semaphore after the request is made.
        """
        self.semaphore.release()
