from rest_framework.routers import SimpleRouter
from restaurant.views import RestViewSet, RestDetailViewSet

router = SimpleRouter(trailing_slash=False)
router.register('restaurants', RestViewSet)
router.register('restaurants', RestDetailViewSet)
urlpatterns = router.urls
