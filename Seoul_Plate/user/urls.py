from rest_framework.routers import SimpleRouter

from user.views import UserViewSet

router = SimpleRouter(trailing_slash=False)
router.register(r'users', UserViewSet)
urlpatterns = router.urls
