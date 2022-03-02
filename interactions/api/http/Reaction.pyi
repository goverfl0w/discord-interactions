from typing import List

from ...api.cache import Cache
from .Request import Request


class HTTPReaction:

    _req: Request
    cache: Cache

    def __init__(self, _req, cache) -> None: ...
    async def create_reaction(self, channel_id: int, message_id: int, emoji: str) -> None: ...
    async def remove_self_reaction(self, channel_id: int, message_id: int, emoji: str) -> None: ...
    async def remove_user_reaction(
        self, channel_id: int, message_id: int, emoji: str, user_id: int
    ) -> None: ...
    async def remove_all_reactions(self, channel_id: int, message_id: int) -> None: ...
    async def remove_all_reactions_of_emoji(
        self, channel_id: int, message_id: int, emoji: str
    ) -> None: ...
    async def get_reactions_of_emoji(
        self, channel_id: int, message_id: int, emoji: str
    ) -> List[dict]: ...
