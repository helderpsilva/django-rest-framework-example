from django.db import models
from django.db.models.deletion import CASCADE


class Actor(models.Model):
    """
    Table with actors information.
    """

    first_name = models.CharField(max_length=255, null=False, blank=False)
    last_name = models.CharField(max_length=255, null=False, blank=False)
    age = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self) -> str:
        return "{} {}".format(self.first_name, self.last_name)


class Movie(models.Model):
    """
    Table with movies information.
    """

    title = models.CharField(max_length=255, null=False, blank=False)
    budget = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    homepage = models.URLField(max_length=255, null=False, blank=False)
    description = models.TextField()
    release_date = models.DateField()
    runtime = models.SmallIntegerField()
    movie_cast = models.ManyToManyField(Actor, through="Cast", related_name="movies")

    def __str__(self) -> str:
        return self.title


class Cast(models.Model):
    """
    Table with cast information.
    """

    movie = models.ForeignKey(Movie, on_delete=CASCADE)
    actor = models.ForeignKey(Actor, on_delete=CASCADE)
    role = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        unique_together = [["movie", "actor"]]

    def __str__(self) -> str:
        return "{}:{}".format(self.actor, self.role)
