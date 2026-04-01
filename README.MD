# BuyBasket Backend (Django REST)

A production-ready REST API for an e-commerce cart and order workflow. Built with Django 6, Django REST Framework, Simple JWT, and CORS handling, this backend powers secure user registration, authentication, cart management, and order checkout.

## ?? Why this project matters

- **JWT-based auth** with secure `ACCESS` and `REFRESH` token flows
- **Role-free, modern user model** with email-only login (custom `User` extends `AbstractUser`)
- **Cart workflow**: add items, view cart, remove item, clear cart
- **Order workflow**: create order, list user's order history
- **Deploy-ready** with database URL support, CORS allowlist, and Whitenoise static handling
- **Easy local setup** for contributors and bug fixes

## ?? Architecture

- `backend/` Django project root
  - `backend/settings.py`, `urls.py`, `wsgi.py`, `asgi.py`
- `users/` auth endpoints + models
- `cart/` cart endpoints + model
- `orders/` checkout/order endpoints + model

## ?? Requirements

- Python 3.10+ (recommend 3.11)
- pip
- virtualenv

## ?? Local setup

```powershell
cd D:\E-commerce\BuyBasket-backend\backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Create `.env` (if not existing) with:

- `SECRET_KEY=your-secret-key`
- `DATABASE_URL=sqlite:///db.sqlite3` (or Postgres URL)
- `DEBUG=True` for local dev only

Migrate and create superuser:

```powershell
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## ?? Endpoints

Base URL: `http://127.0.0.1:8000/`

### Auth (`api/`)

- `POST api/register/` Create user
  - body: `{ "email": "x@x.com", "name": "X", "password": "secret" }`
  - returns: user details (no password)

- `POST api/login/` JWT tokens
  - body: `{ "email": "x@x.com", "password": "secret" }`
  - returns: `access`, `refresh`

- `POST api/token/refresh/` Refresh token
  - body: `{ "refresh": "<refresh_token>" }`

- `GET api/user/` Get current user (Bearer token required)

- `POST api/logout/` Logout (cookie delete, optional)

### Cart (`cart/`)

Authentication: Bearer JWT header required

- `POST cart/addcart/`
  - body: `{ "product_name": "Shoes", "price": "59.99", "quantity": 2, "image": "https://..." }`

- `GET cart/viewcart/`
  - returns array of carts including `total` per item

- `DELETE cart/remove/<id>/`

- `DELETE cart/clear-cart/`

### Orders (`orders/`)

Authentication: Bearer JWT header required

- `POST orders/create/`
  - body example:
    {
      "product_name": "Shoes",
      "price": "59.99",
      "quantity": 2,
      "name": "John Doe",
      "phone": "1234567890",
      "address": "123 Main St",
      "city": "Sample City",
      "state": "CA",
      "pincode": "90001",
      "payment_method": "card"
    }

- `GET orders/vieworders/` List authenticated user orders (descending)

## ??? Security notes

- Production uses `SECURE_SSL_REDIRECT=True`, HTTP-only secure cookies, HSTS.
- JWT `ACCESS_TOKEN_LIFETIME=60 minutes`, `REFRESH_TOKEN_LIFETIME=1 day`.
- CORS origin lock to frontend URL: `https://buybasket-by-harshal.vercel.app`

## ?? Tests

```powershell
python manage.py test
```

## ?? Deployment hints

- Render/Heroku: set `DATABASE_URL` and `SECRET_KEY` as env vars
- Ensure `DEBUG=False`, `ALLOWED_HOSTS` includes production host
- Run `python manage.py collectstatic --noinput`

## ??? How to contribute

1. Fork and branch from `main`
2. Add features/tests in `users`, `cart`, `orders`
3. Run all tests
4. Push PR with clear summary and endpoints changed

## ?? Troubleshooting

- `ValueError: AUTH_USER_MODEL refers to model 'users.User' that is not installed` ? check `INSTALLED_APPS` ordering and run `makemigrations`
- `sqlite3.OperationalError: no such table` ? run `migrate`

---

Made with an emphasis on security, speed, and immediate API usability. 
