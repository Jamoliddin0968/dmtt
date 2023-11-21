from fastapi import APIRouter

from src.routers.auth import router as auth_router
from src.routers.dmtt import router as dmmt_router
from src.routers.organization import router as organization_router
from src.routers.product import router as product_router
from src.routers.season_product import router as season_product_router
from src.routers.user import router as user_router

router = APIRouter(prefix='')

router.include_router(organization_router)
router.include_router(dmmt_router)
router.include_router(user_router)
router.include_router(auth_router)
router.include_router(product_router)
router.include_router(season_product_router)
