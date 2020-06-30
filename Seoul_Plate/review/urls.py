from rest_framework.routers import SimpleRouter

from review.views import ReviewViewSet

router = SimpleRouter(trailing_slash=False)
router.register(r'review', ReviewViewSet)
urlpatterns = router.urls
