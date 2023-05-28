from semanticscholar import SemanticScholar
import pandas as pd
import tokens
from tqdm import tqdm
from setup import *

pd.set_option('display.max_columns', None)
sch = SemanticScholar(api_key=tokens.API_KEY)

total_df = pd.DataFrame()

for search_anchor in SEARCH_ANCHORS:
    print(f"Searching with anchor: {search_anchor} ---> Format: anchor + sub_key")
    for search_sub_key in tqdm(SEARCH_SUB_KEYS):
        query = search_anchor + " " + search_sub_key
        results = sch.search_paper(query, year=TIMEFRAME, limit=MAX_RETURNED_PAPERS, open_access_pdf=True, fields_of_study=FIELDS_OF_STUDY)
        results = [dict(item) for item in results.items]
        df = pd.json_normalize(results)
        df.to_csv(f"output/search/{query}.csv", sep=";", header=True)
        df["subquery"] = search_sub_key
        total_df = pd.concat([total_df, df], ignore_index=True)

    # No sub key
    query = search_anchor
    results = sch.search_paper(query, year=TIMEFRAME, limit=MAX_RETURNED_PAPERS, open_access_pdf=True, fields_of_study=FIELDS_OF_STUDY)
    results = [dict(item) for item in results.items]
    df = pd.json_normalize(results)
    df.to_csv(f"output/search/{query}.csv", sep=";", header=True)
    df["subquery"] = query + " (None)"
    total_df = pd.concat([total_df, df], ignore_index=True)

print("Adding query information for duplicate papers...")
for i, row in tqdm(total_df.iterrows()):
    entries = total_df[total_df["paperId"] == row["paperId"]]
    to_add = ""
    for j, entry_row in entries.iterrows():
        if entry_row["subquery"] not in to_add and entry_row["subquery"] not in row["subquery"]:
            to_add = to_add + " | " + entry_row["subquery"]
    total_df.at[i, "subquery"] = row["subquery"] + to_add

print(f"Finished. Combined {total_df.shape[0]} entries and removing duplicate papers...")
total_df = total_df.reset_index(drop=True)
total_df = total_df.drop_duplicates(subset=["paperId"], ignore_index=True)     # no double papers
print(f"After deduplication: {total_df.shape[0]}")
total_df.to_csv(f"output/search/deduplicated.csv", sep=";", header=True)

print("Done.")
