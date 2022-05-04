from typing import Union, Optional

from django.conf import settings
import redis


class RedisService:
    """
    Abstraction layer over Redis to reduce boilerplate in other services
    """

    _instance: redis.StrictRedis

    def __init__(self, *, db: int):
        self._instance = redis.StrictRedis(
            host=settings.REDIS_HOSTNAME,
            port=settings.REDIS_PORT,
            db=db,
            decode_responses=True,
        )

    def store(
        self,
        *,
        key: str,
        value: Union[bytes, str, int, float],
        expiration_seconds: Optional[int] = None
    ):
        return self._instance.set(key, value, ex=expiration_seconds)

    def retrieve(self, *, key: str):
        return self._instance.get(key)

    def delete(self, *, key: str):
        return self._instance.delete(key)
