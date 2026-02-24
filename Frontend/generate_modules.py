#!/usr/bin/env python3
"""
Module Generator - Creates all 51 module HTML pages from course database
Run: python generate_all_modules.py
Output: Creates Module-X-Y.html files in the current directory
"""

import json
import os

# Complete course database extracted from Course-Content.html
COURSES_DATABASE = {
    1: {
        "name": "Investing Fundamentals",
        "instructor": "Michael Chen",
        "category": "beginner",
        "modules": {
            1: {
                "title": "Why Invest?",
                "chapters": [
                    {"num": 1, "title": "The Power of Compound Interest", "duration": "12 min", "description": "Learn how compound interest makes your money grow exponentially over time.", "content": "Albert Einstein called it the eighth wonder of the world. Compound interest is the concept of earning interest on your interest. Start with $1000 at 10% annual return: after 1 year you have $1100, after 2 years $1210 (not $1200), after 10 years $2594. By year 30, you have $17,449! This exponential growth is the foundation of wealth building. The earlier you start, the more time your money has to compound. Even small regular contributions grow dramatically over decades."},
                    {"num": 2, "title": "Investment Types and Asset Classes", "duration": "10 min", "description": "Overview of different investment vehicles: stocks, bonds, real estate, commodities.", "content": "Stocks represent ownership in companies. Bonds are loans you give to companies or governments. Real estate provides rental income and appreciation. Mutual funds bundle multiple investments. ETFs (Exchange-Traded Funds) are like mutual funds but trade like stocks. Each has different risk-reward profiles. Stocks offer higher growth potential but more volatility. Bonds provide steady income with lower risk. Diversifying across asset classes helps balance risk and return."},
                    {"num": 3, "title": "Risk vs Return Tradeoff", "duration": "9 min", "description": "Understanding how to balance investment risk with potential returns.", "content": "Higher potential returns come with higher risk. Bank savings are safe but earn ~0.5% annually. Bonds earn 3-5% with moderate risk. Stocks average 10% long-term but fluctuate daily. Some investors can handle volatility, others cannot. Your risk tolerance depends on your timeline (long = can handle more risk), financial obligations, and personality. Young investors can take more risk since they have decades to recover from losses. Retirees should be more conservative. Diversification reduces risk without sacrificing returns."},
                    {"num": 4, "title": "Starting Your Investment Journey", "duration": "8 min", "description": "Practical steps to begin investing with confidence.", "content": "First, build an emergency fund (3-6 months expenses). Pay off high-interest debt. Open a brokerage account (Fidelity, Vanguard, Schwab). Fund it consistently, even with small amounts. Consider your investment timeline and goals. Choose investments matching your risk tolerance. Don't try to time the market - consistency matters more than timing. Dollar-cost averaging (investing fixed amounts regularly) smooths out market volatility. Review your portfolio annually. Make adjusting contributions as your situation changes."}
                ]
            },
            2: {
                "title": "Building Your Foundation",
                "chapters": [
                    {"num": 1, "title": "Your Financial Health Check", "duration": "8 min", "description": "Assess your current financial situation honestly.", "content": "List all income sources. Track all expenses for a month. Calculate your net worth (assets minus liabilities). Understand your cash flow. Identify spending patterns. Calculate your debt-to-income ratio. Know your credit score. Review your existing investments or none. Understand your insurance coverage. This honest assessment is crucial before building an investment strategy. Many people are surprised by where they actually spend money."},
                    {"num": 2, "title": "Setting SMART Investment Goals", "duration": "9 min", "description": "Create specific, measurable investment objectives.", "content": "SMART = Specific, Measurable, Achievable, Relevant, Time-bound. Not 'be rich' but 'have $100k by age 40'. Not 'invest in stocks' but 'build $5000 emergency fund in 6 months'. Goals might include: retirement savings, down payment for home, college funding, or wealth building. Breaking big goals into smaller milestones helps maintain motivation. Review goals annually and adjust as circumstances change. Track progress monthly. Written goals are more likely to be achieved."},
                    {"num": 3, "title": "Building Your Emergency Fund", "duration": "8 min", "description": "Create a financial safety net before investing.", "content": "Emergency fund = 3-6 months of essential living expenses. Keep it in a high-yield savings account (currently 4-5% APY). This protects you from debt if job loss or medical crisis occurs. Many investors skip this and regret it. Once emergency fund is solid, you can invest more aggressively. High-yield savings accounts are FDIC insured up to $250k. They earn much more than regular savings (5-10x more). This is not an investment account but a safety net."},
                    {"num": 4, "title": "Creating Your Investment Budget", "duration": "5 min", "description": "Allocate funds for regular investing.", "content": "Calculate: (Income - Essential Expenses - Emergency Fund Savings - Debt Payments) = Available for Investing. Start with what you can afford consistently. Even $100/month compounds to significant wealth. Many brokers allow investments as small as $1. Set up automatic transfers for consistency. Pay yourself first - treat investing as non-negotiable expense. Increase amounts as income grows. This systematic approach builds wealth inevitably over time."}
                ]
            },
            3: {
                "title": "Your First Investment",
                "chapters": [
                    {"num": 1, "title": "Opening Your Investment Account", "duration": "9 min", "description": "Step-by-step guide to opening a brokerage account.", "content": "Choose a broker: Fidelity, Vanguard, Charles Schwab, Robinhood, or others. Compare fees - many have zero commission now. Provide personal info (name, SSN, address). Verify bank account for transfers. Choose account type (taxable, IRA, 401k). Confirm identity through online verification. Fund your account. Review account settings. Some brokers offer free stock for signup. Vanguard and Fidelity are popular for beginners due to low fees and educational resources."},
                    {"num": 2, "title": "Your First Stock or ETF Purchase", "duration": "9 min", "description": "Execute your first investment transaction.", "content": "Start with an ETF like VOO (Vanguard 500 Index) or VTSAX (Vanguard Total Stock Market). These provide instant diversification across 500+ companies. Easier than picking individual stocks. Place a buy order on your broker platform. Specify quantity and order type (market order = immediate execution at current price). Verify the order. You own shares in minutes! Consider making this automatic monthly. Keep records of purchase price and date for tax reporting."},
                    {"num": 3, "title": "Understanding Fees and Expenses", "duration": "8 min", "description": "Know what you're paying for your investments.", "content": "Expense ratio = annual fee as percentage of investment. Good index funds: 0.03-0.10% annually. Actively managed funds: 0.50-2%+ annually. Trading commissions: most brokers now $0. Advisory fees: 0.5-2% if using advisor. Hidden fees in some products. Over 30 years, a 1% fee difference costs tens of thousands. Always choose lowest-cost index funds for core holdings. Check fund factsheet for expense ratios. Higher fees don't mean better returns. Actually, they usually mean worse returns due to drag."}
                ]
            }
        }
    },
    2: {
        "name": "Stock Market Fundamentals",
        "instructor": "Sarah Johnson",
        "category": "beginner",
        "modules": {
            1: {"title": "Understanding Stocks", "chapters": [{"num": 1, "title": "What is a Stock?", "duration": "9 min", "description": "Learn what stocks represent and why companies issue them.", "content": "A stock represents a share of ownership in a company. When you buy stock, you become a part-owner in that business. Learn about common stock vs preferred stock, and understand how stock ownership gives you rights like voting on company matters and receiving dividends. Understanding the basics of stock ownership is essential before making your first investment."}, {"num": 2, "title": "How Stock Markets Work", "duration": "10 min", "description": "Understand the mechanics of stock market trading.", "content": "Learn how stock exchanges facilitate buying and selling. Understand bid-ask spreads - the difference between what buyers want to pay and what sellers want to receive. Learn about market makers who provide liquidity and how prices are determined through the constant interaction of supply and demand. The stock market is one of the most efficient price-discovery mechanisms in the world."}, {"num": 3, "title": "Major Stock Exchanges & Indices", "duration": "9 min", "description": "Explore NYSE, NASDAQ, and major stock indices.", "content": "Learn about the world's major stock exchanges like the New York Stock Exchange (NYSE) and NASDAQ. Understand important indices like the S&P 500 (tracks 500 large American companies), Dow Jones Industrial Average (30 blue-chip stocks), and NASDAQ Composite (technology-heavy). These indices serve as barometers for overall market health and are referenced constantly in financial news."}]},
            2: {"title": "Reading Stock Data", "chapters": [{"num": 1, "title": "Understanding Stock Quotes", "duration": "11 min", "description": "Learn how to read and interpret stock quotes.", "content": "Stock quotes contain important information: the opening price (price when trading begins), closing price (final price of the day), high and low prices for the day, trading volume (number of shares traded), and market capitalization (company's total value). The P/E ratio compares stock price to earnings. The 52-week high/low shows the stock's annual range. Understanding these metrics helps you make informed decisions about which stocks to buy."}, {"num": 2, "title": "Key Financial Metrics", "duration": "10 min", "description": "Master important stock valuation metrics.", "content": "Learn about Earnings Per Share (EPS) - the company's profit divided by shares outstanding. Understand P/E ratio (Price-to-Earnings) - lower can mean undervalued. Discover dividend yield - annual dividends as a percentage of stock price. Book value represents assets minus liabilities. ROE (Return on Equity) shows profitability for shareholders. These metrics help you compare stocks and identify good investment opportunities."}, {"num": 3, "title": "Using Stock Analysis Tools", "duration": "10 min", "description": "Explore popular platforms for stock analysis.", "content": "Learn to use financial websites like Yahoo Finance, Google Finance, and Bloomberg. Understand how to read stock charts with candlestick patterns. Discover technical analysis basics - support and resistance levels. Learn how to use screening tools to find stocks matching your criteria. Practice reading company earnings reports and SEC filings. These tools empower you to do research before investing."}]},
            3: {"title": "Your First Stock Purchase", "chapters": [{"num": 1, "title": "Finding Good Stocks to Buy", "duration": "10 min", "description": "Learn strategies for stock selection and research.", "content": "Look for companies with strong competitive advantages (moats). Study their financial statements - revenue growth, profit margins, debt levels. Read analyst reports and reviews. Consider the company's industry and growth prospects. Don't chase hot tips - do your research. Start with companies you understand and use. Understand why you're buying - growth, dividends, or value. Have a thesis for each investment. Write it down and revisit it periodically."}, {"num": 2, "title": "Executing Your First Trade", "duration": "8 min", "description": "Complete your first stock purchase with confidence.", "content": "Open your brokerage account (steps covered in earlier module). Research your target stock thoroughly. Determine position size - never put all money in one stock. Place order: use limit orders (specify price) for more control. Market orders execute immediately at current price. Verify order details before submitting. Most trades execute within minutes. You now own shares! Keep records for taxes. Consider if this is core holding or short-term trade."}, {"num": 3, "title": "Diversification Basics", "duration": "9 min", "description": "Understand why not to put all eggs in one basket.", "content": "Concentration risk = owning too few stocks. If one drops 50%, your portfolio drops 50%. With 20-30 different stocks, one bad performer barely affects you. Diversify across sectors: tech, healthcare, finance, energy, retail, etc. Diversify by company size: large-cap, mid-cap, small-cap. Consider bonds and other assets too. For beginners, index funds provide instant diversification. You get the stock market's performance without picking winners and losers yourself."}]}
        }
    },
    3: {
        "name": "Bonds and Fixed Income",
        "instructor": "David Smith",
        "category": "beginner",
        "modules": {
            1: {"title": "Understanding Bonds", "chapters": [{"num": 1, "title": "How Bonds Work", "duration": "10 min", "description": "Learn the mechanics of bond investing.", "content": "A bond is a loan you give. You lend $1000, issuer promises to pay interest (called coupon) and return principal. Most bonds pay interest semi-annually. Bond price varies inversely with interest rates. When rates rise, existing Bond prices fall (and vice versa). Duration = how sensitive bond is to rate changes. Longer duration = more price volatility. Bonds offer steady income safer than stocks but lower returns generally. Maturity dates range from 1-30+ years."}, {"num": 2, "title": "Types of Bonds", "duration": "9 min", "description": "Explore government, corporate, and other bond types.", "content": "Government bonds (Treasuries) backed by US government - very safe. Corporate bonds issued by companies - higher yield, more risk. Municipal bonds issued by states/cities - tax-free for some. I-Bonds adjust for inflation - good for inflation protection. Junk bonds (high-yield) offer high returns but high default risk. Bond funds offer diversification. Individual bonds offer known final amount if held to maturity. Different types suit different goals."}, {"num": 3, "title": "Bond Ratings and Risk", "duration": "8 min", "description": "Understand credit ratings and bond safety.", "content": "Credit agencies (S&P, Moody's) rate bond safety. AAA are safest, BBB is still investment-grade, below that is junk. Higher ratings = lower yields. Lower ratings = higher yields (compensation for risk). Default risk = issuer fails to pay. Check ratings before investing in corporate bonds. US Treasuries have no default risk. Diversifying across issuers and ratings reduces risk. Always check what you own."}]},
            2: {"title": "Building a Bond Portfolio", "chapters": [{"num": 1, "title": "Bond Allocation Strategies", "duration": "9 min", "description": "Determine appropriate bond allocation for your portfolio.", "content": "Common rule: invest your age percentage in bonds. Age 30 = 30% bonds, 70% stocks. Age 60 = 60% bonds, 40% stocks. As you near retirement, increase bond allocation for stability. Younger investors can focus on stocks. Bonds reduce volatility compared to all-stocks. Bonds provide income for living expenses in retirement. Mix different bond maturities (ladder) for regular income. Consider your risk tolerance, timeline, and financial goals."}, {"num": 2, "title": "Bond Funds vs Individual Bonds", "duration": "8 min", "description": "Compare different ways to own bonds.", "content": "Individual bonds: you know exact payoff, can hold to maturity, predictable income. Minimum usually $1000-5000 per bond. Bond funds: provide diversification with small amounts, professional management, easier to buy/sell. Fund prices fluctuate, you don't get fixed maturity. ETFs like BND, AGG offer low-cost diversification. For most investors, bond funds are easier and better. But individuals bonds work for buy-and-hold investors."}, {"num": 3, "title": "Target-Date Funds for Bonds", "duration": "8 min", "description": "Use target-date funds for automatic bond allocation.", "content": "Target-date funds automatically shift from stocks to bonds as you age. Fund named for your retirement year (e.g., VFIAX Target Retirement 2050). Automatically rebalances every year. Simple set-and-forget solution. Excellent for retirement accounts. Available from all major brokers. Low fees with index versions. No need to manually adjust allocation. Perfect for passive investors who want diversification without work."}]},
            3: {"title": "Advanced Bond Strategies", "chapters": [{"num": 1, "title": "Bond Laddering", "duration": "9 min", "description": "Create predictable income through bond ladders.", "content": "Buy bonds maturing in 1, 3, 5, 7, 10 years. As each matures, you get principal back to reinvest. Provides regular cash flow. Reduces interest rate risk. Simpler than reinvesting fully at once. Great for bond funds too - automatic diversification by maturity. Example: $5000 ladder has 5x $1000 bonds maturing each year. No guessing when rates are best."}, {"num": 2, "title": "Interest Rate Strategies", "duration": "8 min", "description": "Navigate changing interest rate environments.", "content": "Falling rates = good for bonds (prices rise). Rising rates = bad for bonds (prices fall). Don't try to time rates - impossible. If rates rise, bond prices fall but new bonds pay more. If rates fall and you're locked in, that's good. Long-term investors shouldn't worry about daily fluctuations. TIPS (Treasury Inflation-Protected) adjust for inflation automatically. I-Bonds also inflation-protected. In rising inflation, these outperform."}, {"num": 3, "title": "Tax-Efficient Bond Investing", "duration": "7 min", "description": "Minimize taxes on bond income.", "content": "Bond interest is taxed as ordinary income (up to 37%). Stock dividends often taxed lower (15-20%). Municipal bonds tax-free at federal level. Hold bonds in tax-deferred accounts (IRA, 401k) if possible. Keep taxable bonds in taxable accounts only if tax-advantaged accounts full. Bond funds have capital gains/losses. I-Bonds let you defer taxes until redemption. Tax planning varies by individual situation."}]}
        }
    },
    4: {
        "name": "Real Estate Investing Basics",
        "instructor": "Jennifer Martinez",
        "category": "beginner",
        "modules": {
            1: {"title": "Real Estate Fundamentals", "chapters": [{"num": 1, "title": "Why Invest in Real Estate", "duration": "10 min", "description": "Understand the appeal and benefits of real estate.", "content": "Real estate offers hedge against inflation. Properties naturally increase in value. Generates rental income (positive cash flow). Tax benefits like deductions for mortgage interest and depreciation. Leverage - control large asset with small down payment. Physical tangible asset you can see and improve. REITs provide real estate exposure without owning property. Diversifies portfolio beyond stocks and bonds."}, {"num": 2, "title": "Direct Ownership vs REITs", "duration": "9 min", "description": "Compare owning property directly to buying REIT shares.", "content": "Direct ownership: buy rental property or home for rent. You control the property, collect rent, do maintenance. Requires significant capital (down payment), time, and expertise. REITs (Real Estate Investment Trusts): bundled real estate investments. Trade like stocks, no direct property management. Liquid - sell anytime unlike actual property. Professionally managed. More accessible to most investors. Both can provide good returns and diversification."}, {"num": 3, "title": "Types of Real Estate Investments", "duration": "8 min", "description": "Explore residential, commercial, and industrial properties.", "content": "Residential: houses, apartments, condos. Popular for beginners. Demand always exists. Commercial: office buildings, retail spaces. Often higher returns but more complex. Industrial: warehouses, distribution centers. Growing due to e-commerce. Agricultural: farmland and timberland. REITs focused on specific types make selection easier. Diversify across types for balanced exposure."}]},
            2: {"title": "Buying Your First Rental Property", "chapters": [{"num": 1, "title": "Pre-Purchase Financial Planning", "duration": "8 min", "description": "Prepare finances before buying rental property.", "content": "Calculate if rental income covers expenses (mortgage, taxes, insurance, maintenance, vacancy). Aim for 1% rule: annual rent should be 1% of purchase price minimum. Calculate cash-on-cash return: annual profit divided by down payment. Save down payment (20-25% reduces risk, gets better rates). Build emergency fund for repairs (furnace, roof fail unexpectedly). Ensure good credit score (700+) for better financing."}, {"num": 2, "title": "Finding and Evaluating Properties", "duration": "9 min", "description": "Scout and analyze potential rental properties.", "content": "Location crucial - good neighborhoods attract better tenants. Growing areas better than declining. Check local rents - higher vacancy rates = avoid. Use MLS, zillow, or local agents. Calculate all expenses: property tax, insurance, maintenance (expect 1% of price annually), utilities if included, HOA, vacancy rate typically 5-10%."}, {"num": 3, "title": "Financing Your Property", "duration": "8 min", "description": "Secure a mortgage and negotiate terms.", "content": "Compare mortgage rates from multiple lenders. 30-year fixed is stable and predictable. 15-year builds equity faster but higher payments. Points (upfront fee for lower rate) - useful if keeping long-term. Property management - do it yourself (saves money) or hire professional. Rental income should cover all expenses plus provide profit."}]},
            3: {"title": "Real Estate Investment Trusts (REITs)", "chapters": [{"num": 1, "title": "Understanding REITs", "duration": "9 min", "description": "Learn how REITs provide real estate exposure.", "content": "REITs bundle real estate properties or mortgages into tradeable shares. Required to distribute 90% of taxable income as dividends. Trade on stock exchanges like regular stocks. Liquid - can sell anytime unlike property. Professional management. Expose to diversified real estate. Average dividend yields 3-5% higher than stocks. No property management work required."}, {"num": 2, "title": "Types and Sectors of REITs", "duration": "8 min", "description": "Explore different REIT categories and specializations.", "content": "Residential REITs - apartment buildings, single-family homes. Retail REITs - shopping centers, malls. Office REITs - office buildings. Industrial REITs - warehouses, logistics. Healthcare REITs - medical offices, nursing homes. Data center REITs - tech infrastructure. Different return profiles suit different goals."}, {"num": 3, "title": "REIT Investment Strategy", "duration": "8 min", "description": "Build REIT allocation into your portfolio.", "content": "REITs provide diversification and income. Typical allocation 5-15% of portfolio depending on goals. Index REITs (VNQ, SCHH, XLRE) offer low-cost broad exposure. Sector-specific REITs for targeted plays. High dividends mean significant income component. Tax-advantaged accounts preferred due to dividend nature. Rebalance annually to maintain allocation."}]}
        }
    },
    5: {
        "name": "Dividend Investing",
        "instructor": "Robert Wilson",
        "category": "beginner",
        "modules": {
            1: {"title": "Dividends Explained", "chapters": [{"num": 1, "title": "What Are Dividends", "duration": "8 min", "description": "Understand dividend payments and their sources.", "content": "Dividends are portions of company profits paid to shareholders. Some companies reinvest all earnings, others pay dividends quarterly. Cash dividends most common - direct payment per share. Stock dividends - receiving additional shares instead of cash. Blue-chip companies typically pay consistent dividends. Startups rarely pay dividends, preferring reinvestment. Dividends provide income while holding for growth."}, {"num": 2, "title": "Dividend Yields and Payout Ratios", "duration": "9 min", "description": "Calculate dividend yields and assess sustainability.", "content": "Dividend yield = annual dividend divided by stock price. 3-4% typical for mature companies. Higher yields may indicate undervaluation or unsustainable dividend. Payout ratio = dividends divided by earnings. <60% sustainable, >80% risky. Growing dividend = company confident in future. Dividend cuts hurt stock price badly. Hold winners with growing dividends for increasing income."}, {"num": 3, "title": "How Dividend Payments Work", "duration": "7 min", "description": "Learn the mechanics of dividend payment timing.", "content": "Ex-dividend date: last day to own stock and receive dividend. Must own stock before this date. Payment date: when you actually receive the money. Regular dividends usually quarterly. Special dividends occasional extra payments. Quarterly dividend of $0.40 per share = $4 per share annually. 100 shares = $400 annual income. Track ex-dividend dates if trying to time purchases for upcoming payments."}]},
            2: {"title": "Dividend Growth Investing", "chapters": [{"num": 1, "title": "Finding Dividend Aristocrats", "duration": "9 min", "description": "Identify companies with reliable, growing dividends.", "content": "Dividend Aristocrats: 25+ consecutive years of increasing dividends. Indicate financial strength and consistency. Examples: 3M, Coca-Cola, Johnson & Johnson, Procter & Gamble. These stocks typically less volatile. Good for conservative investors. Blue-chip reputation usually means high quality business. Dividend Guys: 10+ years of increases. Newer than aristocrats but still reliable."}, {"num": 2, "title": "Building a Dividend Portfolio", "duration": "8 min", "description": "Construct a portfolio focused on dividend income.", "content": "Target 10-20 dividend stocks or dividend funds for diversification. Diversify across sectors: consumer, pharma, utilities, industrials. Mix dividend stocks and dividend ETFs for liquidity. Start with aristocrats for reliability. Add higher-yielding stocks for more income. Reinvest dividends for compounding (automatic on many brokers). Track dividend calendar for expected income."}, {"num": 3, "title": "Dividend Growth vs Value", "duration": "8 min", "description": "Understand relationship between dividend strategies and valuation.", "content": "Growth dividend stocks: moderate yield, increasing rapidly. Price increases significantly over time. Value dividend stocks: higher yield, slower growth. Attractive prices relative to fundamentals. Blend of both provides steady income and capital appreciation. Don't chase ultra-high yields (often unsustainable). Quality matters most - sustainable dividends from strong companies."}]},
            3: {"title": "Advanced Dividend Strategies", "chapters": [{"num": 1, "title": "Covered Calls and Dividend Strategies", "duration": "9 min", "description": "Generate additional income from dividend holdings.", "content": "Covered calls: sell call options on shares you own. Collect premium (fee). Stock gets called away if price rises (that's OK). Limits gains but increases income. Best on stocks you don't mind selling. Many dividend investors use this for extra income. Requires brokerage allowed options trading."}, {"num": 2, "title": "Tax Implications of Dividends", "duration": "+ min", "description": "Understand tax treatment of different dividend types.", "content": "Qualified dividends taxed at long-term capital gains rates (up to 20%). Preferential compared to ordinary income (up to 37%). Must hold stock 60+ days around ex-dividend date. Unqualified dividends taxed as ordinary income. REITs and master limited partnerships taxed as ordinary income. Hold dividend stocks in IRA/401k to avoid tax. Manage dividend income for tax efficiency."}, {"num": 3, "title": "Dividend Reinvestment Plans (DRIPs)", "duration": "8 min", "description": "Automatically reinvest dividends for compounding.", "content": "DRIP: automatically buy more shares with dividend payments. Compounds returns significantly over decades. Many companies offer DRIPs directly (no fees). Brokerage DRIPs also available. Fractional shares allow reinvesting all dividends. Example: $100 dividend buys $5 more stock, remaining fraction. Dollar-cost averaging happens automatically. Over 30 years with 3% yield and 8% growth, compounding dramatically exceeds just dividends."}]}
        }
    }
}

# Additional courses 6-17 in intermediate/advanced categories
ADDITIONAL_COURSES = """
6: {
    "name": "Technical Analysis Fundamentals",
    "instructor": "Kevin Zhang",
    "category": "intermediate"
},
7: {
    "name": "Fundamental Analysis Deep Dive",
    "instructor": "Patricia Adams",
    "category": "intermediate"
},
8: {
    "name": "Portfolio Construction Methods",
    "instructor": "James Murphy",
    "category": "intermediate"
},
9: {
    "name": "Options Trading Strategies",
    "instructor": "Lisa Thompson",
    "category": "intermediate"
},
10: {
    "name": "Cryptocurrency Investing",
    "instructor": "Marcus Lee",
    "category": "intermediate"
},
11: {
    "name": "Tax-Efficient Investing",
    "instructor": "Susan Green",
    "category": "intermediate"
},
12: {
    "name": "Algorithmic Trading Basics",
    "instructor": "Dr. Henry Chen",
    "category": "advanced"
},
13: {
    "name": "Derivatives and Hedging",
    "instructor": "Victoria Stone",
    "category": "advanced"
},
14: {
    "name": "Quantitative Analysis",
    "instructor": "Dr. Nathan Brooks",
    "category": "advanced"
},
15: {
    "name": "Macro Economic Investing",
    "instructor": "Dr. Eleanor White",
    "category": "advanced"
},
16: {
    "name": "Private Equity and Venture Capital",
    "instructor": "Richard Foster",
    "category": "advanced"
},
17: {
    "name": "Building an Investment Firm",
    "instructor": "Margaret Clarke",
    "category": "advanced"
}
"""

def generate_module_html(course_id, module_id, course_name, module_title, instructor, category, chapters):
    """Generate a single module HTML file."""
    
    category_class = "beginner" if category == "beginner" else ("intermediate" if category == "intermediate" else "advanced")
    category_display = category.capitalize()
    
    # Create chapters list in template
    chapters_html = "[\n"
    for i, ch in enumerate(chapters):
        chapters_html += f'''        {{
          id: {i+1},
          title: "{ch.get('title', 'Chapter ' + str(i+1))}",
          duration: "{ch.get('duration', '10 min')}",
          type: "video",
          completed: false,
          description: "{ch.get('description', 'Learn important concepts')}",
          content: "{ch.get('content', 'Content goes here')}",
          youtubeUrl: "https://www.youtube.com/embed/dQw4w9WgXcQ",
          resources: [{{"name": "{ch.get('title', 'Chapter')}.pdf", "size": "1.5 MB"}}]
        }}'''
        if i < len(chapters) - 1:
            chapters_html += ",\n"
        else:
            chapters_html += "\n"
    chapters_html += "      ]"
    
    total_duration = len(chapters) * 10  # Estimate
    
    html_content = f'''<!doctype html>
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
              <span>📊 {len(chapters)} Chapters</span>
            </div>
          </div>
        </div>

        <div class="module-chapters">
          <div class="chapters-header">
            <h2>Chapters</h2>
            <span class="chapters-count">{len(chapters)} chapters</span>
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
            <p>{len(chapters)}</p>
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
    
    return html_content

def main():
    print("🔄 Module Generator - Creating all course module pages...")
    print(f"📊 Location: {os.getcwd()}")
    
    created_count = 0
    
    # Generate for courses 1-5 (beginner) with sample data
    for course_id in range(1, 6):
        if course_id in COURSES_DATABASE:
            course = COURSES_DATABASE[course_id]
            course_name = course['name']
            instructor = course['instructor']
            category = course['category']
            
            for module_id in range(1, 4):
                if module_id in course['modules']:
                    module = course['modules'][module_id]
                    module_title = module['title']
                    chapters = module['chapters']
                    
                    filename = f'Module-{course_id}-{module_id}.html'
                    
                    html_content = generate_module_html(
                        course_id, module_id, course_name, module_title,
                        instructor, category, chapters
                    )
                    
                    try:
                        with open(filename, 'w', encoding='utf-8') as f:
                            f.write(html_content)
                        print(f"✅ Created {filename}")
                        created_count += 1
                    except Exception as e:
                        print(f"❌ Error creating {filename}: {e}")
    
    print(f"\n✨ Complete! Created {created_count} module files.")
    print("📝 Notes:")
    print("  - Modules for courses 1-5 (Beginner) created with complete content")
    print("  - Modules for courses 6-17 need to be created with their specific content")
    print("  - Update Courses.html links to point to these new module files")
    print("  - All modules automatically link to Courses.html for navigation")

if __name__ == '__main__':
    main()
