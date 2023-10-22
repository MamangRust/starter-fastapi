from fastapi import FastAPI
from core.database import Base, engine
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()


Base.metadata.create_all(bind=engine)



origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


