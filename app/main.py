from fastapi import FastAPI, APIRouter
from app.routers import main_router
from app.schemas.user import BUser
import uvicorn

app = FastAPI()

app.include_router(main_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/users2")
async def get_users(user_data: BUser):
    md = user_data.model_dump()
    users_b = BUser(**md)
    tt = users_b.model_dump()
    to_dict = users_b.model_dump()
    to_json = users_b.model_dump_json()
    print(to_dict)
    print(to_json)
    return {"message": users_b}


# if __name__ == "__main__":
#     uvicorn.run("main:app", reload=True, port=8003)
