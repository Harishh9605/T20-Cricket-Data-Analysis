# ============================================================
# PROJECT: T20 Cricket Data Analysis
# TOOLS: Python, MySQL, Pandas, Matplotlib, Excel
#
# DESCRIPTION:
# This script connects Python to a MySQL database,
# runs multiple SQL queries on T20 cricket data,
# visualizes the results, and exports outputs to Excel.
# ============================================================


# -----------------------------
# Import required libraries
# -----------------------------
import mysql.connector          # Connects Python to MySQL
import pandas as pd              # Data analysis & tables
import matplotlib.pyplot as plt  # Data visualization
import os                        # File & folder handling


# -----------------------------
# Create output folder for Excel files
# -----------------------------
# If the folder already exists, no error will occur
os.makedirs("output", exist_ok=True)


# -----------------------------
# Connect to MySQL database
# -----------------------------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Harishh@7575",      # <-- CHANGE THIS
    database="t20_analysis"
)

print("Connected to MySQL successfully!")


# ============================================================
# ANALYSIS 1: TOP 10 RUN SCORERS
# ============================================================

query_top_runs = """
SELECT Player, Runs
FROM t20
ORDER BY Runs DESC
LIMIT 10;
"""

df_top_runs = pd.read_sql(query_top_runs, conn)

print("\nTop 10 Run Scorers:")
print(df_top_runs)

# Save to Excel
df_top_runs.to_excel("output/top_10_run_scorers.xlsx", index=False)

# Visualization
plt.figure()
plt.bar(df_top_runs["Player"], df_top_runs["Runs"])
plt.xticks(rotation=75)
plt.xlabel("Player")
plt.ylabel("Runs")
plt.title("Top 10 T20 Run Scorers")
plt.tight_layout()
plt.show()


# ============================================================
# ANALYSIS 2: MOST CONSISTENT BATSMEN (BEST AVERAGE)
# ============================================================

query_avg = """
SELECT Player, Ave
FROM t20
WHERE Mat >= 50
ORDER BY Ave DESC
LIMIT 10;
"""

df_avg = pd.read_sql(query_avg, conn)

print("\nTop 10 Batting Averages:")
print(df_avg)

# Save to Excel
df_avg.to_excel("output/top_10_batting_average.xlsx", index=False)

# Visualization
plt.figure()
plt.bar(df_avg["Player"], df_avg["Ave"])
plt.xticks(rotation=75)
plt.xlabel("Player")
plt.ylabel("Batting Average")
plt.title("Top 10 Most Consistent T20 Batsmen")
plt.tight_layout()
plt.show()


# ============================================================
# ANALYSIS 3: FASTEST SCORING BATSMEN (STRIKE RATE)
# ============================================================

query_sr = """
SELECT Player, SR
FROM t20
WHERE Mat >= 50
ORDER BY SR DESC
LIMIT 10;
"""

df_sr = pd.read_sql(query_sr, conn)

print("\nTop 10 Strike Rates:")
print(df_sr)

# Save to Excel
df_sr.to_excel("output/top_10_strike_rate.xlsx", index=False)

# Visualization
plt.figure()
plt.bar(df_sr["Player"], df_sr["SR"])
plt.xticks(rotation=75)
plt.xlabel("Player")
plt.ylabel("Strike Rate")
plt.title("Top 10 Fastest Scoring T20 Batsmen")
plt.tight_layout()
plt.show()


# ============================================================
# ANALYSIS 4: AVERAGE vs STRIKE RATE (BALANCE ANALYSIS)
# ============================================================

query_balance = """
SELECT Player, Ave, SR
FROM t20
WHERE Mat >= 50;
"""

df_balance = pd.read_sql(query_balance, conn)

print("\nAverage vs Strike Rate Sample:")
print(df_balance.head())

# Save to Excel
df_balance.to_excel("output/average_vs_strike_rate.xlsx", index=False)

# Visualization
plt.figure()
plt.scatter(df_balance["Ave"], df_balance["SR"])
plt.xlabel("Batting Average")
plt.ylabel("Strike Rate")
plt.title("Batting Average vs Strike Rate (T20 Cricket)")
plt.tight_layout()
plt.show()


# ============================================================
# CLOSE DATABASE CONNECTION
# ============================================================

conn.close()
print("\nMySQL connection closed successfully.")
