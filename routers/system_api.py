from fastapi import APIRouter
from common.system_util import get_system_info
router = APIRouter()


@router.get("/")
def get_system():
    return get_system_info()
