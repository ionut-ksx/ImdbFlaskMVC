"""imdb table

Revision ID: 3a8c85840eed
Revises: 
Create Date: 2022-06-14 14:42:05.387149

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "3a8c85840eed"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "actors",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("name", sa.String(255), nullable=False),
        sa.Column("url", sa.String(255), nullable=False),
        sa.Column("filmography_movie_name", sa.String(255), nullable=False),
        sa.Column("filmography_url", sa.String(255), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_table(
        "movies",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("genre", sa.String(255), nullable=False),
        sa.Column("date_of_scraping", sa.String(255), nullable=False),
        sa.Column("director", sa.String(255), nullable=False),
        sa.Column("rating", sa.String(255), nullable=False),
        sa.Column("release_year", sa.String(255), nullable=False),
        sa.Column("title", sa.String(255), nullable=False),
        sa.Column("top_cast", sa.String(255), nullable=False),
        sa.Column("url", sa.String(255), nullable=False),
        sa.Column("image_urls", sa.String(255), nullable=False),
        sa.Column("images", sa.String(255), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("actors")
    op.drop_table("movies")
