from rest_framework.routers import SimpleRouter

from cards.views import CardViewSet

router = SimpleRouter(trailing_slash=False)
router.register(r'cards', CardViewSet)

urlpatterns = router.urls