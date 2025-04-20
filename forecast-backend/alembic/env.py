# alembic/env.py
import os
import sys
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from alembic import context

# ensure src package is importable
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.config import settings
from src.db.models import Base  # your SQLAlchemy metadata

# this is the Alembic Config object
config = context.config

# overwrite the URL in alembic.ini with our sync URL
config.set_main_option("sqlalchemy.url", settings.DATABASE_SYNC_URL)

# compare metadata so autogenerate knows what’s changed
target_metadata = Base.metadata

# keep any logging settings from alembic.ini
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

def run_migrations_online() -> None:
    """Run migrations using a synchronous SQLAlchemy engine."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            # you can enable type comparison etc:
            # compare_type=True,
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    context.run_migrations()
else:
    run_migrations_online()
