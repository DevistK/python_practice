from django.db import models
from django.db.models import F
from restaurant.models import Restaurant


class BookMark(models.Model):
    """
    ForeignKey
    - Restaurant id(PK)
    - User id(PK)
    """
    restaurant = models.ForeignKey('restaurant.Restaurant', on_delete=models.CASCADE)
    bookmark_user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=False, related_name='bookmarks')

    class Meta:
        ordering = ['-id']
        unique_together = ['restaurant', 'bookmark_user']

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        Restaurant.objects.filter(id=self.restaurant_id).update(rest_count=F('rest_count') + 1)

        super().save()
