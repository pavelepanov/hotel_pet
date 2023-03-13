from fastapi import FastAPI

from hotels.router import router as router_hotel


app = FastAPI(
    title="Hotel project"
)

app.include_router(router_hotel)


