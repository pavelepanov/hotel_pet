from fastapi import FastAPI

from hotels.routers import router as router_hotel


app = FastAPI(
    title="Hotel project"
)


def register_routers():
    app.include_router(router_hotel)


register_routers()

