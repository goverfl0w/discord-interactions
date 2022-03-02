from typing import List, Optional

from .Request import Request
from ...api.cache import Cache


class HTTPEmoji:

    _req: Request
    cache: Cache

    def __init__(self, _req, cache) -> None: ...
    async def get_all_emoji(self, guild_id: int) -> List[dict]: ...
    async def get_guild_emoji(self, guild_id: int, emoji_id: int) -> dict: ...
    async def create_guild_emoji(
        self, guild_id: int, payload: dict, reason: Optional[str] = None
    ) -> dict: ...
    async def modify_guild_emoji(
        self, guild_id: int, emoji_id: int, payload: dict, reason: Optional[str] = None
    ) -> dict: ...
    async def delete_guild_emoji(
        self, guild_id: int, emoji_id: int, reason: Optional[str] = None
    ) -> None: ...
