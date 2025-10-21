from fastapi import APIRouter

from .api_test import router as test_router


from .api_country import router as router_country
from .api_city import router as router_city
from .api_district import router as router_district
from .api_certificate_type import router as router_certificate_type
main_router = APIRouter()


main_router.include_router(test_router)


main_router.include_router(router_city)

main_router.include_router(router_district)
main_router.include_router(router_country)
main_router.include_router(router_certificate_type)