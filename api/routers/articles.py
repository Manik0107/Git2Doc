from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from api.database import get_db, Article
from api.models import ArticleResponse, ArticleCreate
from api.middleware.auth_middleware import get_current_admin_user

router = APIRouter(prefix="/api/articles", tags=["Articles"])


@router.get("", response_model=List[ArticleResponse])
async def get_all_articles(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """Get all articles with pagination"""
    articles = db.query(Article).offset(skip).limit(limit).all()
    return articles


@router.get("/{slug}", response_model=ArticleResponse)
async def get_article_by_slug(slug: str, db: Session = Depends(get_db)):
    """Get a single article by slug"""
    article = db.query(Article).filter(Article.slug == slug).first()
    
    if not article:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Article not found"
        )
    
    return article


@router.post("", response_model=ArticleResponse, status_code=status.HTTP_201_CREATED)
async def create_article(
    article_data: ArticleCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_admin_user)
):
    """Create a new article (admin only)"""
    
    # Check if slug already exists
    existing = db.query(Article).filter(Article.slug == article_data.slug).first()
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Article with this slug already exists"
        )
    
    new_article = Article(**article_data.dict())
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    
    return new_article


@router.put("/{article_id}", response_model=ArticleResponse)
async def update_article(
    article_id: int,
    article_data: ArticleCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_admin_user)
):
    """Update an article (admin only)"""
    
    article = db.query(Article).filter(Article.id == article_id).first()
    if not article:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Article not found"
        )
    
    # Update fields
    for key, value in article_data.dict().items():
        setattr(article, key, value)
    
    db.commit()
    db.refresh(article)
    
    return article


@router.delete("/{article_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_article(
    article_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_admin_user)
):
    """Delete an article (admin only)"""
    
    article = db.query(Article).filter(Article.id == article_id).first()
    if not article:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Article not found"
        )
    
    db.delete(article)
    db.commit()
    
    return None
