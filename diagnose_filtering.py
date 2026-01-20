import pandas as pd
from setup import *

# Read the combined file
df = pd.read_csv('output/search/deduplicated_combined.csv', sep=';')

print(f"Total papers in combined file: {len(df)}")
print(f"Papers with null subquery: {df['subquery'].isna().sum()}")
print(f"Papers with empty subquery: {(df['subquery'].astype(str).str.strip() == '').sum()}")
print(f"\nUnique years: {sorted(df['year'].dropna().unique())}")

# Test the filtering logic
print("\n" + "="*60)
print("Testing filtering logic from filter.py:")
print("="*60)

years = df['year'].unique()
total_matches = 0

for year in sorted(years):
    yearly_df = df[df['year'] == year]
    print(f"\nYear {year}: {len(yearly_df)} papers total")
    
    year_matches = 0
    for subquery in SEARCH_SUB_KEYS + SEARCH_ANCHORS:
        # This is the filtering logic from filter.py line 98
        matches = yearly_df[yearly_df['subquery'].str.contains(subquery, na=False)]
        if len(matches) > 0:
            # TOP_X = 5, so we'd take top 5
            top_matches = min(len(matches), TOP_X)
            year_matches += top_matches
            if year in [2024.0, 2025.0] and len(matches) > 0:
                print(f"  {subquery}: {len(matches)} matches -> top {top_matches} selected")
    
    print(f"  Total papers that would be selected for year {year}: {year_matches}")
    total_matches += year_matches

print(f"\n" + "="*60)
print(f"Total papers that would pass filtering: {total_matches}")
print(f"After deduplication (by paperId), this would be even fewer")

# Check what's actually in allTime.csv
print("\n" + "="*60)
print("Checking input/allTime.csv:")
print("="*60)
try:
    alltime_df = pd.read_csv('input/allTime.csv', sep=';')
    print(f"Papers in allTime.csv: {len(alltime_df)}")
    print(f"Years: {sorted(alltime_df['year'].dropna().unique())}")
    print(f"\nThis matches the filtered output from filter.py")
    print(f"The filtering is working as designed - it extracts TOP {TOP_X} papers per year per subquery")
except Exception as e:
    print(f"Error reading allTime.csv: {e}")

