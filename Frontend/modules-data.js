// Complete Course Database - All 17 Courses with Modules
// This file provides data for the Module Viewer page
// Additional courses can be added following the same structure

// NOTE: Due to file size constraints, all 17 courses are not included here.
// For a complete implementation with all courses, extract courseDatabase from Course-Content.html
// and include it globally, then use the Module Viewer with course and module IDs as URL parameters.

// Helper function to get course data
function getCourseData(courseId) {
  if (typeof window.courseDatabase !== 'undefined') {
    return window.courseDatabase[courseId];
  }
  return courseDatabase[courseId];
}

// Helper function to get module data
function getModuleData(courseId, moduleId) {
  const course = getCourseData(courseId);
  if (!course) return null;
  return course.modules.find(m => m.id === moduleId);
}

// Sample courses for demonstration
const courseDatabase = {
  1: {
    id: 1,
    title: "Investment Basics 101",
    instructor: "John Smith",
    totalLessons: 10,
    estimatedTime: "3 weeks",
    category: "beginner",
    modules: [
      {id: 1, title: "Module 1: Why Invest?", description: "Learn why investing is important", lessons: [{id: 1, title: "The Power of Investing & Compound Interest", duration: "8 min", type: "video", completed: false, description: "Discover why investing matters.", content: "Investing is the process of putting your money into financial assets...", youtubeUrl: "https://www.youtube.com/embed/xDqfM0fH2Fs", resources: []}, {id: 2, title: "Risk vs Reward", duration: "10 min", type: "video", completed: false, description: "Learn risk-return relationship.", content: "Every investment carries risk...", youtubeUrl: "https://www.youtube.com/embed/T8D8L3nshqY", resources: []}, {id: 3, title: "Types of Investments", duration: "12 min", type: "video", completed: false, description: "Overview of asset classes.", content: "Explore stocks, bonds, real estate...", youtubeUrl: "https://www.youtube.com/embed/XdFFF9w-cYo", resources: []}, {id: 4, title: "Getting Started", duration: "9 min", type: "video", completed: false, description: "First investment steps.", content: "Learn about brokerage accounts...", youtubeUrl: "https://www.youtube.com/embed/v9D7HLoI_e8", resources: []}]},
      {id: 2, title: "Module 2: Building Your Foundation", description: "Create investment foundation", lessons: [{id: 5, title: "Creating Your Investment Plan", duration: "11 min", type: "video", completed: false, description: "Develop investment strategy.", content: "Create solid investment plan...", youtubeUrl: "https://www.youtube.com/embed/oTKp4M9YlJ0", resources: []}, {id: 6, title: "Emergency Fund", duration: "8 min", type: "video", completed: false, description: "Importance of emergency fund.", content: "Establish 3-6 month fund...", youtubeUrl: "https://www.youtube.com/embed/7dH0RKB2wAQ", resources: []}, {id: 7, title: "The Importance of Diversification", duration: "10 min", type: "video", completed: false, description: "Spread investments.", content: "Learn the basket principle...", youtubeUrl: "https://www.youtube.com/embed/m4OQYu6EkEw", resources: []}]},
      {id: 3, title: "Module 3: Your First Investment", description: "Take first investment step", lessons: [{id: 8, title: "Index Funds & ETFs", duration: "11 min", type: "video", completed: false, description: "Low-cost investment vehicles.", content: "Discover index funds...", youtubeUrl: "https://www.youtube.com/embed/u2MKXqzqKdI", resources: []}, {id: 9, title: "Dollar-Cost Averaging", duration: "9 min", type: "video", completed: false, description: "Regular investment strategy.", content: "Learn DCA approach...", youtubeUrl: "https://www.youtube.com/embed/7_LqjrDdP5o", resources: []}, {id: 10, title: "Tracking Progress", duration: "7 min", type: "video", completed: false, description: "Monitor performance.", content: "Track investments...", youtubeUrl: "https://www.youtube.com/embed/Kz3jfTVJWzU", resources: []}]}
    ]
  },
  2: {
    id: 2,
    title: "Stock Market Fundamentals",
    instructor: "Sarah Johnson",
    totalLessons: 8,
    estimatedTime: "2 weeks",
    category: "beginner",
    modules: [
      {id: 1, title: "Module 1: Understanding Stocks", description: "How stocks work", lessons: [{id: 1, title: "What is a Stock?", duration: "9 min", type: "video", completed: false, description: "Stock representation.", content: "A stock represents ownership...", youtubeUrl: "https://www.youtube.com/embed/p7HKvqRI_Bo", resources: []}, {id: 2, title: "How Stock Markets Work", duration: "11 min", type: "video", completed: false, description: "Market mechanics.", content: "Learn how exchanges work...", youtubeUrl: "https://www.youtube.com/embed/EWz3ZyJNPWo", resources: []}, {id: 3, title: "Major Stock Exchanges", duration: "8 min", type: "video", completed: false, description: "NYSE, NASDAQ overview.", content: "Learn about major exchanges...", youtubeUrl: "https://www.youtube.com/embed/DFuL-bFQ7f4", resources: []}]},
      {id: 2, title: "Module 2: Reading Stock Data", description: "Understand market data", lessons: [{id: 4, title: "Reading Stock Quotes", duration: "10 min", type: "video", completed: false, description: "Quote interpretation.", content: "Learn to read quotes...", youtubeUrl: "https://www.youtube.com/embed/WBZdGMhZqe4", resources: []}, {id: 5, title: "Stock Charts", duration: "12 min", type: "video", completed: false, description: "Chart interpretation.", content: "Understand charts...", youtubeUrl: "https://www.youtube.com/embed/gl6aqXZFao8", resources: []}]},
      {id: 3, title: "Module 3: Your First Stock Purchase", description: "Make first investment", lessons: [{id: 6, title: "How to Buy Your First Stock", duration: "9 min", type: "video", completed: false, description: "Purchasing guide.", content: "Step-by-step purchase...", youtubeUrl: "https://www.youtube.com/embed/HfI1XP1mPrA", resources: []}, {id: 7, title: "Market Terminology", duration: "10 min", type: "video", completed: false, description: "Learn key terms.", content: "Essential vocabulary...", youtubeUrl: "https://www.youtube.com/embed/JT16zw0K-Ts", resources: []}, {id: 8, title: "Avoiding Mistakes", duration: "8 min", type: "video", completed: false, description: "Common beginner mistakes.", content: "Learn to avoid pitfalls...", youtubeUrl: "https://www.youtube.com/embed/j2rZ7g3c8P4", resources: []}]}
    ]
  }
};
