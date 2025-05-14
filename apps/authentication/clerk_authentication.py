import requests
import jwt
from jwt import PyJWKClient
from django.contrib.auth import get_user_model
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings

User = get_user_model()

class ClerkJWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer '):
            return None

        token = auth_header.split(' ')[1]
        jwks_url = settings.CLERK_JWKS_URL

        try:
            jwk_client = PyJWKClient(jwks_url)
            signing_key = jwk_client.get_signing_key_from_jwt(token)

            print("Autenticando token JWT...")

            decoded_token = jwt.decode(
                token,
                signing_key.key,
                algorithms=["RS256"],  
                audience=settings.CLERK_AUDIENCE,
                issuer=settings.CLERK_ISSUER,
            )

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('El token ha expirado.')
        except jwt.InvalidTokenError as e:
            raise AuthenticationFailed(f'Token inválido: {str(e)}')

        print("Token decodificado:", decoded_token)

        email = decoded_token.get("email")
        if not email:
            raise AuthenticationFailed("Token inválido: falta el email")

        user, _ = User.objects.get_or_create(
            correo_electronico=email,
            defaults={
            }
        )

        return (user, token)
