from fastapi_users.authentication import AuthenticationBackend, BearerTransport

from api.dependencies.strategy import get_database_strategy

bearer_transport = BearerTransport("auth/jwt/login")

authentication_backend = AuthenticationBackend(
    name="access-tokens-db",
    transport=bearer_transport,
    get_strategy=get_database_strategy,
)
