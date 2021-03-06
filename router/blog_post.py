from typing import Optional
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)

class BlogModel(BaseModel):
    title: str
    content: str
    no_comments: int
    published: Optional[bool]

@router.post('/new')
def create_blog(blog: BlogModel):
    return blog.title