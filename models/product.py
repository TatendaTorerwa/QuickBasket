#!/usr/bin/env python3

"""The model that holds the Product class."""

from sqlalchemy import Column, Integer, String, Enum, DateTime, Float, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from base import Base

class Product(Base):
    """Represents the Product class."""

    __tablename__ = 'Products'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    price = Column(Float, nullable=False)
    stock = Column(Integer, default=0)
    image_url = Column(String(255))
    category_id = Column(Integer, ForeignKey('categories.id'))
    created_at = Column(DateTime, server_default=func.now())

    
    category = relationship('Category', back_populates='products')
    cart_items = relationship('CarItem', back_populates='product')
    order_items = relationship('OrderItem', back_populates='product')
    reviews = relationship('Review', back_populates='product')
    wishlist = relationship('Whishlist', back_populates='product')


