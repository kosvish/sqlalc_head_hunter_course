import os
import sys
import asyncio

sys.path.insert(1, os.path.join(sys.path[0], '../..'))
from queries.core import create_tables
from queries.orm import insert_data, async_insert_data
from queries.orm import create_tables as create_tables_orm

create_tables_orm()
# insert_data()

# asyncio.run(async_insert_data())
