"""Database creation

Revision ID: f43c567e27b5
Revises:
Create Date: 2024-02-13 17:18:01.230353

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "f43c567e27b5"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "files",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("file", sa.LargeBinary(), nullable=False),
        sa.Column("content_type", sa.String(), nullable=False),
        sa.Column("path", sa.String(), nullable=False),
        sa.Column("size", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("files")
    # ### end Alembic commands ###
