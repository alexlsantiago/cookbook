# Cookbook

A small Django app for keeping toast recipes. Everything lives on one screen:
recipes render as toast-style popup cards that slide in, you click one to expand
it, and you can search the collection by ingredient.

Built as my research-milestone sample project for the Django/Python framework.

## Running it

```
pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py runserver 8042
```

Then open http://localhost:8042/``

