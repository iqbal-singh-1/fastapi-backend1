from fastapi import FastAPI
from app.routes import auth, product, bid, order, notification, insurance
import uvicorn
import os

app = FastAPI()

# ✅ Include all routes
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(product.router, prefix="/products", tags=["Products"])
app.include_router(bid.router, prefix="/bids", tags=["Bidding"])
app.include_router(order.router, prefix="/orders", tags=["Orders"])
app.include_router(notification.router,
                   prefix="/notifications", tags=["Notifications"])
app.include_router(insurance.router, prefix="/insurance",
                   tags=["Insurance"])  # ✅ Added Insurance API


@app.get("/")
def read_root():
    return {"message": "FastAPI Backend is Running!"}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
