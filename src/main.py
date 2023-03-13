from hotels.router import router as router_hotel
from bookings.router import router as router_bookings

from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import ValidationError
from fastapi.responses import JSONResponse


app = FastAPI(
    title="Hotel project"
)


@app.exception_handler(ValidationError)
async def validation_exception_handler(request: Request, exc: ValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors()}),
    )

app.include_router(router_hotel)
app.include_router(router_bookings)


