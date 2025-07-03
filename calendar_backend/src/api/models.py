from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime, Text
from sqlalchemy.orm import relationship
from .db import Base

# PUBLIC_INTERFACE
class User(Base):
    """User model mapped to users table."""
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    clerk_id = Column(String, unique=True)
    preferences = Column(Text)

    events = relationship("Event", back_populates="user", cascade="all, delete")
    tasks = relationship("Task", back_populates="user", cascade="all, delete")
    notifications = relationship("Notification", back_populates="user", cascade="all, delete")
    oauth_tokens = relationship("OAuthToken", back_populates="user", cascade="all, delete")


# PUBLIC_INTERFACE
class Event(Base):
    """Event model mapped to events table."""
    __tablename__ = "events"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String, nullable=False)
    description = Column(Text)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    recurrence = Column(String)
    category = Column(String)
    priority = Column(String)
    color = Column(String)

    user = relationship("User", back_populates="events")


# PUBLIC_INTERFACE
class Task(Base):
    """Task model mapped to tasks table."""
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String, nullable=False)
    description = Column(Text)
    due_time = Column(DateTime)
    completed = Column(Boolean, default=False)
    category = Column(String)
    priority = Column(String)

    user = relationship("User", back_populates="tasks")


# PUBLIC_INTERFACE
class Notification(Base):
    """Notification model mapped to notifications table."""
    __tablename__ = "notifications"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    event_id = Column(Integer, ForeignKey("events.id"))
    type = Column(String)
    scheduled_time = Column(DateTime)
    sent_status = Column(Boolean, default=False)

    user = relationship("User", back_populates="notifications")
    event = relationship("Event")


# PUBLIC_INTERFACE
class OAuthToken(Base):
    """OAuthToken model for storing provider tokens securely."""
    __tablename__ = "oauth_tokens"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    provider = Column(String, nullable=False)
    token = Column(Text, nullable=False)
    expires_at = Column(DateTime)
    scopes = Column(String)

    user = relationship("User", back_populates="oauth_tokens")
