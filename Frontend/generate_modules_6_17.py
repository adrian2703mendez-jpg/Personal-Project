#!/usr/bin/env python3
"""
Advanced Module Generator - Creates all remaining 36 module pages for courses 6-17
Run: python generate_modules_6_17.py
"""

def generate_module_html(course_id, module_id, course_name, module_title, instructor, category, num_chapters):
    """Generate a module HTML file with placeholder content."""
    
    category_class = "intermediate" if category == "intermediate" else "advanced"
    category_display = category.capitalize()
    
    # Create dynamic chapter content based on course theme
    chapters_data = []
    chapter_titles = {
        6: ["Chart Patterns", "Support & Resistance", "Moving Averages"],  # Technical Analysis
        7: ["Income Statements", "Balance Sheets", "Cash Flow Analysis"],  # Fundamental Analysis
        8: ["Asset Allocation", "Rebalancing", "Risk Management"],  # Portfolio Construction
        9: ["Call Options", "Put Options", "Spreads & Strategies"],  # Options Trading
        10: ["Blockchain Basics", "Bitcoin & Ethereum", "Crypto Wallets"],  # Cryptocurrency
        11: ["Tax Brackets", "Tax-Advantaged Accounts", "Capital Gains"],  # Tax-Efficient
        12: ["Python for Trading", "Strategy Development", "Backtesting"],  # Algorithmic Trading
        13: ["Futures Contracts", "Hedging Strategies", "Risk Limits"],  # Derivatives
        14: ["Statistical Analysis", "Regression Models", "Factor Analysis"],  # Quantitative
        15: ["Economic Cycles", "Interest Rates", "Inflation"],  # Macro Economic
        16: ["Fund Structure", "Due Diligence", "Returns Analysis"],  # Private Equity
        17: ["Business Plan", "Risk Management", "Growth Strategies"]  # Building Investment Firm
    }
    
    durations = ["8 min", "10 min", "9 min"]
    chapter_count = min(3, num_chapters) if num_chapters else 3
    
    chapters_html = "[\n"
    for i in range(chapter_count):
        chapter_num = i + 1
        title = chapter_titles.get(course_id, ["Chapter " + str(chapter_num)] * 3)[i]
        duration = durations[i % 3]
        
        chapters_html += f'''        {{
          id: {chapter_num},
          title: "{title}",
          duration: "{duration}",
          type: "video",
          completed: false,
          description: "Learn key concepts and applications in this module.",
          content: "Explore fundamental and advanced concepts related to {title.lower()}. Understand practical applications and best practices. This chapter covers essential techniques you'll use in real-world investing scenarios.",
          youtubeUrl: "https://www.youtube.com/embed/dQw4w9WgXcQ",
          resources: [{{"name": "{title}.pdf", "size": "1.8 MB"}}]
        }}'''
        if i < chapter_count - 1:
            chapters_html += ",\n"
        else:
            chapters_html += "\n"
    chapters_html += "      ]"
    
    total_duration = chapter_count * 9
    
    html = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Module {module_id}: {module_title} - {course_name}</title>
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

  <main class="module-page {category_class}">
    <div class="module-container">
      <aside class="module-sidebar">
        <div class="module-sidebar-header">
          <h3>Navigation</h3>
          <div class="module-category-badge">{category_display}</div>
        </div>
        <div class="module-sidebar-body">
          <a href="Module-{course_id}-1.html" class="module-nav-link{' active' if module_id == 1 else ''}">Module 1</a>
          <a href="Module-{course_id}-2.html" class="module-nav-link{' active' if module_id == 2 else ''}">Module 2</a>
          <a href="Module-{course_id}-3.html" class="module-nav-link{' active' if module_id == 3 else ''}">Module 3</a>
          <hr style="border: none; border-top: 1px solid rgba(255,255,255,0.1); margin: 12px 0;">
          <a href="Courses.html" class="module-nav-link">← All Courses</a>
        </div>
        <a href="Lobby.html" class="back-button">
          <span>🏠</span>
          <span>Back to Lobby</span>
        </a>
      </aside>

      <section class="module-main">
        <div class="module-header">
          <div class="module-header-content">
            <h1>Module {module_id}: {module_title}</h1>
            <div class="module-header-meta">
              <span>📚 {course_name}</span>
              <span>👨‍🏫 {instructor}</span>
              <span>⏱️ {total_duration} mins</span>
              <span>📊 {chapter_count} Chapters</span>
            </div>
          </div>
        </div>

        <div class="module-chapters">
          <div class="chapters-header">
            <h2>Chapters</h2>
            <span class="chapters-count">{chapter_count} chapters</span>
          </div>
          <div class="chapters-list" id="chaptersList"></div>
        </div>

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

          <section id="resourcesSection" class="chapter-resources" style="display: none;">
            <h3>📥 Resources for this Chapter</h3>
            <div class="resources-list" id="resourcesList"></div>
          </section>

          <div class="chapter-navigation">
            <button class="btn-nav" id="prevBtn" onclick="previousChapter()" disabled>← Previous</button>
            <div class="chapter-indicator" id="chapterIndicator">Chapter 0 of 0</div>
            <button class="btn-nav" id="nextBtn" onclick="nextChapter()" disabled>Next →</button>
          </div>

          <div class="module-actions">
            <button class="btn-primary" id="completeBtn" onclick="completeChapter()">✓ Mark Chapter Complete</button>
            <button class="btn-secondary" onclick="toggleResources()">📥 View Resources</button>
            <a href="Assessments.html" class="btn-secondary" style="text-decoration: none;">🧪 Take Quiz</a>
          </div>
        </div>
      </section>

      <aside class="module-info-panel">
        <div class="info-card">
          <h3>📚 Module Info</h3>
          <div class="info-item">
            <label>Course</label>
            <p>{course_name}</p>
          </div>
          <div class="info-item">
            <label>Instructor</label>
            <p>{instructor}</p>
          </div>
          <div class="info-item">
            <label>Total Chapters</label>
            <p>{chapter_count}</p>
          </div>
          <div class="info-item">
            <label>Estimated Time</label>
            <p>{total_duration} minutes</p>
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
            <li>Master the fundamentals</li>
            <li>Practice consistently</li>
            <li>Review complex topics</li>
            <li>Apply concepts to trading</li>
          </ul>
        </div>
      </aside>
    </div>
  </main>

  <script>
    const moduleData = {{
      courseId: {course_id},
      courseName: "{course_name}",
      moduleId: {module_id},
      moduleName: "Module {module_id}: {module_title}",
      instructor: "{instructor}",
      category: "{category_class}",
      estimatedTime: "{total_duration} mins",
      chapters: {chapters_html}
    }};

    let currentChapterIndex = 0;

    function initializePage() {{
      loadChaptersList();
      if (moduleData.chapters.length > 0) loadChapter(0);
    }}

    function loadChaptersList() {{
      const chaptersList = document.getElementById('chaptersList');
      chaptersList.innerHTML = '';

      moduleData.chapters.forEach((chapter, index) => {{
        const btn = document.createElement('button');
        btn.className = 'chapter-item';
        if (chapter.completed) btn.classList.add('completed');
        if (currentChapterIndex === index) btn.classList.add('active');

        const header = document.createElement('div');
        header.className = 'chapter-item-header';

        const num = document.createElement('div');
        num.className = 'chapter-number';
        num.textContent = index + 1;

        const title = document.createElement('h4');
        title.className = 'chapter-title';
        title.textContent = chapter.title;

        header.appendChild(num);
        header.appendChild(title);

        const details = document.createElement('div');
        details.className = 'chapter-details';
        details.innerHTML = `
          <span class="chapter-detail-item">⏱️ ${{chapter.duration}}</span>
          <span class="chapter-detail-item">🎬 Video</span>
          <span class="chapter-detail-item">${{chapter.completed ? '✓ Watched' : '○ Not watched'}}</span>
        `;

        btn.appendChild(header);
        btn.appendChild(details);
        btn.onclick = () => loadChapter(index);

        chaptersList.appendChild(btn);
      }});
    }}

    function loadChapter(index) {{
      if (index < 0 || index >= moduleData.chapters.length) return;

      currentChapterIndex = index;
      const chapter = moduleData.chapters[index];

      document.getElementById('chapterTitle').textContent = chapter.title;
      document.getElementById('chapterDuration').textContent = '⏱️ Duration: ' + chapter.duration;
      document.getElementById('chapterType').textContent = '🎬 Type: Video';

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

      document.getElementById('prevBtn').disabled = index === 0;
      document.getElementById('nextBtn').disabled = index === moduleData.chapters.length - 1;

      const completeBtn = document.getElementById('completeBtn');
      completeBtn.textContent = chapter.completed ? '✓ Chapter Completed' : '✓ Mark Chapter Complete';
      completeBtn.classList.toggle('completed', chapter.completed);

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

    function completeChapter() {{
      const chapter = moduleData.chapters[currentChapterIndex];
      chapter.completed = !chapter.completed;
      if (chapter.completed) alert('Chapter marked as complete! 🎉');
      loadChaptersList();
      loadChapter(currentChapterIndex);
    }}

    function previousChapter() {{
      if (currentChapterIndex > 0) loadChapter(currentChapterIndex - 1);
    }}

    function nextChapter() {{
      if (currentChapterIndex < moduleData.chapters.length - 1) loadChapter(currentChapterIndex + 1);
    }}

    function toggleResources() {{
      const resourcesSection = document.getElementById('resourcesSection');
      resourcesSection.style.display = resourcesSection.style.display === 'none' ? 'block' : 'none';
    }}

    function downloadResource(resourceName) {{
      alert('Downloading: ' + resourceName);
    }}

    function updateProgress() {{
      const completed = moduleData.chapters.filter(c => c.completed).length;
      const total = moduleData.chapters.length;
      const percentage = Math.round((completed / total) * 100);
      document.getElementById('completedChapters').textContent = completed;
      document.getElementById('moduleProgress').textContent = percentage + '%';
    }}

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
</html>'''
    
    return html

# Course data for 6-17
COURSES_6_17 = {
    6: {"name": "Technical Analysis Fundamentals", "instructor": "Kevin Zhang", "category": "intermediate"},
    7: {"name": "Fundamental Analysis Deep Dive", "instructor": "Patricia Adams", "category": "intermediate"},
    8: {"name": "Portfolio Construction Methods", "instructor": "James Murphy", "category": "intermediate"},
    9: {"name": "Options Trading Strategies", "instructor": "Lisa Thompson", "category": "intermediate"},
    10: {"name": "Cryptocurrency Investing", "instructor": "Marcus Lee", "category": "intermediate"},
    11: {"name": "Tax-Efficient Investing", "instructor": "Susan Green", "category": "intermediate"},
    12: {"name": "Algorithmic Trading Basics", "instructor": "Dr. Henry Chen", "category": "advanced"},
    13: {"name": "Derivatives and Hedging", "instructor": "Victoria Stone", "category": "advanced"},
    14: {"name": "Quantitative Analysis", "instructor": "Dr. Nathan Brooks", "category": "advanced"},
    15: {"name": "Macro Economic Investing", "instructor": "Dr. Eleanor White", "category": "advanced"},
    16: {"name": "Private Equity and Venture Capital", "instructor": "Richard Foster", "category": "advanced"},
    17: {"name": "Building an Investment Firm", "instructor": "Margaret Clarke", "category": "advanced"}
}

def main():
    print("🔄 Advanced Module Generator - Creating modules for courses 6-17...")
    created = 0
    
    for course_id in range(6, 18):
        if course_id in COURSES_6_17:
            course = COURSES_6_17[course_id]
            name = course["name"]
            instructor = course["instructor"]
            category = course["category"]
            
            for module_id in range(1, 4):
                filename = f"Module-{course_id}-{module_id}.html"
                
                html = generate_module_html(
                    course_id, module_id,
                    name, f"Module {module_id}",
                    instructor, category, 3
                )
                
                try:
                    with open(filename, 'w', encoding='utf-8') as f:
                        f.write(html)
                    print(f"✅ Created {filename}")
                    created += 1
                except Exception as e:
                    print(f"❌ Error: {filename} - {e}")
    
    print(f"\n✨ Complete! Created {created} module files for courses 6-17.")
    print("📊 Summary:")
    print(f"  - Intermediate courses (6-11): 18 modules")
    print(f"  - Advanced courses (12-17): 18 modules")
    print("  - All 51 module files now ready!")
    print("  - Next: Delete old Course-Content.html, course.html, Classes.html")
    print("  - Then: Test Courses.html navigation")

if __name__ == '__main__':
    main()
