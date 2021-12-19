from django.db import models

class Movie(models.Model):
    """
    Table containing information on movies.
    """
    title = models.CharField(max_length=255, null=False, blank=False)
    budget = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    homepage = models.URLField(max_length=255, null=False, blank=False)
    description = models.TextField()
    release_date = models.DateField()
    runtime = models.SmallIntegerField()

    def __str__(self) -> str:
        return self.title

