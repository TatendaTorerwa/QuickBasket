#!/usr/bin/env python3
"""The model that holds the Users class."""

from sqlalchemy import Column, Integer, String, Enum, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from base import Base

class User(Base):
    """Represents the User class."""

    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(100), nullable=False, unique=True)
    password_hash = Column(String(255), nullable=False)
    role = Column(Enum('admin', 'customer', name='user_roles'), default='customer')
    created_at = Column(DateTime, server_default=func.now())
    
    """Relationships."""
    orders = relationship('Order', back_populates='user')
    cart_items = relationship('CarItem', back_populates='user')
    reviews = relationship('Review', back_populates='user')
    wishlist = relationship('Wishlist', back_populates='user')
    shipping_addresses = relationship('ShippingAddress', back_populates='user')


