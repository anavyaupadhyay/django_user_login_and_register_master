from userapp.api.viewsets import userviewsets
from rest_framework import routers

router = routers.DefaultRouter()
router.register('userapp',userviewsets,base_name='userapp_api')