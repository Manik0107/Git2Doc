from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


# User Schemas
class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    full_name: str


class UserCreate(UserBase):
    password: Optional[str] = None


class UserLogin(BaseModel):
    username: str  # Can be email or phone
    password: Optional[str] = None


class UserResponse(UserBase):
    id: int
    is_admin: bool
    created_at: datetime
    
    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str
    user: UserResponse


# Article Schemas
class ArticleBase(BaseModel):
    title: str
    slug: str
    excerpt: str
    content: Optional[str] = None
    image: str
    author_name: str
    author_avatar: str
    date: str
    read_time: str
    color_class: str


class ArticleCreate(ArticleBase):
    pass


class ArticleResponse(ArticleBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True


# Document Schemas
class DocumentCreate(BaseModel):
    repo_url: str
    prompt: Optional[str] = None


class DocumentResponse(BaseModel):
    id: int
    user_id: int
    name: str
    repo_url: str
    github_repo: str
    status: str
    file_path: Optional[str] = None
    pages: Optional[int] = None
    size: Optional[str] = None
    created_at: datetime
    
    class Config:
        from_attributes = True


# Subscription Schemas
class SubscriptionResponse(BaseModel):
    id: int
    user_id: int
    plan: str
    status: str
    started_at: datetime
    expires_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True
