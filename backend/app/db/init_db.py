from sqlalchemy.orm import Session
from ..db.session import engine
from ..db.base import Base
from ..models import User, Category, Product, Pack, PackVariant, PackVariantItem
from ..core.config import settings
from ..core.security import hash_password


def init_db(db: Session):
    """Initialize database with tables and seed data"""
    # Create all tables
    Base.metadata.create_all(bind=engine)
    
    # Check if already seeded
    if db.query(User).first():
        print("Database already seeded, skipping...")
        return
    
    print("Seeding database...")
    
    # Create admin user
    admin = User(
        email=settings.ADMIN_EMAIL,
        password_hash=hash_password(settings.ADMIN_PASSWORD),
        full_name="Admin User",
        role="admin"
    )
    db.add(admin)
    
    # Create categories
    categories = [
        Category(name="Rice"),
        Category(name="Oil"),
        Category(name="Pasta & Noodles")
    ]
    for cat in categories:
        db.add(cat)
    db.commit()
    
    # Get category IDs
    rice_cat = db.query(Category).filter(Category.name == "Rice").first()
    oil_cat = db.query(Category).filter(Category.name == "Oil").first()
    pasta_cat = db.query(Category).filter(Category.name == "Pasta & Noodles").first()
    
    # Create products
    products = [
        Product(
            name="Rice 5kg",
            price=8500,
            stock_qty=100,
            category_id=rice_cat.id,
            image_url="https://images.unsplash.com/photo-1586201375761-83865001e31c?w=400"
        ),
        Product(
            name="Palm Oil 1L",
            price=2500,
            stock_qty=100,
            category_id=oil_cat.id,
            image_url="https://images.unsplash.com/photo-1474979266404-7eaacbcd87c5?w=400"
        ),
        Product(
            name="Indomie Pack",
            price=1500,
            stock_qty=200,
            category_id=pasta_cat.id,
            image_url="https://images.unsplash.com/photo-1612929633738-8fe44f7ec841?w=400"
        )
    ]
    for prod in products:
        db.add(prod)
    db.commit()
    
    # Get product IDs
    rice = db.query(Product).filter(Product.name == "Rice 5kg").first()
    oil = db.query(Product).filter(Product.name == "Palm Oil 1L").first()
    noodles = db.query(Product).filter(Product.name == "Indomie Pack").first()
    
    # Create packs
    packs_data = [
        {
            "name": "Starter Pack",
            "description": "Perfect for singles and small households",
            "variants": [
                {
                    "name": "Basic",
                    "price": 10000,
                    "items": [
                        {"product_id": rice.id, "qty": 1},
                        {"product_id": noodles.id, "qty": 2}
                    ]
                },
                {
                    "name": "Plus",
                    "price": 12500,
                    "items": [
                        {"product_id": rice.id, "qty": 1},
                        {"product_id": oil.id, "qty": 1},
                        {"product_id": noodles.id, "qty": 2}
                    ]
                }
            ]
        },
        {
            "name": "Family Pack",
            "description": "Great value for families",
            "variants": [
                {
                    "name": "Standard",
                    "price": 22000,
                    "items": [
                        {"product_id": rice.id, "qty": 2},
                        {"product_id": oil.id, "qty": 2},
                        {"product_id": noodles.id, "qty": 4}
                    ]
                },
                {
                    "name": "Large",
                    "price": 35000,
                    "items": [
                        {"product_id": rice.id, "qty": 3},
                        {"product_id": oil.id, "qty": 3},
                        {"product_id": noodles.id, "qty": 6}
                    ]
                }
            ]
        },
        {
            "name": "Premium Pack",
            "description": "Our best value bundle",
            "variants": [
                {
                    "name": "Gold",
                    "price": 45000,
                    "items": [
                        {"product_id": rice.id, "qty": 4},
                        {"product_id": oil.id, "qty": 4},
                        {"product_id": noodles.id, "qty": 8}
                    ]
                },
                {
                    "name": "Platinum",
                    "price": 65000,
                    "items": [
                        {"product_id": rice.id, "qty": 6},
                        {"product_id": oil.id, "qty": 6},
                        {"product_id": noodles.id, "qty": 12}
                    ]
                }
            ]
        }
    ]
    
    for pack_data in packs_data:
        pack = Pack(
            name=pack_data["name"],
            description=pack_data["description"]
        )
        db.add(pack)
        db.commit()
        db.refresh(pack)
        
        for variant_data in pack_data["variants"]:
            variant = PackVariant(
                pack_id=pack.id,
                name=variant_data["name"],
                price=variant_data["price"]
            )
            db.add(variant)
            db.commit()
            db.refresh(variant)
            
            for item_data in variant_data["items"]:
                item = PackVariantItem(
                    variant_id=variant.id,
                    product_id=item_data["product_id"],
                    qty=item_data["qty"]
                )
                db.add(item)
        
        db.commit()
    
    print("Database seeded successfully!")
