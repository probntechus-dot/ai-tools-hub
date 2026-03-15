#!/usr/bin/env python3
"""Rebuild index.html with all 129 articles properly categorized."""

import os
import re
from collections import defaultdict
from pathlib import Path

# Define comprehensive category mapping
CATEGORY_KEYWORDS = {
    'Healthcare & Medical': ['medical', 'dental', 'healthcare', 'therapy', 'clinical', 'hospital', 'nursing', 'pharmacy', 'wellness', 'mental', 'psychology', 'psychiatry', 'speech', 'occupational'],
    'Food & Hospitality': ['bakery', 'cafe', 'restaurant', 'bar', 'brewery', 'coffee', 'catering', 'event-planning', 'hotel', 'lodging', 'guest', 'hospitality', 'dining'],
    'Real Estate & Property': ['real-estate', 'property', 'realtor', 'mortgage', 'landlord', 'property-management'],
    'Education & Learning': ['education', 'school', 'tutor', 'course', 'learning', 'academy', 'bootcamp', 'training', 'university', 'college'],
    'Marketing & Sales': ['marketing', 'seo', 'social-media', 'email', 'content', 'branding', 'sales', 'advertising', 'copywriting', 'lead-generation'],
    'E-Commerce & Retail': ['ecommerce', 'shop', 'retail', 'inventory', 'dropship', 'marketplace', 'vendor', 'commerce'],
    'Finance & Accounting': ['finance', 'bank', 'accounting', 'crypto', 'investment', 'insurance', 'credit-union', 'cryptocurrency', 'trading', 'stock'],
    'Video & Animation': ['video', 'editing', 'animation', 'motion', 'youtube', 'streaming', 'podcast'],
    'Design & Graphics': ['design', 'graphic', 'photo', 'image', 'photography', 'visual', 'art', 'illustration', 'ui-ux'],
    'Writing & Content': ['writing', 'blogging', 'copywriting', 'content-creation', 'journalism'],
    'Development & Tech': ['development', 'code', 'programming', 'software', 'app', 'web', 'database', 'it-infrastructure', 'cybersecurity'],
    'Productivity & Automation': ['automation', 'workflow', 'productivity', 'project', 'management', 'task', 'collaboration', 'crm'],
    'Manufacturing & Logistics': ['manufacturing', 'warehouse', 'logistics', 'supply-chain', 'shipping', '3d-printing'],
    'Gaming & Entertainment': ['gaming', 'game', 'esports', 'entertainment', 'escape-room', 'music', 'audio', 'sound'],
    'Travel & Tourism': ['travel', 'tourism', 'hotel', 'airline', 'itinerary', 'booking'],
    'Language & Translation': ['language', 'translation', 'multilingual', 'grammar', 'writing'],
    'Fitness & Sports': ['fitness', 'gym', 'sports', 'coaching', 'athletic', 'training', 'wellness', 'yoga'],
    'Agriculture & Farming': ['agriculture', 'farming', 'garden', 'landscape', 'aquaculture', 'fishery'],
    'HR & Recruitment': ['hr', 'recruitment', 'hiring', 'talent', 'human-resources', 'payroll', 'onboarding'],
    'Fashion & Beauty': ['fashion', 'clothing', 'beauty', 'salon', 'spa', 'cosmetics', 'hair'],
    'Automotive': ['automotive', 'vehicle', 'car', 'mechanic', 'transport', 'dealership', 'rental', 'fleet'],
    'Service & Trades': ['plumbing', 'electrical', 'construction', 'roofing', 'hvac', 'landscaping', 'lawn-care', 'cleaning', 'janitorial', 'moving'],
    'Business & General': ['business', 'startup', 'entrepreneur', 'franchise', 'corporate', 'management', 'planning'],
    'Arts & Culture': ['art', 'museum', 'gallery', 'music', 'dance', 'theater', 'film', 'culture'],
    'Government & Public': ['government', 'nonprofit', 'public', 'legal', 'law', 'court', 'compliance', 'regulation', 'policy'],
}

# Get all article files
articles_dir = Path('articles')
article_files = sorted([f for f in articles_dir.glob('*.html')])

# Extract metadata from each article
articles_data = []

for article_file in article_files:
    slug = article_file.stem
    
    # Read the article to extract title
    with open(article_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract title from <h1> tag
    title_match = re.search(r'<h1[^>]*>([^<]+)</h1>', content)
    title = title_match.group(1) if title_match else slug.replace('-', ' ').title()
    
    # Extract description from meta or first paragraph
    description_match = re.search(r'<meta name="description" content="([^"]+)"', content)
    if description_match:
        description = description_match.group(1)
    else:
        p_match = re.search(r'<p>([^<]{0,150})</p>', content)
        description = (p_match.group(1) + '...') if p_match else 'Discover AI tools for this category.'
    
    if len(description) > 150:
        description = description[:147] + '...'
    
    # Categorize based on slug
    category = 'General'
    slug_lower = slug.lower()
    for cat, keywords in CATEGORY_KEYWORDS.items():
        if any(keyword in slug_lower for keyword in keywords):
            category = cat
            break
    
    articles_data.append({
        'slug': slug,
        'title': title,
        'description': description,
        'category': category,
    })

# Group by category
categories = defaultdict(list)
for article in articles_data:
    categories[article['category']].append(article)

# Sort categories and articles
sorted_categories = sorted(categories.keys())

# Build the new index.html
html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Tools Hub - Discover the Best AI Tools for Every Industry</title>
    <meta name="description" content="Comprehensive directory of 129+ AI tools for business, marketing, design, development, and more. Expert reviews and comparisons by Sarah Mitchell.">
    <link rel="canonical" href="https://aitoolshub-psi.vercel.app/">
    <link rel="stylesheet" href="style.css">
    
    <meta property="og:title" content="AI Tools Hub - Best AI Tools Directory">
    <meta property="og:description" content="Comprehensive directory of 129+ AI tools for every industry. Expert reviews and comparisons.">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://aitoolshub-psi.vercel.app/">
    
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "WebSite",
      "name": "AI Tools Hub",
      "url": "https://aitoolshub-psi.vercel.app/",
      "description": "Comprehensive directory of 129+ AI tools",
      "publisher": {
        "@type": "Organization",
        "name": "AI Tools Hub"
      }
    }
    </script>
</head>
<body>
    <nav class="main-nav">
        <div class="nav-container">
            <a href="index.html" class="logo">AI Tools Hub</a>
            <div class="nav-links">
                <a href="#categories">Categories</a>
                <a href="#articles">All Articles</a>
            </div>
        </div>
    </nav>

    <header class="hero-section">
        <div class="hero-content">
            <h1>Discover the Best AI Tools for Every Industry</h1>
            <p class="hero-subtitle">Expert reviews and comparisons of 129+ AI platforms by Sarah Mitchell</p>
        </div>
    </header>

    <section id="categories" class="categories-section">
        <div class="container">
            <h2>Browse by Category</h2>
            <div class="category-grid">
'''

# Add category cards
for category in sorted_categories:
    article_count = len(categories[category])
    category_id = category.lower().replace(' & ', '-').replace(' ', '-')
    html += f'''                <div class="category-card">
                    <h3>{category}</h3>
                    <p>{article_count} articles</p>
                    <a href="#cat-{category_id}" class="btn-secondary">Explore</a>
                </div>
'''

html += '''            </div>
        </div>
    </section>

    <section id="articles" class="articles-section">
        <div class="container">
            <h2>Search & Filter Articles</h2>
            
            <div class="search-filter-box">
                <input type="text" id="searchInput" class="search-input" placeholder="Search articles...">
                <div class="filter-controls">
                    <select id="categoryFilter" class="filter-select">
                        <option value="">All Categories</option>
'''

# Add category filter options
for category in sorted_categories:
    html += f'                        <option value="{category}">{category}</option>\n'

html += '''                    </select>
                </div>
            </div>

            <div class="articles-results">
                <p class="results-count"><span id="resultCount">0</span> articles found</p>
                <div id="articlesContainer" class="articles-grid">
                    <!-- Articles will be loaded here by JavaScript -->
                </div>
            </div>
        </div>
    </section>
'''

# Add category sections with articles
for category in sorted_categories:
    category_id = category.lower().replace(' & ', '-').replace(' ', '-')
    html += f'''
    <section id="cat-{category_id}" class="category-articles-section">
        <div class="container">
            <h2>{category}</h2>
            <div class="articles-grid">
'''
    
    for article in sorted(categories[category], key=lambda x: x['title']):
        html += f'''                <article class="article-card" data-category="{category}" data-title="{article['title'].lower()}">
                    <h3><a href="articles/{article['slug']}.html">{article['title']}</a></h3>
                    <p>{article['description']}</p>
                    <a href="articles/{article['slug']}.html" class="read-more">Read More →</a>
                </article>
'''
    
    html += '''            </div>
        </div>
    </section>
'''

html += '''
    <footer class="main-footer">
        <div class="footer-content">
            <p>&copy; 2026 AI Tools Hub. Expert AI tool reviews by Sarah Mitchell.</p>
            <div class="footer-links">
                <a href="/about">About</a>
                <a href="/privacy">Privacy</a>
                <a href="/contact">Contact</a>
            </div>
        </div>
    </footer>

    <script>
        // Get all article cards and data
        const allArticles = Array.from(document.querySelectorAll('[data-category]'));
        const searchInput = document.getElementById('searchInput');
        const categoryFilter = document.getElementById('categoryFilter');
        const resultsCount = document.getElementById('resultCount');
        const articlesContainer = document.getElementById('articlesContainer');

        function filterArticles() {
            const searchTerm = searchInput.value.toLowerCase();
            const selectedCategory = categoryFilter.value;

            const filtered = allArticles.filter(article => {
                const title = article.getAttribute('data-title');
                const category = article.getAttribute('data-category');
                const matchesSearch = title.includes(searchTerm) || article.textContent.toLowerCase().includes(searchTerm);
                const matchesCategory = !selectedCategory || category === selectedCategory;
                return matchesSearch && matchesCategory;
            });

            // Update results container
            articlesContainer.innerHTML = '';
            filtered.forEach(article => {
                articlesContainer.appendChild(article.cloneNode(true));
            });

            resultsCount.textContent = filtered.length;
        }

        searchInput.addEventListener('input', filterArticles);
        categoryFilter.addEventListener('change', filterArticles);

        // Initialize with all articles on page load
        window.addEventListener('load', () => {
            filterArticles();
        });
    </script>
</body>
</html>'''

# Write the new index.html
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"✅ Rebuilt index.html with {len(articles_data)} articles")
print(f"📊 Categories: {len(sorted_categories)}")
for category in sorted_categories:
    print(f"   - {category}: {len(categories[category])} articles")
