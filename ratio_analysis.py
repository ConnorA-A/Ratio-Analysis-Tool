import yfinance as yf
import pandas as pd

ticker = input("Please input a ticker: ")
stock = yf.Ticker(ticker)

#income statement data

income_statement = stock.income_stmt
income_statement = income_statement.iloc[:, :4]

balance_sheet = stock.balance_sheet
balance_sheet = balance_sheet.iloc[:, :4]

#print(income_statement)
print(income_statement.index)
#print(income_statement.columns)

#print(balance_sheet)
#print(balance_sheet.index)
#print(balance_sheet.columns)




# Revenue Growth

revenue = income_statement.loc["Total Revenue"].sort_index()
growth = revenue.pct_change() 
revenue_growth_rate = growth.map(lambda x: f"{x:.2%}")



# Gross Profit Margin

gross_profit = income_statement.loc["Gross Profit"].sort_index()
gpm = gross_profit / revenue
gpm_percent = gpm.map(lambda x: f"{x:.2%}")

# EBITDA Margin

ebitda = income_statement.loc["EBITDA"].sort_index()
ebitda_revenue = ebitda / revenue
ebitda_margin = ebitda_revenue.map(lambda x: f"{x:.2%}")



# Operating Profit Margin

operating_profit = income_statement.loc["Operating Income"].sort_index()
opm = operating_profit / revenue
opm_percent = opm.map(lambda x: f"{x:.2%}")


# Net Profit Margin

net_profit = income_statement.loc["Net Income"].sort_index()
npm = net_profit / revenue
npm_percent = npm.map(lambda x: f"{x:.2%}")

# Retrun on Assets

total_assets = balance_sheet.loc["Total Assets"].sort_index()
roa = net_profit / total_assets
roa_percent = roa.map(lambda x: f"{x:.2%}")

# Return on Equity

shareholder_equity = balance_sheet.loc["Stockholders Equity"].sort_index()
roe = net_profit / shareholder_equity
roe_percent = roe.map(lambda x: f"{x:.2%}")


# Retrun on Capital Employed

current_liabilities = balance_sheet.loc["Current Liabilities"].sort_index()
capital_employed = total_assets - current_liabilities
roce = operating_profit / capital_employed
roce_percent = roce.map(lambda x: f"{x:.2%}")


print("\nProfitability Ratios")
data = {
    "YOY Revenue Growth Rate": revenue_growth_rate,
    "Gross Profit Margin": gpm_percent,
    "EBITDA Margin": ebitda_margin,
    "Operating Profit Margin": opm_percent,
    "Net Profit Margin": npm_percent,
    "Return on Assets": roa_percent,
    "Return on Equity": roe_percent,
    "Retur on Capital Employed": roce_percent
}

df = pd.DataFrame(data)
df = df.replace(["nan%", "NaN", "nan"], "N/A")
df = df.T
df = df[df.columns[::-1]]
print(df)

print("\n\nLiquidity Ratios")

# Current Ratio

current_assets = balance_sheet.loc["Current Assets"].sort_index()
current_ratio = (current_assets / current_liabilities).round(2)

# Quick Ratio

inventory = balance_sheet.loc["Inventory"].sort_index()
quick_ratio = ((current_assets - inventory) / current_liabilities).round(2)

# Asset Turnover

asset_turnover = (revenue / total_assets).round(2)

# Inventory Turnover

cogs = income_statement.loc["Cost Of Revenue"].sort_index()
inventory_turnover = (cogs / inventory).round(2)

data = {
    "Current Ratio": current_ratio,
    "Quick Ratio": quick_ratio,
    "Asset Turnover": asset_turnover,
    "Inventory Turnover": inventory_turnover
}

df = pd.DataFrame(data)
df = df.replace(["nan%", "NaN", "nan"], "N/A")
df = df.fillna("N/A")
df = df.T
df = df[df.columns[::-1]]
print(df)