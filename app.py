from fastapi import FastAPI
from core.database import Base, engine
from fastapi.middleware.cors import CORSMiddleware
from routes.category import categoryrouter
from routes.user import user_router
from routes.auth import authrouter
from routes.product import productrouter
from routes.order import orderrrouter
from routes.cart import cartrouter
from routes.review import reviewrouter
from routes.slider import sliderrouter
from routes.rajaongkir import rajaongkir_router
from routes.midtrans import midtransrouter
from core.database import Base, engine
from core.cloudinary import my_cloudinary




app = FastAPI()
my_cloudinary


Base.metadata.create_all(bind=engine)



origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(categoryrouter, prefix="/api")
app.include_router(user_router, prefix="/api")
app.include_router(authrouter, prefix="/api")
app.include_router(productrouter, prefix="/api")
app.include_router(cartrouter, prefix="/api")
app.include_router(orderrrouter, prefix="/api")
app.include_router(sliderrouter, prefix="/api")
app.include_router(rajaongkir_router, prefix="/api")
app.include_router(midtransrouter, prefix="/api")
app.include_router(reviewrouter, prefix="/api")



@app.get("/")
async def root():
    return {"message": "Hello World"}


