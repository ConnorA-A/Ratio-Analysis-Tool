# Ratio Analysis Tool

A Python tool that pulls financial statement data for any public company and calculates a comprehensive set of financial ratios across six categories — the kind of analysis you'd do when evaluating a company's performance, financial health, or investment potential.

Built to practise applying the ratio analysis I studied in my accounting degree using real financial data, while developing my Python and pandas skills.

## What it does

Enter any stock ticker and the tool pulls four years of financial statement data (income statement, balance sheet, and cash flow statement) via yfinance, then calculates and displays:

**Profitability** — YOY revenue growth, gross profit margin, EBITDA margin, operating profit margin, net profit margin, return on assets, return on equity, and return on capital employed

**Liquidity** — current ratio and quick ratio (automatically excludes inventory for companies that don't carry it)

**Leverage** — debt-to-equity, debt-to-assets, interest cover, and debt-to-EBITDA

**Efficiency** — receivables days, payables days, inventory days, cash conversion cycle, inventory turnover, and asset turnover

**Per share** — basic EPS, diluted EPS, revenue per share, book value per share, cash per share, and total debt per share

**Valuation** — trailing and forward P/E, P/B, price-to-sales, price-to-cashflow, PEG ratio, EV/EBITDA, and dividend yield

## Screenshot

### Output for Coca-Cola (KO)

![Ratio analysis output for KO showing all six ratio categories across four years](screenshots/ko_output.png)

## Built with

- **Python**
- **yfinance** — financial statement and market data
- **pandas** — data structuring and table formatting

## What I learned

- Pulling and navigating real financial statement data programmatically (income statement, balance sheet, cash flow)
- Handling missing data defensively — not every company reports the same line items (e.g. inventory for service companies), so the tool checks before calculating rather than crashing
- Applying textbook ratio formulas to messy real-world data where line item names and availability vary between companies
- Formatting mixed output types (percentages, multiples, currency) cleanly in pandas DataFrames