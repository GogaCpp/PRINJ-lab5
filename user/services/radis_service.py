import json
from redis.asyncio import Redis
from ..config import settings


class RedisCache:
    def __init__(self):
        self.redis = None

    async def get_redis(self) -> Redis:
        if self.redis is None:
            self.redis = await Redis(
                host=settings.redis_host,
                port=settings.redis_port,
                db=settings.redis_db,
                password=settings.redis_password,
            )
        return self.redis

    async def cache_user(self, user: dict, ttl: int = 86400000):
        redis = await self.get_redis()
        user_id = user.get("id")
        user["id"] = str(user["id"])
        value = json.dumps(user)

        await redis.setex(
            f"cached:user:{user_id}",
            ttl,
            value
        )

    async def get_cached_user(self, user_id: str):
        redis = await self.get_redis()
        key = f"cached:user:{user_id}"
        user = await redis.get(key)
        return json.loads(user) if user else None

    async def remove_user(self, user_id: str):
        redis = await self.get_redis()
        await redis.delete(f"cached:user:{user_id}")

    async def close(self):
        if self.redis and not self.redis.closed:
            await self.redis.close()
