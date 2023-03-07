"""Change to declarative models

Revision ID: f184fb00be5c
Revises: 1386c61a2f94
Create Date: 2023-03-06 22:50:01.461157

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'f184fb00be5c'
down_revision = '1386c61a2f94'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('booking', 'room_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('booking', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('booking', 'date_from',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.alter_column('booking', 'date_to',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.alter_column('booking', 'price',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('booking', 'total_cost',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('booking', 'total_days',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('hotel', 'name',
               existing_type=sa.VARCHAR(length=140),
               nullable=False)
    op.alter_column('hotel', 'category_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('hotel', 'location',
               existing_type=sa.VARCHAR(length=140),
               nullable=False)
    op.alter_column('hotel', 'services',
               existing_type=postgresql.JSON(astext_type=sa.Text()),
               nullable=False)
    op.alter_column('hotel', 'rooms_quantity',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('hotel', 'images_id',
               existing_type=postgresql.JSON(astext_type=sa.Text()),
               nullable=False)
    op.alter_column('hotel_category', 'name',
               existing_type=sa.VARCHAR(length=140),
               nullable=False)
    op.alter_column('room', 'hotel_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('room', 'name',
               existing_type=sa.VARCHAR(length=140),
               nullable=False)
    op.alter_column('room', 'description',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
    op.alter_column('room', 'price',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('room', 'services',
               existing_type=postgresql.JSON(astext_type=sa.Text()),
               nullable=False)
    op.alter_column('room', 'quantity',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('room', 'images_id',
               existing_type=postgresql.JSON(astext_type=sa.Text()),
               nullable=False)
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(length=140),
               nullable=False)
    op.alter_column('user', 'hashed_password',
               existing_type=sa.VARCHAR(length=300),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'hashed_password',
               existing_type=sa.VARCHAR(length=300),
               nullable=True)
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(length=140),
               nullable=True)
    op.alter_column('room', 'images_id',
               existing_type=postgresql.JSON(astext_type=sa.Text()),
               nullable=True)
    op.alter_column('room', 'quantity',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('room', 'services',
               existing_type=postgresql.JSON(astext_type=sa.Text()),
               nullable=True)
    op.alter_column('room', 'price',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('room', 'description',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
    op.alter_column('room', 'name',
               existing_type=sa.VARCHAR(length=140),
               nullable=True)
    op.alter_column('room', 'hotel_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('hotel_category', 'name',
               existing_type=sa.VARCHAR(length=140),
               nullable=True)
    op.alter_column('hotel', 'images_id',
               existing_type=postgresql.JSON(astext_type=sa.Text()),
               nullable=True)
    op.alter_column('hotel', 'rooms_quantity',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('hotel', 'services',
               existing_type=postgresql.JSON(astext_type=sa.Text()),
               nullable=True)
    op.alter_column('hotel', 'location',
               existing_type=sa.VARCHAR(length=140),
               nullable=True)
    op.alter_column('hotel', 'category_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('hotel', 'name',
               existing_type=sa.VARCHAR(length=140),
               nullable=True)
    op.alter_column('booking', 'total_days',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('booking', 'total_cost',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('booking', 'price',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('booking', 'date_to',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.alter_column('booking', 'date_from',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.alter_column('booking', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('booking', 'room_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###