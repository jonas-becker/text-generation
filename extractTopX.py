import pandas as pd
from tqdm import tqdm
from setup import *

pd.set_option('display.max_columns', None)

df = pd.read_csv("input/allTime.csv", sep=";")

print("Total papers: " + str(df.shape[0]))

years = df["year"].unique()

top_df_citationCount = pd.DataFrame()
for year in years:
    yearly_df = df[df["year"] == year]
    top_df_citationCount = pd.concat([top_df_citationCount, yearly_df.nlargest(TOP_X, ['citationCount'])])
print(f"Extracted a total of {top_df_citationCount.shape[0]} for citationCount.")
top_df_citationCount.to_csv(f"output/extraction/topX_citationCount.csv", sep=";", header=True)

top_df_influentialCitationCount = pd.DataFrame()
for year in years:
    yearly_df = df[df["year"] == year]
    top_df_influentialCitationCount = pd.concat([top_df_influentialCitationCount, yearly_df.nlargest(TOP_X, ['influentialCitationCount'])])
print(f"Extracted a total of {top_df_influentialCitationCount.shape[0]} for influentialCitationCount.")
top_df_influentialCitationCount.to_csv(f"output/extraction/topX_influentialCitationCount.csv", sep=";", header=True)

overlap_df = pd.merge(top_df_citationCount, top_df_influentialCitationCount, how="inner", on=["paperId"])
print(f"There is an overlap of {overlap_df.shape[0]}.")
overlap_df.to_csv(f"output/extraction/overlap.csv", sep=";", header=True)

for year in years:
    print(f"{year}: {df[df['year'] == year].shape[0]} papers")

print(df["query"].nunique())

print("Done.")
