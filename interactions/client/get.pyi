from typing import overload, Type, TypeVar, List, Iterable, Optional, Callable, Awaitable

from interactions.client.bot import Client

from interactions.api.models.channel import Channel
from interactions.api.models.guild import Guild
from interactions.api.models.member import Member
from interactions.api.models.message import Message, Emoji, Sticker
from interactions.api.models.role import Role
from interactions.api.models.user import User
from interactions.api.models.webhook import Webhook

_T = TypeVar("_T")

# not API-object related
@overload
def get(
    item: Iterable, *, id: Optional[int] = None, name: Optional[str] = None, check: Callable[..., bool]
) -> _T: ...

# API-object related

#with http force 
# single objects
@overload
def get(client: Client, obj: Type[Channel], *, channel_id: int, force_http: Optional[bool]) -> Awaitable[Channel]: ...
@overload
def get(
    client: Client, obj: Type[Emoji], *, guild_id: int, emoji_id: int, force_http: Optional[bool]
) -> Awaitable[Emoji]: ...
@overload
def get(client: Client, obj: Type[Guild], *, guild_id: int, force_http: Optional[bool]) -> Awaitable[Guild]: ...
@overload
def get(
    client: Client, obj: Type[Member], *, guild_id: int, member_id: int, force_http: Optional[bool]
) -> Awaitable[Member]: ...
@overload
def get(
    client: Client,
    obj: Type[Message],
    *,
    channel_id: int,
    message_id: int,
    force_http: Optional[bool], 
) -> Awaitable[Message]: ...
@overload
def get(client: Client, obj: Type[Role], *, guild_id: int, role_id: int, force_http: Optional[bool]) -> Awaitable[Role]: ...
@overload
def get(client: Client, obj: Type[Sticker], *, sticker_id: int, force_http: Optional[bool]) -> Awaitable[Sticker]: ...
@overload
def get(client: Client, obj: Type[User], *, user_id: int, force_http: Optional[bool]) -> Awaitable[User]: ...
@overload
def get(client: Client, obj: Type[Webhook], *, webhook_id: int, force_http: Optional[bool]) -> Awaitable[Webhook]: ...

# list of objects
@overload
def get(client: Client, obj: Type[List[Channel]], *, channel_ids: List[int], force_http: Optional[bool]) -> Awaitable[List[Channel]]: ...
@overload
def get(client: Client, obj: Type[List[Emoji]], *, guild_id: int, emoji_ids: List[int], force_http: Optional[bool]) -> Awaitable[List[Emoji]]: ...
@overload
def get(client: Client, obj: Type[List[Guild]], *, guild_ids: List[int], force_http: Optional[bool]) -> Awaitable[List[Guild]]: ...
@overload
def get(
    client: Client,
    obj: Type[List[Member]],
    *,
    guild_id: int,
    member_ids: List[int], 
    force_http: Optional[bool]
) -> Awaitable[List[Member]]: ...
@overload
def get(
    client: Client,
    obj: Type[List[Message]],
    *,
    channel_id: int,
    message_ids: List[int],
    force_http: Optional[bool]
) -> Awaitable[List[Message]]: ...
@overload
def get(client: Client, obj: Type[List[Role]], *, guild_id: int, role_ids: List[int], force_http: Optional[bool]) -> Awaitable[List[Role]]: ...
@overload
def get(client: Client, obj: Type[List[Sticker]], *, sticker_ids: List[int], force_http: Optional[bool]) -> Awaitable[List[Sticker]]: ...
@overload
def get(client: Client, obj: Type[List[User]], *, user_ids: List[int], force_http: Optional[bool]) -> Awaitable[List[User]]: ...
@overload
def get(client: Client, obj: Type[List[Webhook]], *, webhook_ids: List[int], force_http: Optional[bool]) -> Awaitable[List[Webhook]]: ...

# with cache force
@overload
def get(client: Client, obj: Type[Channel], *, channel_id: int, force_cache: Optional[bool] = True) -> Channel: ...
@overload
def get(
    client: Client, obj: Type[Emoji], *, guild_id: int, emoji_id: int, force_cache: Optional[bool] = True
) -> Awaitable[Emoji]: ...
@overload
def get(client: Client, obj: Type[Guild], *, guild_id: int, force_cache: Optional[bool] = True) -> Guild: ...
@overload
def get(
    client: Client, obj: Type[Member], *, guild_id: int, member_id: int, force_cache: Optional[bool] = True
) -> Member: ...
@overload
def get(
    client: Client,
    obj: Type[Message],
    *,
    channel_id: int,
    message_id: int,
    force_cache: Optional[bool] = True, 
) -> Message: ...
@overload
def get(client: Client, obj: Type[Role], *, guild_id: int, role_id: int, force_cache: Optional[bool] = True) -> Role: ...
@overload
def get(client: Client, obj: Type[Sticker], *, sticker_id: int, force_cache: Optional[bool] = True) -> Sticker: ...
@overload
def get(client: Client, obj: Type[User], *, user_id: int, force_cache: Optional[bool] = True) -> User: ...
@overload
def get(client: Client, obj: Type[Webhook], *, webhook_id: int, force_cache: Optional[bool] = True) -> Webhook: ...

# list of objects
@overload
def get(client: Client, obj: Type[List[Channel]], *, channel_ids: List[int], force_cache: Optional[bool] = True) -> List[Channel]: ...
@overload
def get(client: Client, obj: Type[List[Emoji]], *, guild_id: int, emoji_ids: List[int], force_cache: Optional[bool] = True) -> List[Emoji]: ...
@overload
def get(client: Client, obj: Type[List[Guild]], *, guild_ids: List[int], force_cache: Optional[bool] = True) -> List[Guild]: ...
@overload
def get(
    client: Client,
    obj: Type[List[Member]],
    *,
    guild_id: int,
    member_ids: List[int], 
    force_cache: Optional[bool] = True
) -> List[Member]: ...
@overload
def get(
    client: Client,
    obj: Type[List[Message]],
    *,
    channel_id: int,
    message_ids: List[int],
    force_cache: Optional[bool] = True
) -> List[Message]: ...
@overload
def get(client: Client, obj: Type[List[Role]], *, guild_id: int, role_ids: List[int], force_cache: Optional[bool] = True) -> List[Role]: ...
@overload
def get(client: Client, obj: Type[List[Sticker]], *, sticker_ids: List[int], force_cache: Optional[bool] = True) -> List[Sticker]: ...
@overload
def get(client: Client, obj: Type[List[User]], *, user_ids: List[int], force_cache: Optional[bool] = True) -> List[User]: ...
@overload
def get(client: Client, obj: Type[List[Webhook]], *, webhook_ids: List[int], force_cache: Optional[bool] = True) -> List[Webhook]: ...


# Having a not-overloaded definition stops showing a warning/complaint from the IDE if wrong arguments are put in,
# so we'll leave that out
