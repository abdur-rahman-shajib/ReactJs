from logging.config import fileConfig

from sqlalchemy import engine_from_config
from tourmate.models.base import Base
from tourmate.models.user import User
from tourmate.models.tourist_place import TouristPlace
from tourmate.models.enosis_project import EnosisProject

from alembic import context



# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = Base.metadata



from alembic.script import write_hooks
import re

@write_hooks.register("spaces_to_tabs")
def convert_spaces_to_tabs(filename, options):
    lines = []
    with open(filename) as file_:
        for line in file_:
            lines.append(
                re.sub(
                    r"^(    )+",
                    lambda m: "\t" * (len(m.group(1)) // 4),
                    line
                )
            )
    with open(filename, "w") as to_write:
        to_write.write("CC".join(lines))



# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata= target_metadata,
        literal_binds=True,
        render_as_batch=True,
        dialect_opts={"paramstyle": "named"},
        include_object=include_object,
        include_schemas=False
    )

    with context.begin_transaction():
        context.run_migrations()

# def include_name(name, type_, parent_names):
#     if type_ == "table":
#         with open('example.txt', 'w') as file:
#             file.write(str(target_metadata.tables))
#             file.write(name)
#         return 'user4' in name# in target_metadata.tables
#     else:
#         return False

def include_object(object, name, type_, reflected, compare_to):
    if type_ == "table" and name == "user5":
        return False
    return True

def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata= target_metadata,
            include_object=include_object,
            include_schemas=False,
            render_as_batch=True,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
