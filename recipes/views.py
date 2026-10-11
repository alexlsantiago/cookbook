from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST

from .models import Recipe

FIELDS = ("name", "ingredients", "description", "steps")
REQUIRED = ("name", "ingredients", "steps")


def mark_matches(recipes, query):
    """Tag each ingredient line with whether it matches the search term."""
    needle = query.lower()
    tagged = []
    for recipe in recipes:
        recipe.matches = [
            {"text": line, "hit": bool(needle) and needle in line.lower()}
            for line in recipe.ingredient_list
        ]
        recipe.hit_count = sum(1 for match in recipe.matches if match["hit"])
        tagged.append(recipe)
    return tagged


def index(request):
    query = request.GET.get("q", "").strip()
    draft, error, form_open = {}, None, False

    if request.method == "POST":
        draft = {field: request.POST.get(field, "").strip() for field in FIELDS}
        if all(draft[field] for field in REQUIRED):
            Recipe.objects.create(**draft)
            return redirect("index")
        error = "Name, ingredients, and steps are all required."
        form_open = True

    everything = Recipe.objects.all()
    found = everything.filter(ingredients__icontains=query) if query else everything

    return render(request, "recipes/index.html", {
        "recipes": mark_matches(found, query),
        "query": query,
        "total": everything.count(),
        "draft": draft,
        "error": error,
        "form_open": form_open,
    })


@require_POST
def delete(request, pk):
    Recipe.objects.filter(pk=pk).delete()
    return redirect("index")
