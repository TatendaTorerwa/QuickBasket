#!/usr/bin/env python3
"""The model that holds the Category class."""

from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from base import Base

class Category(Base):
    """Represents the Category class."""

    __tablename__ = 'Categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    description = Column(Text)

    """Relationships."""
    products = relationship('Product', back_populates='category')
