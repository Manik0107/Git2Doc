from api.database import init_db, SessionLocal, User, Article, Subscription
from api.utils.password import hash_password
from datetime import datetime

# Initialize database
init_db()

# Create session
db = SessionLocal()

# Clear existing data (for development)
db.query(Article).delete()
db.query(Subscription).delete()
db.query(User).delete()
db.commit()

# Create admin user
admin_user = User(
    email="admin@git2doc.com",
    password_hash=hash_password("admin123"),
    full_name="Admin User",
    is_admin=True
)
db.add(admin_user)
db.commit()
db.refresh(admin_user)

# Create admin subscription
admin_subscription = Subscription(
    user_id=admin_user.id,
    plan="enterprise",
    status="active"
)
db.add(admin_subscription)
db.commit()

# Create test user
test_user = User(
    email="test@test.com",
    password_hash=hash_password("test123"),
    full_name="Test User",
    is_admin=False
)
db.add(test_user)
db.commit()
db.refresh(test_user)

# Create test user subscription
test_subscription = Subscription(
    user_id=test_user.id,
    plan="free",
    status="active"
)
db.add(test_subscription)
db.commit()

# Seed articles from frontend
articles_data = [
    {
        "title": "BUILDING A CAPSULE WARDROBE",
        "excerpt": "Discover how to curate a versatile wardrobe with fewer pieces that work seamlessly together, creating endless styling possibilities while embracing sustainable fashion.",
        "date": "March 19, 2025",
        "image": "https://images.unsplash.com/photo-1490481651871-ab68de25d43d?w=800&h=800&fit=crop",
        "slug": "building-capsule-wardrobe",
        "color_class": "bg-vibrant-purple",
        "author_name": "Sofia Laurent",
        "author_avatar": "https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=100&h=100&fit=crop",
        "read_time": "5 min",
        "content": """<p>The capsule wardrobe concept has revolutionized how we approach getting dressed. It's not about restriction—it's about intentional curation and discovering your authentic style.</p>
      
<h2>UNDERSTANDING THE FOUNDATION</h2>
<p>A capsule wardrobe typically consists of 30-40 versatile pieces that can be mixed and matched to create multiple outfits. The key is selecting items that reflect your lifestyle and personal aesthetic.</p>

<h2>STARTING WITH ESSENTIALS</h2>
<p>Begin with classic pieces: a well-fitted blazer, quality denim, crisp white shirts, and neutral basics. These foundational items form the backbone of your wardrobe and never go out of style.</p>

<h2>COLOR HARMONY</h2>
<p>Choose a cohesive color palette that complements your skin tone and personal style. Neutrals like black, white, navy, and beige provide versatility, while one or two accent colors add personality.</p>

<h2>QUALITY OVER QUANTITY</h2>
<p>Invest in well-made pieces that will last. Look for quality fabrics, proper construction, and timeless silhouettes. A higher price point per item often means better longevity and less overall spending.</p>

<h2>SEASONAL TRANSITIONS</h2>
<p>Rotate pieces seasonally while maintaining your core wardrobe. Layering pieces like cardigans and lightweight jackets allow your capsule to work year-round.</p>

<p>Building a capsule wardrobe is a journey of self-discovery. It teaches you what you truly love to wear and helps eliminate decision fatigue while promoting more sustainable fashion choices.</p>"""
    },
    {
        "title": "SUSTAINABLE FASHION LUXURY",
        "excerpt": "Explore how conscious design is reshaping the fashion industry, from innovative materials to transparent production practices.",
        "date": "March 15, 2025",
        "image": "https://images.unsplash.com/photo-1523381210434-271e8be1f52b?w=800&h=800&fit=crop",
        "slug": "sustainable-fashion-luxury",
        "color_class": "bg-vibrant-yellow",
        "author_name": "Alessandro Verde",
        "author_avatar": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=100&h=100&fit=crop",
        "read_time": "7 min",
        "content": None
    },
    {
        "title": "THRIFTING DESIGNER PIECES",
        "excerpt": "Learn the art of vintage shopping and how to spot authentic designer gems while building a unique, sustainable wardrobe.",
        "date": "March 10, 2025",
        "image": "https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=800&h=800&fit=crop",
        "slug": "thrifting-designer-pieces",
        "color_class": "bg-vibrant-mint",
        "author_name": "Isabella Monroe",
        "author_avatar": "https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=100&h=100&fit=crop",
        "read_time": "6 min",
        "content": None
    },
    {
        "title": "MASTERING YOUR COLOR PALETTE",
        "excerpt": "Unlock the power of color to enhance your natural features and create stunning, cohesive outfits that express your unique style.",
        "date": "February 28, 2025",
        "image": "https://images.unsplash.com/photo-1525562723836-dca67a71d5f1?w=800&h=800&fit=crop",
        "slug": "color-palette-fashion",
        "color_class": "bg-vibrant-coral",
        "author_name": "Sofia Laurent",
        "author_avatar": "https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=100&h=100&fit=crop",
        "read_time": "5 min",
        "content": None
    },
    {
        "title": "WHY CUSTOM FIT MATTERS",
        "excerpt": "Discover how proper tailoring transforms off-the-rack pieces into perfectly fitted garments that elevate your entire wardrobe.",
        "date": "February 20, 2025",
        "image": "https://images.unsplash.com/photo-1507679799987-c73779587ccf?w=800&h=800&fit=crop",
        "slug": "custom-fit-tailoring",
        "color_class": "bg-vibrant-blue",
        "author_name": "Alessandro Verde",
        "author_avatar": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=100&h=100&fit=crop",
        "read_time": "4 min",
        "content": None
    },
    {
        "title": "STATEMENT PIECES STYLING",
        "excerpt": "Master the art of accessorizing to transform simple outfits into memorable looks with jewelry, bags, and scarves.",
        "date": "February 15, 2025",
        "image": "https://images.unsplash.com/photo-1515562141207-7a88fb7ce338?w=800&h=800&fit=crop",
        "slug": "statement-pieces-styling",
        "color_class": "bg-vibrant-magenta",
        "author_name": "Isabella Monroe",
        "author_avatar": "https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=100&h=100&fit=crop",
        "read_time": "6 min",
        "content": None
    },
    {
        "title": "UNDERSTANDING TEXTILE QUALITY",
        "excerpt": "Learn to identify premium fabrics and understand how material choice impacts garment longevity, comfort, and style.",
        "date": "February 10, 2025",
        "image": "https://images.unsplash.com/photo-1558769132-cb1aea1847c8?w=800&h=800&fit=crop",
        "slug": "textile-quality-guide",
        "color_class": "bg-vibrant-orange",
        "author_name": "Sofia Laurent",
        "author_avatar": "https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=100&h=100&fit=crop",
        "read_time": "8 min",
        "content": None
    },
    {
        "title": "EMERGING FASHION DESIGNERS",
        "excerpt": "Spotlight on innovative new designers who are redefining fashion with fresh perspectives and boundary-pushing creativity.",
        "date": "February 5, 2025",
        "image": "https://images.unsplash.com/photo-1558769132-92e717d613cd?w=800&h=800&fit=crop",
        "slug": "emerging-fashion-designers",
        "color_class": "bg-vibrant-lavender",
        "author_name": "Alessandro Verde",
        "author_avatar": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=100&h=100&fit=crop",
        "read_time": "5 min",
        "content": None
    },
    {
        "title": "MONOCHROME STYLING GUIDE",
        "excerpt": "Master the sophisticated art of head-to-toe monochromatic dressing for effortlessly chic and elongating looks.",
        "date": "January 28, 2025",
        "image": "https://images.unsplash.com/photo-1483985988355-763728e1935b?w=800&h=800&fit=crop",
        "slug": "monochrome-styling-guide",
        "color_class": "bg-vibrant-yellow",
        "author_name": "Isabella Monroe",
        "author_avatar": "https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=100&h=100&fit=crop",
        "read_time": "7 min",
        "content": None
    }
]

# Insert articles
for article_data in articles_data:
    article = Article(**article_data)
    db.add(article)

db.commit()

print("✅ Database seeded successfully!")
print(f"   - Admin user: admin@git2doc.com / admin123")
print(f"   - Test user: test@test.com / test123")
print(f"   - Articles: {len(articles_data)}")

db.close()
