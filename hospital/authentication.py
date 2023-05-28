from rest_framework_simplejwt.tokens import RefreshToken

def generate_jwt_token(doctor):
    refresh = RefreshToken.for_user(doctor)
    token = str(refresh.access_token)

    return token
