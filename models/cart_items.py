#!/usr/bin/env python3
"""The model that holds the CartItems class."""

from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from base import Base

class CartItem(Base):
    """Represents CartItems class."""

    __tablename__ = 'cart_items'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, default=1)
    added_at = Column(DateTime, server_default=func.now())

    user = relationship('User', back_populates='cart_items')
    product = relationship('Product', back_populates='cart_items')
