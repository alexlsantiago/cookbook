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

Then open http://localhost:8042/

## What it does

**Add a recipe.** Four fields: name, ingredients, description (optional), steps.
Ingredients and steps are entered one per line; the app splits them into
structured lists and counts them, so each card shows "5 ingredients · 4 steps".

**Search by ingredient.** Typing an ingredient filters the stack to recipes that
use it, reports how many of the total matched, auto-expands those cards, and
highlights the specific ingredient lines that matched.

**Delete.** The × on a card arms a two-step confirm (Delete / Cancel) rather than
a browser dialog, so it works in embedded browsers that suppress `confirm()`.

## Layout

| Path | What's in it |
|---|---|
| `recipes/models.py` | The `Recipe` model, plus `ingredient_list` / `step_list` line splitting |
| `recipes/views.py` | `index` (list + search + add) and `delete`; `mark_matches` tags matching lines |
| `recipes/urls.py` | Two routes |
| `recipes/templates/recipes/index.html` | The entire UI — markup, CSS, and the small delete script |

## Colors

Cream `#f7f1e1` and forest green `#1f4d33`, defined as CSS variables at the top
of the template.
