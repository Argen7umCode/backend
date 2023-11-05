from fastapi import Depends, HTTPException, status
import jwt

from datetime import timedelta, datetime


class Verificator:
    def __init__(self, expiration_time: timedelta, algorithm: str, secret_key: str) -> None:
        self.expiration_time = expiration_time
        self.algorithm = algorithm
        self.secret_key = secret_key

    def create_jwt(self, data: dict):
        data['exp'] = datetime.utcnow() + self.expiration_time
        return jwt.encode(data, self.secret_key, algorithm=self.algorithm)

    def verify_jwt(self, token: str = Depends(None)):
        from app import oauth2_scheme
        if token is None:
            token = Depends(oauth2_scheme)
        try:
            return jwt.decode(token, self.secret_key, algorithms=[self.algorithm]).get('sub')
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Expired Signature Error")
        except jwt.PyJWKError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Token")
