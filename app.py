import uvicorn
from routers import user_router, login_router, message_router, conversation_router


from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

app = FastAPI()

app.include_router(user_router)
app.include_router(login_router)
app.include_router(message_router)
app.include_router(conversation_router)

@app.get('/')
async def start():
    return {'message' : 'Hello World'}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)