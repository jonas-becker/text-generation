FIELDS = ["paperId", "url", "title", "venue", "publicationVenue", "year", "authors", "abstract",
          "referenceCount", "citationCount", "openAccessPdf", "fieldsOfStudy", "s2FieldsOfStudy", "publicationTypes",
          "publicationDate", "journal"]
TIMEFRAME = None     # format: '{year}' or '{start}-{end}'
MAX_RETURNED_PAPERS = 100   # should not be more than 100
FIELDS_OF_STUDY = ["Computer Science"]

SEARCH_ANCHORS = [
    "Text Generation",
    "Machine Generated Text"
]
SEARCH_SUB_KEYS = [
    "Paraphrase",
    "NLP",
    "Natural Language Generation",
    "Language Model",
    "Evaluation Metrics",
    "Bias",
    "Privacy",
    "Controllable",
    "Creative",
    "Machine",
    "Automated",
    "Task",
    "Training",
    "Cost",
    "CO2 Emission",
    "Detection"
]

TOP_X = 5  # how many top papers per year and subquery to extract