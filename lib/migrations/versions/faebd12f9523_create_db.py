# lib/migrations/versions/faebd12f9523_create_db.py
"""create db

Revision ID: faebd12f9523
Revises: 
Create Date: 2023-03-15 13:20:05.247015

"""
from alembic import op # type: ignore
import sqlalchemy as sa # type: ignore


# revision identifiers, used by Alembic.
revision = 'faebd12f9523'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Create the 'games' table
    op.create_table(
        'games',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('title', sa.String(), nullable=True),
        sa.Column('platform', sa.String(), nullable=True),
        sa.Column('genre', sa.String(), nullable=True),
        sa.Column('price', sa.Integer(), nullable=True),
    )
    # Create the 'reviews' table
    op.create_table(
        'reviews',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('score', sa.Integer(), nullable=True),
        sa.Column('comment', sa.String(), nullable=True),
        sa.Column('game_id', sa.Integer(), sa.ForeignKey('games.id'), nullable=True),
    )


def downgrade() -> None:
    # Drop the tables in reverse order
    op.drop_table('reviews')
    op.drop_table('games')