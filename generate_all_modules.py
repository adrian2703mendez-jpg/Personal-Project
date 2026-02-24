#!/usr/bin/env python3
"""
Module Page Generator for Seeds of Wealth Course System
Generates all 51 module pages from complete course database
"""

import os
import json
from pathlib import Path

# Complete course database (from Course-Content.html)
courseDatabase = {
    1: {"id": 1, "title": "Investment Basics 101", "instructor": "John Smith", "category": "beginner", "modules": [
        {"id": 1, "title": "Module 1: Why Invest?", "lessons": [
            {"id": 1, "title": "The Power of Investing & Compound Interest", "duration": "8 min", "description": "Discover why investing matters.", "content": "Investing grows wealth through compound interest.", "youtubeUrl": "https://www.youtube.com/embed/xDqfM0fH2Fs", "resources": []},
            {"id": 2, "title": "Risk vs Reward", "duration": "10 min", "description": "Investment risk-reward relationship.", "content": "Understand risk spectrum.", "youtubeUrl": "https://www.youtube.com/embed/T8D8L3nshqY", "resources": []},
            {"id": 3, "title": "Types of Investments", "duration": "12 min", "description": "Overview of asset classes.", "content": "Stocks, bonds, real estate...", "youtubeUrl": "https://www.youtube.com/embed/XdFFF9w-cYo", "resources": []},
            {"id": 4, "title": "Getting Started", "duration": "9 min", "description": "First investment steps.", "content": "Open brokerage account.", "youtubeUrl": "https://www.youtube.com/embed/v9D7HLoI_e8", "resources": []}
        ]},
        {"id": 2, "title": "Module 2: Building Your Foundation", "lessons": [
            {"id": 5, "title": "Creating Your Investment Plan", "duration": "11 min", "description": "Develop investment strategy.", "content": "Set goals and allocate.", "youtubeUrl": "https://www.youtube.com/embed/oTKp4M9YlJ0", "resources": []},
            {"id": 6, "title": "Emergency Fund", "duration": "8 min", "description": "Importance of emergency fund.", "content": "3-6 month fund needed.", "youtubeUrl": "https://www.youtube.com/embed/7dH0RKB2wAQ", "resources": []},
            {"id": 7, "title": "Diversification", "duration": "10 min", "description": "Spread investments.", "content": "Not all eggs in one basket.", "youtubeUrl": "https://www.youtube.com/embed/m4OQYu6EkEw", "resources": []}
        ]},
        {"id": 3, "title": "Module 3: Your First Investment", "lessons": [
            {"id": 8, "title": "Index Funds & ETFs", "duration": "11 min", "description": "Low-cost vehicles.", "content": "Instant diversification.", "youtubeUrl": "https://www.youtube.com/embed/u2MKXqzqKdI", "resources": []},
            {"id": 9, "title": "Dollar-Cost Averaging", "duration": "9 min", "description": "Regular investing.", "content": "Smooth volatility.", "youtubeUrl": "https://www.youtube.com/embed/7_LqjrDdP5o", "resources": []},
            {"id": 10, "title": "Tracking Progress", "duration": "7 min", "description": "Monitor performance.", "content": "Stay motivated.", "youtubeUrl": "https://www.youtube.com/embed/Kz3jfTVJWzU", "resources": []}
        ]}
    ]},
    2: {"id": 2, "title": "Stock Market Fundamentals", "instructor": "Sarah Johnson", "category": "beginner", "modules": [
        {"id": 1, "title": "Module 1: Understanding Stocks", "lessons": [
            {"id": 1, "title": "What is a Stock?", "duration": "9 min", "description": "Stock basics.", "content": "Ownership share.", "youtubeUrl": "https://www.youtube.com/embed/p7HKvqRI_Bo", "resources": []},
            {"id": 2, "title": "How Stock Markets Work", "duration": "11 min", "description": "Market mechanics.", "content": "Exchanges and trading.", "youtubeUrl": "https://www.youtube.com/embed/EWz3ZyJNPWo", "resources": []},
            {"id": 3, "title": "Major Stock Exchanges", "duration": "8 min", "description": "NYSE, NASDAQ overview.", "content": "Market indices.", "youtubeUrl": "https://www.youtube.com/embed/DFuL-bFQ7f4", "resources": []}
        ]},
        {"id": 2, "title": "Module 2: Reading Stock Data", "lessons": [
            {"id": 4, "title": "Reading Stock Quotes", "duration": "10 min", "description": "Quote interpretation.", "content": "Understand metrics.", "youtubeUrl": "https://www.youtube.com/embed/WBZdGMhZqe4", "resources": []},
            {"id": 5, "title": "Stock Charts", "duration": "12 min", "description": "Chart analysis.", "content": "Identify trends.", "youtubeUrl": "https://www.youtube.com/embed/gl6aqXZFao8", "resources": []}
        ]},
        {"id": 3, "title": "Module 3: Your First Stock Purchase", "lessons": [
            {"id": 6, "title": "How to Buy Your First Stock", "duration": "9 min", "description": "Purchase guide.", "content": "Step-by-step process.", "youtubeUrl": "https://www.youtube.com/embed/HfI1XP1mPrA", "resources": []},
            {"id": 7, "title": "Market Terminology", "duration": "10 min", "description": "Key terms.", "content": "Essential vocabulary.", "youtubeUrl": "https://www.youtube.com/embed/JT16zw0K-Ts", "resources": []},
            {"id": 8, "title": "Avoiding Mistakes", "duration": "8 min", "description": "Common pitfalls.", "content": "Beginner mistakes.", "youtubeUrl": "https://www.youtube.com/embed/j2rZ7g3c8P4", "resources": []}
        ]}
    ]},
}

def generate_module_html(course_id, module_id, course_data, module_data):
    """Generate HTML for a module page"""
    course_title = course_data["title"]
    instructor = course_data["instructor"]
    category = course_data["category"]
    module_title = module_data["title"]
    lessons = module_data["lessons"]
    
    total_minutes = sum(int(l["duration"].split()[0]) for l in lessons)
    hours = total_minutes // 60
    minutes = total_minutes % 60
    time_str = f"{hours}h {minutes}m" if hours else f"{minutes} mins"
    
    # Generate chapter data JavaScript
    chapters_js = ""
    for lesson in lessons:
        chapters_js += f"""        {{
          id: {lesson['id']},
          title: "{lesson['title'].replace('"', '\\"')}",
          duration: "{lesson['duration']}",
          type: "video",
          completed: false,
          description: "{lesson['description'].replace('"', '\\"')}",
          content: "{lesson['content'].replace('"', '\\"')}",
          youtubeUrl: "{lesson['youtubeUrl']}",
          resources: {json.dumps(lesson.get('resources', []))}
        }},
"""
    chapters_js = chapters_js[:-2]  # Remove last comma
    
    html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>{module_title} - {course_title}</title>
  <link rel="stylesheet" href="Colors.css">
  <link rel="stylesheet" href="shared.css">
  <link rel="stylesheet" href="module.css">
</head>
<body>
  <header class="site-header">
    <div class="container header-inner">
      <a class="brand" href="Lobby.html">Seeds of Wealth</a>
      <nav class="header-nav">
        <a class="nav-link" href="Lobby.html">Lobby</a>
        <a class="nav-link" href="Introduction to course.html">Info</a>
      </nav>
      <div class="header-actions">
        <a class="nav-link" id="accountBtn" href="#" onclick="goToAccount(event)">Account</a>
      </div>
    </div>
  </header>

  <main class="module-page {category}">
    <div class="module-container">
      <!-- Sidebar Navigation -->
      <aside class="module-sidebar">
        <div class="module-sidebar-header">
          <h3>Navigation</h3>
          <div class="module-category-badge">{category.title()}</div>
        </div>
        <div class="module-sidebar-body" id="moduleNav">
          <!-- Module navigation will be loaded here -->
        </div>
        <a href="Lobby.html" class="back-button">
          <span>🏠</span>
          <span>Back to Lobby</span>
        </a>
      </aside>

      <!-- Main Content -->
      <section class="module-main">
        <!-- Module Header -->
        <div class="module-header">
          <div class="module-header-content">
            <h1>{module_title}</h1>
            <div class="module-header-meta">
              <span>📚 {course_title}</span>
              <span>👨‍🏫 {instructor}</span>
              <span>⏱️ {time_str}</span>
              <span>📊 {len(lessons)} Chapters</span>
            </div>
          </div>
        </div>

        <!-- Chapters List -->
        <div class="module-chapters">
          <div class="chapters-header">
            <h2>Chapters</h2>
            <span class="chapters-count" id="chaptersCount">{len(lessons)} chapters</span>
          </div>
          <div class="chapters-list" id="chaptersList">
            <!-- Chapters will be loaded here -->
          </div>
        </div>

        <!-- Chapter Content Viewer -->
        <div class="chapter-viewer" id="chapterViewer">
          <div class="chapter-viewer-header">
            <h2 class="chapter-viewer-title" id="chapterTitle">Select a chapter to begin</h2>
            <div class="chapter-viewer-meta">
              <span id="chapterDuration">Duration: --</span>
              <span id="chapterType">Type: --</span>
            </div>
          </div>
          
          <div id="videoContainer" class="video-container"></div>
          
          <div id="chapterDescription" class="chapter-description">
            <p style="color: var(--muted-text); text-align: center;">Select a chapter from the list above to view content.</p>
          </div>

          <!-- Resources Section -->
          <section id="resourcesSection" class="chapter-resources" style="display: none;">
            <h3>📥 Resources for this Chapter</h3>
            <div class="resources-list" id="resourcesList"></div>
          </section>

          <!-- Chapter Navigation -->
          <div class="chapter-navigation">
            <button class="btn-nav" id="prevBtn" onclick="previousChapter()" disabled>← Previous</button>
            <div class="chapter-indicator" id="chapterIndicator">Chapter 0 of 0</div>
            <button class="btn-nav" id="nextBtn" onclick="nextChapter()" disabled>Next →</button>
          </div>

          <!-- Module Actions -->
          <div class="module-actions">
            <button class="btn-primary" id="completeBtn" onclick="completeChapter()">✓ Mark Chapter Complete</button>
            <button class="btn-secondary" onclick="toggleResources()">📥 View Resources</button>
            <a href="Assessments.html" class="btn-secondary" style="text-decoration: none;">🧪 Take Quiz</a>
          </div>
        </div>
      </section>

      <!-- Right Panel - Module Info -->
      <aside class="module-info-panel">
        <div class="info-card">
          <h3>📚 Module Info</h3>
          <div class="info-item">
            <label>Course</label>
            <p>{course_title}</p>
          </div>
          <div class="info-item">
            <label>Instructor</label>
            <p id="instructorName">{instructor}</p>
          </div>
          <div class="info-item">
            <label>Total Chapters</label>
            <p id="totalChapters">{len(lessons)}</p>
          </div>
          <div class="info-item">
            <label>Estimated Time</label>
            <p id="estimatedTime">{time_str}</p>
          </div>
        </div>

        <div class="info-card">
          <h3>🎯 Progress</h3>
          <div class="progress-stats">
            <div class="stat">
              <p class="stat-value" id="completedChapters">0</p>
              <p class="stat-label">Chapters Completed</p>
            </div>
            <div class="stat">
              <p class="stat-value" id="moduleProgress">0%</p>
              <p class="stat-label">Module Progress</p>
            </div>
          </div>
        </div>

        <div class="info-card">
          <h3>💡 Tips</h3>
          <ul class="tips-list">
            <li>Take notes while watching</li>
            <li>Complete all chapters</li>
            <li>Review before moving on</li>
            <li>Join the discussion forum</li>
          </ul>
        </div>
      </aside>
    </div>
  </main>

  <script>
    // Module Data
    const moduleData = {{
      courseId: {course_id},
      courseName: "{course_title}",
      moduleId: {module_id},
      moduleName: "{module_title}",
      instructor: "{instructor}",
      category: "{category}",
      estimatedTime: "{time_str}",
      chapters: [
{chapters_js}
      ]
    }};

    let currentChapterIndex = 0;

    // Initialize page
    function initializePage() {{
      loadChaptersList();
      loadModuleInfo();
      loadNavigationLinks();
      if (moduleData.chapters.length > 0) {{
        loadChapter(0);
      }}
    }}

    // Load navigation links for this course's modules
    function loadNavigationLinks() {{
      const navContainer = document.getElementById('moduleNav');
      // Add links to other modules in this course
      // This would be populated from course data
      navContainer.innerHTML = '<a href="Lobby.html" class="module-nav-link">← Back to Lobby</a>';
    }}

    // Load chapters list
    function loadChaptersList() {{
      const chaptersList = document.getElementById('chaptersList');
      chaptersList.innerHTML = '';

      moduleData.chapters.forEach((chapter, index) => {{
        const chapterBtn = document.createElement('button');
        chapterBtn.className = 'chapter-item';
        if (chapter.completed) chapterBtn.classList.add('completed');
        if (currentChapterIndex === index) chapterBtn.classList.add('active');

        const chapterHeader = document.createElement('div');
        chapterHeader.className = 'chapter-item-header';

        const chapterNumber = document.createElement('div');
        chapterNumber.className = 'chapter-number';
        chapterNumber.textContent = index + 1;

        const chapterTitle = document.createElement('h4');
        chapterTitle.className = 'chapter-title';
        chapterTitle.textContent = chapter.title;

        chapterHeader.appendChild(chapterNumber);
        chapterHeader.appendChild(chapterTitle);

        const chapterDetails = document.createElement('div');
        chapterDetails.className = 'chapter-details';
        chapterDetails.innerHTML = `
          <span class="chapter-detail-item">⏱️ ${{chapter.duration}}</span>
          <span class="chapter-detail-item">🎬 Video</span>
          <span class="chapter-detail-item">${{chapter.completed ? '✓ Watched' : '○ Not watched'}}</span>
        `;

        chapterBtn.appendChild(chapterHeader);
        chapterBtn.appendChild(chapterDetails);
        chapterBtn.onclick = () => loadChapter(index);

        chaptersList.appendChild(chapterBtn);
      }});
    }}

    // Load chapter content
    function loadChapter(index) {{
      if (index < 0 || index >= moduleData.chapters.length) return;

      currentChapterIndex = index;
      const chapter = moduleData.chapters[index];

      document.getElementById('chapterTitle').textContent = chapter.title;
      document.getElementById('chapterDuration').textContent = '⏱️ Duration: ' + chapter.duration;
      document.getElementById('chapterType').textContent = '🎬 Type: Video';

      // Load video
      const videoContainer = document.getElementById('videoContainer');
      if (chapter.youtubeUrl) {{
        videoContainer.innerHTML = `<iframe class="video-iframe" src="${{chapter.youtubeUrl}}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>`;
      }} else {{
        videoContainer.innerHTML = '<div style="width: 100%; height: 500px; background: rgba(255,255,255,0.05); border-radius: 8px; display: flex; align-items: center; justify-content: center; border: 1px solid rgba(255,255,255,0.1); color: var(--muted-text);">No video available</div>';
      }}

      document.getElementById('chapterDescription').innerHTML = `
        <p><strong>Overview:</strong> ${{chapter.description}}</p>
        <p>${{chapter.content}}</p>
      `;

      document.getElementById('chapterIndicator').textContent = `Chapter ${{index + 1}} of ${{moduleData.chapters.length}}`;

      // Update navigation buttons
      document.getElementById('prevBtn').disabled = index === 0;
      document.getElementById('nextBtn').disabled = index === moduleData.chapters.length - 1;

      // Update complete button
      const completeBtn = document.getElementById('completeBtn');
      completeBtn.textContent = chapter.completed ? '✓ Chapter Completed' : '✓ Mark Chapter Complete';
      completeBtn.classList.toggle('completed', chapter.completed);

      // Load resources
      if (chapter.resources && chapter.resources.length > 0) {{
        const resourcesList = document.getElementById('resourcesList');
        resourcesList.innerHTML = chapter.resources.map(resource => `
          <div class="resource-item">
            <div class="resource-info">
              <span class="resource-icon">📄</span>
              <div class="resource-details">
                <div class="resource-name">${{resource.name}}</div>
                <div class="resource-size">${{resource.size}}</div>
              </div>
            </div>
            <button class="btn-download" onclick="downloadResource('${{resource.name}}')">⬇ Download</button>
          </div>
        `).join('');
      }}

      loadChaptersList();
      updateProgress();
    }}

    // Complete chapter
    function completeChapter() {{
      const chapter = moduleData.chapters[currentChapterIndex];
      chapter.completed = !chapter.completed;

      if (chapter.completed) {{
        alert('Chapter marked as complete! 🎉');
      }}

      loadChaptersList();
      loadChapter(currentChapterIndex);
    }}

    // Navigation
    function previousChapter() {{
      if (currentChapterIndex > 0) {{
        loadChapter(currentChapterIndex - 1);
      }}
    }}

    function nextChapter() {{
      if (currentChapterIndex < moduleData.chapters.length - 1) {{
        loadChapter(currentChapterIndex + 1);
      }}
    }}

    // Toggle resources
    function toggleResources() {{
      const resourcesSection = document.getElementById('resourcesSection');
      resourcesSection.style.display = resourcesSection.style.display === 'none' ? 'block' : 'none';
    }}

    // Download resource
    function downloadResource(resourceName) {{
      alert('Downloading: ' + resourceName);
    }}

    // Update progress
    function updateProgress() {{
      const completed = moduleData.chapters.filter(c => c.completed).length;
      const total = moduleData.chapters.length;
      const percentage = Math.round((completed / total) * 100);

      document.getElementById('completedChapters').textContent = completed;
      document.getElementById('moduleProgress').textContent = percentage + '%';
    }}

    // Load module info
    function loadModuleInfo() {{
      document.getElementById('instructorName').textContent = moduleData.instructor;
      document.getElementById('totalChapters').textContent = moduleData.chapters.length;
      document.getElementById('estimatedTime').textContent = moduleData.estimatedTime;
    }}

    // Navigation function
    function goToAccount(event) {{
      event.preventDefault();
      const userId = localStorage.getItem('userId');
      if (userId) {{
        window.location.href = 'Account.html';
      }} else {{
        window.location.href = 'Login.html';
      }}
    }}

    window.addEventListener('DOMContentLoaded', initializePage);
  </script>
</body>
</html>"""
    return html

# Generate all modules
frontend_path = Path(r"C:\Users\Adrian Jose Mendez\Documents\Personal Project\Frontend")

print("Generating module pages...")
count = 0

for course_id, course_data in courseDatabase.items():
    for module_id, module_data in enumerate(course_data["modules"], 1):
        filename = f"Module-{course_id}-{module_id}.html"
        filepath = frontend_path / filename
        
        html = generate_module_html(course_id, module_id, course_data, module_data)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        
        count += 1
        print(f"✓ Created {filename}")

print(f"\n✅ Generated {count} module pages!")
