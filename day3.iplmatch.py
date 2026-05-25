# =========================================================
# 🏏 IPL DELIVERY DATA EXPLORER (UPDATED FOR YOUR DATA)
# =========================================================

import pandas as pd
import sys
import os

# ✅ Fix emoji issue (Windows)
sys.stdout.reconfigure(encoding='utf-8')

# =========================================================
# STEP 1 — LOAD DATASET
# =========================================================

file_path = r"matches.csv"   # <-- your current file (deliveries data)

if not os.path.exists(file_path):
    print("❌ File not found!")
    exit()

df = pd.read_csv(file_path)

print("="*50)
print("📌 FIRST 5 ROWS")
print("="*50)
print(df.head())


# =========================================================
# STEP 2 — DATASET INFO
# =========================================================

print("\n" + "="*50)
print("📊 DATASET INFO")
print("="*50)
df.info()


# =========================================================
# STEP 3 — STATISTICAL SUMMARY
# =========================================================

print("\n" + "="*50)
print("📈 DATA SUMMARY")
print("="*50)
print(df.describe())


# =========================================================
# STEP 4 — TOTAL RUNS SCORED
# =========================================================

print("\n" + "="*50)
print("🏏 TOTAL RUNS SCORED IN IPL")
print("="*50)

print("Total Runs:", df['total_runs'].sum())


# =========================================================
# STEP 5 — TOP 5 BATSMEN (BY RUNS)
# =========================================================

print("\n" + "="*50)
print("🏆 TOP 5 BATSMEN")
print("="*50)

top_batsmen = df.groupby('batsman')['batsman_runs'].sum().sort_values(ascending=False).head(5)
print(top_batsmen)


# =========================================================
# STEP 6 — TOP 5 BOWLERS (BY WICKETS)
# =========================================================

print("\n" + "="*50)
print("🎯 TOP 5 BOWLERS")
print("="*50)

wickets = df[df['player_dismissed'].notnull()]
top_bowlers = wickets['bowler'].value_counts().head(5)

print(top_bowlers)


# =========================================================
# STEP 7 — MATCHES COUNT
# =========================================================

print("\n" + "="*50)
print("📊 TOTAL MATCHES")
print("="*50)

print("Total Matches:", df['match_id'].nunique())


# =========================================================
# STEP 8 — EXTRA RUNS ANALYSIS
# =========================================================

print("\n" + "="*50)
print("⚡ EXTRA RUNS")
print("="*50)

print("Total Extra Runs:", df['extra_runs'].sum())


# =========================================================
# STEP 9 — CHECK NULL VALUES
# =========================================================

print("\n" + "="*50)
print("❓ NULL VALUES")
print("="*50)

print(df.isnull().sum())


# =========================================================
# STEP 10 — SORT DATA
# =========================================================

print("\n" + "="*50)
print("📅 SORTED DATA (BY MATCH ID)")
print("="*50)

print(df.sort_values(by='match_id').head())


# =========================================================
# STEP 11 — GROUPBY EXAMPLE
# =========================================================

print("\n" + "="*50)
print("📌 TOTAL RUNS BY TEAM")
print("="*50)

team_runs = df.groupby('batting_team')['total_runs'].sum().sort_values(ascending=False)
print(team_runs.head())


# =========================================================
# BONUS — STRIKE RATE OF TOP BATSMAN
# =========================================================

print("\n" + "="*50)
print("🔥 BONUS: STRIKE RATE")
print("="*50)

balls = df.groupby('batsman')['ball'].count()
runs = df.groupby('batsman')['batsman_runs'].sum()

strike_rate = (runs / balls) * 100

print(strike_rate.sort_values(ascending=False).head(5))


# =========================================================
# FINAL MESSAGE
# =========================================================

print("\n" + "="*50)
print("✅ IPL DELIVERY DATA ANALYSIS COMPLETED!")
print("="*50)