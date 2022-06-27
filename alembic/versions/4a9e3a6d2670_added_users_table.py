"""Added users table

Revision ID: 4a9e3a6d2670
Revises: 6829415e3371
Create Date: 2022-06-26 00:39:09.234023

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "4a9e3a6d2670"
down_revision = "6829415e3371"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("username", sa.String(120), unique=True, nullable=False),
        sa.Column("email", sa.String(120), nullable=False),
        sa.Column("pwhash", sa.String(255), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("users")
