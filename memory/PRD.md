# FoodNova - Product Requirements Document

## Original Problem Statement
Build FoodNova as a production-ready full-stack food ordering app (Customer + Admin) with:
- Customer login, admin login, ordering, cart, checkout
- Receipt upload for payment verification
- Admin dashboard for orders, products, stock management

## User Choices
- Database: PostgreSQL (production) + SQLite (local dev)
- Payment: Manual verification only (admin approves receipts)
- Storage: Local file storage with abstraction for future S3
- UI Theme: Clean minimal white theme with deep green + warm accents
- Currency: Nigerian Naira (₦) with comma formatting

## Architecture

### Backend (FastAPI)
```
backend/
├── app/
│   ├── core/         # config, security, cors
│   ├── db/           # session, base, init_db
│   ├── models/       # SQLAlchemy models
│   ├── schemas/      # Pydantic schemas
│   ├── routes/       # API endpoints
│   └── services/     # inventory, pricing, receipts
├── uploads/          # Receipt storage
└── requirements.txt
```

### Frontend (React)
```
frontend/
├── src/
│   ├── api/          # client, auth, store
│   ├── components/   # Navbar, ProductCard, CartDrawer, etc.
│   ├── context/      # AuthContext, CartContext
│   └── pages/        # Home, Login, Checkout, Admin pages
└── package.json
```

## User Personas

### Customer
- Browse products and packs
- Add items to cart
- Place orders with delivery info
- Upload payment receipts
- Track order status

### Admin
- View dashboard with stats
- Manage orders (status updates)
- Approve/reject payment receipts
- Manage products (CRUD)
- Monitor stock levels

## Core Requirements (Implemented)

### Authentication
- [x] JWT-based authentication with access + refresh tokens
- [x] Customer registration
- [x] Customer login
- [x] Admin login with role validation
- [x] Protected routes for both customer and admin

### Products & Categories
- [x] Category listing (Rice, Oil, Pasta & Noodles)
- [x] Product listing with filtering
- [x] Product images and stock display
- [x] Naira price formatting

### Bundle Packs
- [x] Pack listing with variants
- [x] Pack detail modal with items
- [x] Add pack variant to cart

### Shopping Cart
- [x] Add/remove items
- [x] Quantity adjustment
- [x] Cart persistence (localStorage)
- [x] Cart drawer with subtotal

### Checkout & Orders
- [x] Checkout form (address, phone)
- [x] Payment method selection
- [x] Order creation with items
- [x] Stock reduction on order
- [x] Order listing (my orders)
- [x] Order detail view

### Receipt Upload
- [x] File upload (PNG, JPG, WEBP, PDF)
- [x] Storage abstraction (local/S3)
- [x] Receipt status tracking

### Admin Dashboard
- [x] Order statistics
- [x] Revenue calculation
- [x] Recent orders list
- [x] Low stock alerts

### Admin Order Management
- [x] Order list with filters
- [x] Order detail view
- [x] Status updates
- [x] Receipt approval/rejection

### Admin Product Management
- [x] Product list with search
- [x] Create product
- [x] Edit product
- [x] Delete product (soft delete)
- [x] Stock management
- [x] Add new category from Products page

### Admin Pack Management
- [x] Pack list view at /admin/packs
- [x] Create new pack
- [x] Edit pack details
- [x] Delete pack
- [x] Add variants with items
- [x] Edit/delete variants

### Order Status
- [x] Pending
- [x] Paid
- [x] Confirmed
- [x] Out for Delivery
- [x] Delivered (NEW)
- [x] Cancelled

## What's Been Implemented (Feb 2026)
- Full backend API with FastAPI + SQLAlchemy
- Database models: User, Category, Product, Pack, Order, Receipt, Payment
- JWT authentication with role-based access
- All CRUD endpoints for admin
- React frontend with shadcn/ui
- Responsive design with Tailwind CSS
- Cart with localStorage persistence
- Complete checkout flow
- Admin dashboard with analytics
- Receipt upload and verification

## Prioritized Backlog

### P0 (Critical) - DONE
- [x] Core ordering flow
- [x] Admin receipt verification
- [x] Authentication

### P1 (Important)
- [ ] Email notifications on order status change
- [ ] Order history search/filter
- [ ] Bulk product import

### P2 (Nice to Have)
- [ ] Customer address book
- [ ] Order cancellation by customer
- [ ] Product reviews
- [ ] Wishlist feature

## Recent Updates (Feb 7, 2026)
- ✅ Fixed cart persistence bug (cart items now persist after page navigation)
- ✅ Added "Add Category" feature to Admin Products page
- ✅ Created Admin Packs management page (/admin/packs)
- ✅ Added "Delivered" status to order workflow
- ✅ Added backend tests for admin features (15 pytest tests)

## Next Tasks
1. Deploy to Render (backend) and Vercel (frontend)
2. Add navbar logo (need image URL from user)
3. Add email notifications (SendGrid integration)
4. Implement Paystack/Stripe for automated payments
5. Add product image upload to S3

## Default Credentials
- Admin: admin@foodnova.com / Admin123!
