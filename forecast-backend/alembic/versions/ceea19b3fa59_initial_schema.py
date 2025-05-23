"""initial schema

Revision ID: ceea19b3fa59
Revises: 
Create Date: 2025-04-20 13:11:20.381578

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ceea19b3fa59'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('hashed_password', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.drop_table('goals')
    op.drop_table('titles')
    op.drop_table('employees')
    op.drop_table('credits')
    op.drop_table('projects')
    op.drop_table('Employee_trend')
    # ### end Alembic commands ###


# def downgrade():
#     op.execute("DROP TABLE IF EXISTS goals CASCADE")



def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Employee_trend',
    sa.Column('emp_no', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('gender', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('marital_status', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('age_band', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('age', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('department', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('education', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('education_field', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('job_role', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('business_travel', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('employee_count', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('attrition', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('attrition_label', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('job_satisfaction', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('active_employee', sa.BOOLEAN(), autoincrement=False, nullable=True)
    )
    op.create_table('projects',
    sa.Column('project_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('project_name', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('emp_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['emp_id'], ['employees.emp_id'], name='projects_emp_id_fkey'),
    sa.PrimaryKeyConstraint('project_id', name='projects_pkey')
    )
    op.create_table('credits',
    sa.Column('person_id', sa.NUMERIC(), autoincrement=False, nullable=True),
    sa.Column('id', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('character', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('role', sa.VARCHAR(), autoincrement=False, nullable=True)
    )
    op.create_table('employees',
    sa.Column('emp_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('f_name', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('l_name', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('department', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('salary', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('joining_date', sa.DATE(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('emp_id', name='employees_pkey')
    )
    op.create_table('titles',
    sa.Column('id', sa.VARCHAR(), server_default=sa.text("nextval('titles_id_seq'::regclass)"), autoincrement=False, nullable=False),
    sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('type', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('description', sa.VARCHAR(length=8000), autoincrement=False, nullable=True),
    sa.Column('release_year', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('age_certification', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('runtime', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('genres', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('production_countries', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('seasons', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('imdb_id', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('imdb_score', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('imdb_votes', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('tmdb_popularity', sa.NUMERIC(), autoincrement=False, nullable=True),
    sa.Column('tmdb_score', sa.NUMERIC(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='titles_pkey')
    )
    op.create_table('goals',
    sa.Column('GOAL_ID', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('MATCH_ID', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('PID', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('DURATION', sa.NUMERIC(), autoincrement=False, nullable=True),
    sa.Column('ASSIST', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('GOAL_DESC', sa.String(), autoincrement=False, nullable=True)
    )
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
