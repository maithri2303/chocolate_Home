from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base

class SeasonalFlavor(Base):
    __tablename__ = 'seasonal_flavors'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    is_available = Column(Boolean, default=True)

class Ingredient(Base):
    __tablename__ = 'ingredients'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    low_stock_threshold = Column(Integer, default=10)

class CustomerSuggestion(Base):
    __tablename__ = 'customer_suggestions'
    id = Column(Integer, primary_key=True)
    suggestion = Column(String, nullable=False)
    allergy_concern = Column(String, nullable=True)
