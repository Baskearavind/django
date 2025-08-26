🚀 Execution Steps
1️⃣ Setup Virtual Environment

Inside your project folder (ecom in your case):

python -m venv venv


Activate it:

Windows (CMD):

venv\Scripts\activate


PowerShell:

venv\Scripts\Activate.ps1


Linux/Mac:

source venv/bin/activate

2️⃣ Install Dependencies

Make sure you have requirements.txt. Then run:

pip install -r requirements.txt


(If requirements.txt is missing, install Django manually: pip install django pillow)

3️⃣ Database Setup

Run migrations to create the default tables:

python manage.py migrate

4️⃣ Create Superuser (for admin access)
python manage.py createsuperuser


👉 Enter username, email, password.

5️⃣ Register Apps in settings.py

Open ecommerce/settings.py → ensure your apps are listed under INSTALLED_APPS:

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Your apps
    'core',
    'accounts',
    'products',
    'cart',
    'orders',
    'payments',
]

6️⃣ Run Development Server
python manage.py runserver


Open in browser:

👉 Home: http://127.0.0.1:8000/

👉 Admin: http://127.0.0.1:8000/admin/

7️⃣ Add Some Data

Login to Admin with superuser credentials.

Add categories, products, etc.

Now they’ll appear on your frontend pages.

8️⃣ Test Navigation

Ensure {% url 'home' %}, {% url 'login' %}, {% url 'cart_detail' %}, etc. work.

If you see NoReverseMatch, check that the name in urls.py matches the template link.

9️⃣ Collect Static Files (optional for production)
python manage.py collectstatic
