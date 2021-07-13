"""empty message

Revision ID: b62de5541991
Revises: 6cecfa349d58
Create Date: 2021-07-13 11:39:53.266592

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b62de5541991'
down_revision = '6cecfa349d58'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('cart_product_id_fkey', 'cart', type_='foreignkey')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key('cart_product_id_fkey', 'cart', 'product', ['product_id'], ['id'])
    # ### end Alembic commands ###