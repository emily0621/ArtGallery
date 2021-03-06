"""empty message

Revision ID: 6578c4077a7a
Revises: 
Create Date: 2022-02-08 21:06:55.357612

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6578c4077a7a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('category_name', sa.String(length=25), nullable=False),
    sa.Column('category', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category'], ['category.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tag',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('tag_name', sa.String(length=25), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('type_link',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=25), nullable=False),
    sa.Column('picture', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('viewer',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=25), nullable=False),
    sa.Column('email', sa.String(length=25), nullable=False),
    sa.Column('password', sa.String(length=45), nullable=False),
    sa.Column('avatar_link', sa.String(length=256), nullable=True),
    sa.Column('date_of_birth', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('author',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('watermark', sa.String(length=256), nullable=False),
    sa.Column('first_name', sa.String(length=25), nullable=True),
    sa.Column('last_name', sa.String(length=25), nullable=True),
    sa.Column('phone', sa.String(length=25), nullable=True),
    sa.Column('viewer_id', sa.Integer(), nullable=False),
    sa.Column('country', sa.String(length=25), nullable=True),
    sa.Column('city', sa.String(length=25), nullable=True),
    sa.ForeignKeyConstraint(['viewer_id'], ['viewer.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('watermark')
    )
    op.create_table('followers',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('author', sa.Integer(), nullable=False),
    sa.Column('viewer', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['author'], ['author.id'], ),
    sa.ForeignKeyConstraint(['viewer'], ['viewer.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('links_for_author',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('link', sa.String(length=25), nullable=False),
    sa.Column('type_link', sa.Integer(), nullable=False),
    sa.Column('author', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['author'], ['author.id'], ),
    sa.ForeignKeyConstraint(['type_link'], ['type_link.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('post',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=25), nullable=False),
    sa.Column('text', sa.String(length=1000), nullable=True),
    sa.Column('likes', sa.Integer(), nullable=False),
    sa.Column('category', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(length=256), nullable=False),
    sa.Column('author', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['author'], ['author.id'], ),
    sa.ForeignKeyConstraint(['category'], ['category.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comments',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('text', sa.String(length=256), nullable=False),
    sa.Column('likes', sa.Integer(), nullable=False),
    sa.Column('post', sa.Integer(), nullable=False),
    sa.Column('viewer', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post'], ['post.id'], ),
    sa.ForeignKeyConstraint(['viewer'], ['viewer.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('likes',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('viewer', sa.Integer(), nullable=False),
    sa.Column('post', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post'], ['post.id'], ),
    sa.ForeignKeyConstraint(['viewer'], ['viewer.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('post_has_post',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('post_first', sa.Integer(), nullable=False),
    sa.Column('post_second', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_first'], ['post.id'], ),
    sa.ForeignKeyConstraint(['post_second'], ['post.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('post_has_tag',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('post', sa.Integer(), nullable=False),
    sa.Column('tag', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post'], ['post.id'], ),
    sa.ForeignKeyConstraint(['tag'], ['tag.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post_has_tag')
    op.drop_table('post_has_post')
    op.drop_table('likes')
    op.drop_table('comments')
    op.drop_table('post')
    op.drop_table('links_for_author')
    op.drop_table('followers')
    op.drop_table('author')
    op.drop_table('viewer')
    op.drop_table('type_link')
    op.drop_table('tag')
    op.drop_table('category')
    # ### end Alembic commands ###
