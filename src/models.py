import datetime
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, func, text
from src.database import Base, str_200
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional, Annotated
import enum

intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
updated_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"),
                                                        onupdate=datetime.datetime.utcnow
                                                        )]


class WorkersOrm(Base):
    __tablename__ = 'workers'
    id: Mapped[intpk]
    username: Mapped[str]


class WorkLoad(enum.Enum):
    parttime = 'partime'
    fulltime = 'fulltime'


class ResumesOrm(Base):
    __tablename__ = "resumes"

    id: Mapped[intpk]
    title: Mapped[str_200]
    compensation: Mapped[Optional[int]]
    workload: Mapped[WorkLoad]
    worker_id: Mapped[int] = mapped_column(ForeignKey("workers.id", ondelete="CASCADE"))
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]


metadata_obj = MetaData()

workers_table = Table(
    'workers',
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column('username', String)
)
