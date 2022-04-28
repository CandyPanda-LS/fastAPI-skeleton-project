from fastapi import APIRouter
from ..services import blog
router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)

@router.get('/')
def all():
    return blog.get_all()