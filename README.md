git clone https://github.com/Baskearavind/django.git

cd django

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py createsuperuser

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
