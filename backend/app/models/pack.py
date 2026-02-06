from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Text
from sqlalchemy.orm import relationship
from ..db.base import Base


class Pack(Base):
    __tablename__ = "packs"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    is_active = Column(Boolean, default=True)
    
    variants = relationship("PackVariant", back_populates="pack", cascade="all, delete-orphan")


class PackVariant(Base):
    __tablename__ = "pack_variants"
    
    id = Column(Integer, primary_key=True, index=True)
    pack_id = Column(Integer, ForeignKey("packs.id"), nullable=False)
    name = Column(String(255), nullable=False)
    price = Column(Integer, nullable=False)
    
    pack = relationship("Pack", back_populates="variants")
    items = relationship("PackVariantItem", back_populates="variant", cascade="all, delete-orphan")


class PackVariantItem(Base):
    __tablename__ = "pack_variant_items"
    
    id = Column(Integer, primary_key=True, index=True)
    variant_id = Column(Integer, ForeignKey("pack_variants.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    qty = Column(Integer, nullable=False)
    
    variant = relationship("PackVariant", back_populates="items")
    product = relationship("Product")
