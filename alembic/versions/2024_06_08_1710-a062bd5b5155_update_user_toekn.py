"""update user toekn

Revision ID: a062bd5b5155
Revises: 1f5ada94b8a8
Create Date: 2024-06-08 17:10:28.090992

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "a062bd5b5155"
down_revision: Union[str, None] = "1f5ada94b8a8"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("users", "token", existing_type=sa.VARCHAR(), nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("users", "token", existing_type=sa.VARCHAR(), nullable=False)
    # ### end Alembic commands ###
