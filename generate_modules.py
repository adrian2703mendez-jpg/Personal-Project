import json
import os
from pathlib import Path

# Path to frontend folder
frontend_path = Path(r"C:\Users\Adrian Jose Mendez\Documents\Personal Project\Frontend")

# Complete course database extracted from Course-Content.html
courseDatabase = {
    1: {
        "id": 1,
        "title": "Investment Basics 101",
        "instructor": "John Smith",
        "totalLessons": 10,
        "estimatedTime": "3 weeks",
        "category": "beginner",
        "modules": [
            {
                "id": 1,
                "title": "Module 1: Why Invest?",
                "lessons": [
                    {"id": 1, "title": "The Power of Investing & Compound Interest", "duration": "8 min", "type": "video", "completed": False, "description": "Discover why investing matters and how compound interest can grow your wealth exponentially over time.", "content": "Investing is the process of putting your money into financial assets with the goal of growing your wealth. Learn about the power of compound interest, often called the 'eighth wonder of the world', and how starting early can dramatically impact your financial future. Understand the difference between saving and investing, and why both are important.", "youtubeUrl": "https://www.youtube.com/embed/xDqfM0fH2Fs", "resources": [{"name": "Compound Interest Calculator.xlsx", "size": "1.2 MB"}, {"name": "Investment Timeline Guide.pdf", "size": "2.1 MB"}]},
                    {"id": 2, "title": "Risk vs Reward: Understanding Investment Risk", "duration": "10 min", "type": "video", "completed": False, "description": "Learn the fundamental relationship between investment risk and potential rewards.", "content": "Every investment carries some level of risk. This lesson explores the risk-reward spectrum, from savings accounts (low risk, low return) to stocks (higher risk, potentially higher return). Understand your risk tolerance and how it should influence your investment decisions.", "youtubeUrl": "https://www.youtube.com/embed/T8D8L3nshqY", "resources": [{"name": "Risk Assessment Questionnaire.pdf", "size": "856 KB"}]},
                    {"id": 3, "title": "Types of Investments: Stocks, Bonds & More", "duration": "12 min", "type": "video", "completed": False, "description": "Overview of the main asset classes available to investors.", "content": "Explore the fundamental asset classes: stocks (ownership), bonds (lending), real estate, commodities, and alternatives. Learn the characteristics, risks, and benefits of each type of investment.", "youtubeUrl": "https://www.youtube.com/embed/XdFFF9w-cYo", "resources": [{"name": "Asset Classes Comparison Chart.pdf", "size": "1.8 MB"}]},
                    {"id": 4, "title": "Getting Started: First Steps to Investing", "duration": "9 min", "type": "video", "completed": False, "description": "Practical steps to open your first investment account and make your first investment.", "content": "Learn about brokerage accounts, investment platforms, and how to get started. Understand account types like taxable accounts, IRAs, and 401(k)s. Find out what documentation you'll need and how to fund your account.", "youtubeUrl": "https://www.youtube.com/embed/v9D7HLoI_e8", "resources": []}
                ]
            },
            {
                "id": 2,
                "title": "Module 2: Building Your Foundation",
                "lessons": [
                    {"id": 5, "title": "Creating Your Investment Plan", "duration": "11 min", "type": "video", "completed": False, "description": "Develop a personalized investment strategy based on your goals.", "content": "Create a solid investment plan by setting clear goals, determining your time horizon, and assessing your risk tolerance. Learn to differentiate between short-term and long-term goals, and how to allocate investments accordingly.", "youtubeUrl": "https://www.youtube.com/embed/oTKp4M9YlJ0", "resources": [{"name": "Investment Plan Template.xlsx", "size": "945 KB"}]},
                    {"id": 6, "title": "Emergency Fund & Starting Capital", "duration": "8 min", "type": "video", "completed": False, "description": "Why you need an emergency fund before investing.", "content": "Learn the importance of establishing a 3-6 month emergency fund before investing. Understand how much capital you should start with and strategies for consistent investing through dollar-cost averaging.", "youtubeUrl": "https://www.youtube.com/embed/7dH0RKB2wAQ", "resources": []},
                    {"id": 7, "title": "The Importance of Diversification", "duration": "10 min", "type": "video", "completed": False, "description": "Spread your investments to reduce risk.", "content": "Learn the core principle of 'not putting all eggs in one basket'. Understand how diversification across asset classes, sectors, and geographies can reduce portfolio risk while maintaining growth potential.", "youtubeUrl": "https://www.youtube.com/embed/m4OQYu6EkEw", "resources": [{"name": "Diversification Strategy Guide.pdf", "size": "2.3 MB"}]}
                ]
            },
            {
                "id": 3,
                "title": "Module 3: Your First Investment",
                "lessons": [
                    {"id": 8, "title": "Index Funds & ETFs for Beginners", "duration": "11 min", "type": "video", "completed": False, "description": "Start with low-cost, diversified investment vehicles.", "content": "Discover index funds and ETFs - two of the best ways to start investing. Learn how they provide instant diversification, low fees, and historically strong returns for long-term investors.", "youtubeUrl": "https://www.youtube.com/embed/u2MKXqzqKdI", "resources": [{"name": "Index Funds vs ETFs Comparison.pdf", "size": "1.6 MB"}, {"name": "Top Index Funds to Consider.xlsx", "size": "1.1 MB"}]},
                    {"id": 9, "title": "Dollar-Cost Averaging Strategy", "duration": "9 min", "type": "video", "completed": False, "description": "Invest regularly to smooth out market volatility.", "content": "Learn dollar-cost averaging (DCA), a strategy where you invest fixed amounts at regular intervals. This approach reduces market timing risk and builds discipline into your investing habits.", "youtubeUrl": "https://www.youtube.com/embed/7_LqjrDdP5o", "resources": [{"name": "DCA Calculator Tool.xlsx", "size": "892 KB"}]},
                    {"id": 10, "title": "Tracking Progress & Staying Motivated", "duration": "7 min", "type": "video", "completed": False, "description": "Monitor your investments and maintain long-term perspective.", "content": "Understand how to track your portfolio performance, set realistic expectations, and stay motivated during market downturns. Learn the importance of avoiding emotional decisions and sticking to your investment plan.", "youtubeUrl": "https://www.youtube.com/embed/Kz3jfTVJWzU", "resources": []}
                ]
            }
        ]
    }
}

def generate_chapter_items_html(lessons):
    """Generate HTML for chapter list items"""
    html_parts = []
    for idx, lesson in enumerate(lessons):
        html_parts.append(f'''            <button class="chapter-item" onclick="loadChapter({idx})">
              <div class="chapter-item-header">
                <div class="chapter-number">{idx + 1}</div>
                <h4 class="chapter-title">{lesson['title']}</h4>
              </div>
              <div class="chapter-details">
                <span class="chapter-detail-item">⏱️ {lesson['duration']}</span>
                <span class="chapter-detail-item">🎬 Video</span>
                <span class="chapter-detail-item">○ Not watched</span>
              </div>
            </button>''')
    return '\n'.join(html_parts)

def generate_chapter_data_script(lessons):
    """Generate JavaScript for chapter data"""
    chapters_data = []
    for lesson in lessons:
        resources_json = json.dumps(lesson.get('resources', []))
        chapter_data = f'''        {{
          id: {lesson['id']},
          title: "{lesson['title'].replace('"', '\\"')}",
          duration: "{lesson['duration']}",
          type: "video",
          completed: false,
          description: "{lesson['description'].replace('"', '\\"')}",
          content: "{lesson['content'].replace('"', '\\"')}",
          youtubeUrl: "{lesson['youtubeUrl']}",
          resources: {resources_json}
        }}'''
        chapters_data.append(chapter_data)
    return ',\n'.join(chapters_data)

def calculate_total_duration(lessons):
    """Calculate total duration from lessons"""
    total_minutes = 0
    for lesson in lessons:
        duration_str = lesson['duration'].split()[0]
        try:
            total_minutes += int(duration_str)
        except:
            pass
    hours = total_minutes // 60
    minutes = total_minutes % 60
    if hours > 0:
        return f"{hours}h {minutes}m" if minutes > 0 else f"{hours}h"
    return f"{minutes} mins"

def generate_resources_html(lessons):
    """Generate HTML for resources based on lessons that have them"""
    all_resources = []
    for lesson in lessons:
        if lesson.get('resources'):
            all_resources.extend(lesson['resources'])
    
    if not all_resources:
        return "            <!-- No resources available -->"
    
    html_parts = []
    for resource in all_resources:
        html_parts.append(f'''            <div class="resource-item">
              <div class="resource-info">
                <span class="resource-icon">📄</span>
                <div class="resource-details">
                  <div class="resource-name">{resource['name']}</div>
                  <div class="resource-size">{resource['size']}</div>
                </div>
              </div>
              <button class="btn-download" onclick="downloadResource('{resource['name']}')">⬇ Download</button>
            </div>''')
    return '\n'.join(html_parts)

print("Module Page Generator Started")
print(f"Generating module pages in: {frontend_path}")

# For now, just print the structure to verify
for course_id, course in courseDatabase.items():
    print(f"\n{course['title']} ({course['category']})")
    for module in course['modules']:
        total_duration = calculate_total_duration(module['lessons'])
        print(f"  - {module['title']}: {len(module['lessons'])} chapters, {total_duration}")

print("\nScript ready to generate module HTML files")
