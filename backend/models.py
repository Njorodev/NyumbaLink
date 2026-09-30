from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Text, Float
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(80), nullable=False)
    last_name = Column(String(80), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    phone = Column(String(30), unique=True, index=True, nullable=True)
    password_hash = Column(String(255), nullable=False)
    role = Column(String(20), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    # 🔹 Links back to Property.owner
    properties = relationship("Property", back_populates="owner", cascade="all, delete-orphan")


class Property(Base):
    __tablename__ = "properties"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    property_type = Column(String(80), nullable=False)
    purpose = Column(String(20), nullable=False)
    county = Column(String(80), nullable=False)
    town = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)

    total_units = Column(Integer, nullable=False, default=1)
    available_units = Column(Integer, nullable=False, default=1)

    description = Column(Text, nullable=True)
    image_url = Column(String(500), nullable=True)
    is_available = Column(Boolean, default=True)

    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    # 🔹 Fixed: foreign key column name matches database column `user_id`
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # 🔹 Fixed: relationship attribute named `owner` so `Property.owner` works
    owner = relationship("User", back_populates="properties")