from fastapi_users.authentication import AuthenticationBackend, BearerTransport

from api.dependencies.strategy import get_database_strategy
from core.config import settings

bearer_transport = BearerTransport(settings.api.bearer_token_url)

authentication_backend = AuthenticationBackend(
    name="access-tokens-db",
    transport=bearer_transport,
    get_strategy=get_database_strategy,
)
