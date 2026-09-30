# NyumbaLink FastAPI Backend

## Features
- Landlord and seeker signup
- Login
- JWT access tokens
- bcrypt password hashing
- SQLite database
- Protected landlord property posting
- Public property listing/search
- County, town, type and rent/land filters
- Swagger docs

## Run

```bash
python -m venv venv
```

Windows:
```bash
venv\Scripts\activate
```

Install:
```bash
pip install -r requirements.txt
```

Set a secret key:
```powershell
$env:SECRET_KEY="your-long-random-secret"
```

Start:
```bash
uvicorn app.main:app --reload
```

Open:
- API: http://127.0.0.1:8000
- Swagger: http://127.0.0.1:8000/docs

## Frontend integration

Replace your current `auth.js` with `frontend-auth.js`.
Replace your current `script.js` with `frontend-script.js`.

Signup forms should use:
```html
<form class="auth-form" data-mode="signup" data-role="landlord">
```
or:
```html
<form class="auth-form" data-mode="signup" data-role="seeker">
```

Login forms:
```html
<form class="auth-form" data-mode="login" data-role="landlord">
```

Expected signup field names:
`first_name`, `last_name`, `email`, `phone`, `password`, `confirm_password`

Expected login names:
`email`, `password`

Property form names:
`title`, `property_type`, `purpose`, `county`, `town`, `price`, `description`, `image_url`

Your original JavaScript only simulated submission. The replacement files actually call FastAPI.