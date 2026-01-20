from tqdm import tqdm
import pandas as pd
from setup import *
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size': 16})

pd.set_option('display.max_columns', None)

df = pd.read_csv("input/allTime.csv", sep=";")
print(df.head())

print("STATS:")
print("Total papers: " + str(df.shape[0]))
print("Total papers (2017+): " + str(df[df["year"] >= 2017].shape[0]))
print("Total papers (2018+): " + str(df[df["year"] >= 2018].shape[0]))
print("Total papers (2019+): " + str(df[df["year"] >= 2019].shape[0]))
print("Total papers (2020+): " + str(df[df["year"] >= 2020].shape[0]))
print("Total papers (2021+): " + str(df[df["year"] >= 2021].shape[0]))
print("Total papers (2022+): " + str(df[df["year"] >= 2022].shape[0]))
print("Total papers (2023+): " + str(df[df["year"] >= 2023].shape[0]))
print("Total papers (2024+): " + str(df[df["year"] >= 2024].shape[0]))
print("Total papers (2025+): " + str(df[df["year"] >= 2025].shape[0]))

interdisciplinary_fields = [    # checked manually
    'Art',
    'Biology',
    'Business',
    'Chemistry',
    'Computer Science',
    'Economics',
    'Engineering',
    'Environmental Science',
    'Geography',
    'Mathematics',
    'Medicine',
    'Physics',
    'Political Science',
    'Psychology',
    'Sociology'
]
df_stats = df.dropna(subset=['fieldsOfStudy'])
print("Amount of papers from the field (additional field besides Computer Science)")
for f in interdisciplinary_fields:
    print(str(f) + " : " + str(df_stats[df_stats["fieldsOfStudy"].str.contains(str(f))].shape[0]))


years = df["year"].unique()

xpoints = []
ypoints= []
for year in np.sort(np.array(years)):
    print(f"{year}: {df[df['year'] == year].shape[0]} papers")
    if int(year) >= 2010:
        xpoints = xpoints + [int(year)]
        ypoints = ypoints + [int(df[df['year'] == year].shape[0])]

plt.plot(xpoints, ypoints)
plt.xticks(xpoints[::2])
plt.grid()
plt.title("Number of publications returned\nby the Semantic Scholar API per year")
plt.savefig('output/figures/yearly_distribution.png')

plt.clf()
xpoints = []
ypoints= []
for year in np.sort(np.array(years)):
    if int(year) >= 2010:
        xpoints = xpoints + [int(year)]
        influentialCitationCountList = list(df[df['year'] == year]["influentialCitationCount"])
        avg = sum(influentialCitationCountList)/len(influentialCitationCountList)
        ypoints = ypoints + [avg]

plt.plot(xpoints, ypoints)
plt.xticks(xpoints[::2])

xpoints = []
ypoints= []
for year in np.sort(np.array(years)):
    if int(year) >= 2010:
        xpoints = xpoints + [int(year)]
        citationCountList = list(df[df['year'] == year]["citationCount"])
        avg = sum(citationCountList)/len(citationCountList)
        ypoints = ypoints + [avg]

plt.plot(xpoints, ypoints)
plt.xticks(xpoints[::2])
plt.grid()
plt.legend(["Influential Citations", "Raw Citiations"])
plt.title("Average citations per year")
plt.savefig('output/figures/avg_citations.png')

top_df_influentialCitationCount = pd.DataFrame()
for year in years:
    for subquery in SEARCH_SUB_KEYS + SEARCH_ANCHORS:
        yearly_df = df[df["year"] == year]
        yearly_subquery_df = yearly_df[yearly_df["subquery"].str.contains(subquery)]
        top_df_influentialCitationCount = pd.concat([top_df_influentialCitationCount, yearly_subquery_df.nlargest(TOP_X, ['influentialCitationCount'])])

print(f"Extracted a total of {top_df_influentialCitationCount.shape[0]} for influentialCitationCount.")
top_df_influentialCitationCount = top_df_influentialCitationCount.reset_index(drop=True)
top_df_influentialCitationCount = top_df_influentialCitationCount.drop_duplicates(subset=["paperId"], ignore_index=True)     # no double papers
print(f"Reduced the amount of papers down to {top_df_influentialCitationCount.shape[0]} after deduplication.")
print(f"Amount of papers from 2017+: {top_df_influentialCitationCount[top_df_influentialCitationCount['year']>=2017].shape[0]}")
print(f"Amount of papers from 2023: {top_df_influentialCitationCount[top_df_influentialCitationCount['year']==2023].shape[0]}")
print(f"Amount of papers from 2024: {top_df_influentialCitationCount[top_df_influentialCitationCount['year']==2024].shape[0]}")
print(f"Amount of papers from 2025: {top_df_influentialCitationCount[top_df_influentialCitationCount['year']==2025].shape[0]}")

top_df_influentialCitationCount.to_csv(f"output/extraction/topX_YearSubquery.csv", sep=";", header=True)

df = top_df_influentialCitationCount

print("STATS:")
print("Total papers: " + str(df.shape[0]))
print("Total papers (2017+): " + str(df[df["year"] >= 2017].shape[0]))
print("Total papers (2018+): " + str(df[df["year"] >= 2018].shape[0]))
print("Total papers (2019+): " + str(df[df["year"] >= 2019].shape[0]))
print("Total papers (2020+): " + str(df[df["year"] >= 2020].shape[0]))
print("Total papers (2021+): " + str(df[df["year"] >= 2021].shape[0]))
print("Total papers (2022+): " + str(df[df["year"] >= 2022].shape[0]))
print("Total papers (2023+): " + str(df[df["year"] >= 2023].shape[0]))
print("Total papers (2024+): " + str(df[df["year"] >= 2024].shape[0]))
print("Total papers (2025+): " + str(df[df["year"] >= 2025].shape[0]))

interdisciplinary_fields = [    # checked manually
    'Art',
    'Biology',
    'Business',
    'Chemistry',
    'Computer Science',
    'Economics',
    'Engineering',
    'Environmental Science',
    'Geography',
    'Mathematics',
    'Medicine',
    'Physics',
    'Political Science',
    'Psychology',
    'Sociology'
]
df_stats = df.dropna(subset=['fieldsOfStudy'])
print("Amount of papers from the field (additional field besides Computer Science)")
for f in interdisciplinary_fields:
    print(str(f) + " : " + str(df_stats[df_stats["fieldsOfStudy"].str.contains(str(f))].shape[0]))

years = df["year"].unique()

xpoints = []
ypoints= []
for year in np.sort(np.array(years)):
    print(f"{year}: {df[df['year'] == year].shape[0]} papers")
    
print("Done.")
