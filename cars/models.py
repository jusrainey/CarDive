from django.db import models


class CarInsightCache(models.Model):
    """Cache ChatGPT insight results for a car."""

    year = models.IntegerField()
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    data = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("year", "make", "model")

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"
