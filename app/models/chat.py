from sqlalchemy import Column, Integer, String, Text, ForeignKey
from app.database.base import Base


class ChatMessage(Base):

    __tablename__ = "chat_messages"

    id = Column(
        Integer,
        primary_key=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    role = Column(
        String
    )

    content = Column(
        Text
    )