from sqlalchemy import Table, Column, Integer, String, JSON, TIMESTAMP, ForeignKey, MetaData

metadata = MetaData()

booking = Table(
    "booking",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("room_id", Integer, ForeignKey("room.id")),
    Column("user_id", Integer, ForeignKey("user.id")),
    Column("date_from", TIMESTAMP),
    Column("date_to", TIMESTAMP),
    Column("price", Integer),
    Column("total_cost", Integer),
    Column("total_days", Integer),
)

room = Table(
    "room",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("hotel_id", Integer, ForeignKey("hotel.id")),
    Column("name", String(140)),
    Column("description", String(250)),
    Column("price", Integer),
    Column("services", JSON),
    Column("quantity", Integer),
    Column("images_id", JSON),
)

hotel = Table(
    "hotel",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(140)),
    Column("category_id", Integer, ForeignKey("hotel_category.id")),
    Column("location", String(140)),
    Column("services", JSON),
    Column("rooms_quantity", Integer),
    Column("images_id", JSON),
)

hotel_category = Table(
    "hotel_category",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(140)),
)

user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String(140)),
    Column("hashed_password", String(300)),
)
