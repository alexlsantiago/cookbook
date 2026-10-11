from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=120)
    ingredients = models.TextField(help_text="One ingredient per line")
    description = models.TextField(blank=True)
    steps = models.TextField(help_text="One step per line")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name

    @property
    def ingredient_list(self):
        return [line.strip() for line in self.ingredients.splitlines() if line.strip()]

    @property
    def step_list(self):
        return [line.strip() for line in self.steps.splitlines() if line.strip()]
