from sqlalchemy import Column, Integer, String, Boolean, Date, JSON
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Queues(Base):
    __tablename__ = "queues"

    id = Column(Integer, primary_key=True, nullable=False)
    task_no = Column(String, nullable=False)
    priority = Column(Boolean, nullable=False)
    last_updated_at = Column(Date, nullable=False)
    search_count = Column(Integer, nullable=False)
    messages_json = Column(JSON)

    def __repr__(self) -> str:
        return f"Queues(task_no={self.task_no!r}, priority={self.priority!r}, last_updated_at={self.last_updated_at!r})"
