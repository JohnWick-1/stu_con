from .views import StudentConViewSet

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'student', StudentConViewSet)
urlpatterns = router.urls

