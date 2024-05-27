# Text Generation: A Systematic Literature Review of Tasks, Evaluation, and Challenges

[![arXiv](https://img.shields.io/badge/arXiv-2405.15604-b31b1b.svg)](https://arxiv.org/abs/2405.15604)

This is the official repository for the paper **Text Generation: A Systematic Literature Review of Tasks, Evaluation, and Challenges**.

<p float="left">
  <img src="under_construction.png" width="800" />
</p>

This repository is under construction. Please be patient until we sort things out. Thank you!

## Metrics

| **Type**        | **Category** | **Metric**       | **Description**                                                                               | **Used** |
|-----------------|--------------|------------------|-----------------------------------------------------------------------------------------------|----------|
| Model-free      | N-gram       | [BLEU](https://www.aclweb.org/anthology/P02-1040/) | Textual overlap between source and reference (precision).                                    | 69       |
|                 |              | [ROUGE](https://www.aclweb.org/anthology/W04-1013/) | Textual overlap between source and reference (recall).                                       | 46       |
|                 |              | [METEOR](https://www.aclweb.org/anthology/W05-0909/) | Textual overlap between source and reference (precision and recall).                         | 32       |
|                 |              | [CIDEr](https://openaccess.thecvf.com/content_cvpr_2015/html/Vedantam_CIDEr_Consensus-Based_Image_2015_CVPR_paper.html) | Measures consensus on multiple reference texts.                                               | 15       |
|                 |              | [chrF++](https://www.aclweb.org/anthology/W17-4770/) | Character-based F-score computed using n-grams.                                              | 13       |
|                 |              | [Dist-n](https://www.aclweb.org/anthology/N16-1014/) | Measures generation diversity by the percentage of distinct n-grams.                         | 8        |
|                 |              | [NIST](https://dl.acm.org/doi/10.5555/1289189.1289273) | Alters BLEU to also consider n-gram informativeness.                                         | 6        |
|                 |              | [Self-BLEU](https://dl.acm.org/doi/10.1145/3209978.3210080) | Measures generation diversity by calculating BLEU between generated samples.                 | 2        |
|                 | Statistical  | [Perplexity](https://aclanthology.org/2023.acl-long.13/) | Fluency metric based on the likelihood of word sequences.                                    | 23       |
|                 |              | [Word Error Rate](https://aclanthology.org/D18-1150/) | The rate of words that are different from a reference sequence based on the Levenshtein distance. | 11       |
|                 | Graph        | [SPICE](https://link.springer.com/chapter/10.1007/978-3-319-46454-1_24) | Measures the semantic similarity of two texts by the distance of their scene graphs.         | 6        |
| Model-based     | Hybrid       | [BERTScore](https://arxiv.org/abs/1904.09675) | Contextual token similarity to measure textual overlap.                                      | 13       |
|                 |              | [MoverScore](https://aclanthology.org/D19-1053/) | Uses contextualized embeddings and captures both intersection and deviation from the reference for a similarity score. | 6        |
|                 |              | [Word Mover Distance](https://proceedings.mlr.press/v37/kusnerb15.html) | Distance metric to measure the dissimilarity of two texts. | 2        |
|                 | Trained      | [BLEURT](https://aclanthology.org/2020.acl-main.704/) | Models human judgement on text quality. | 4        |
|                 |              | [BARTScore](https://proceedings.neurips.cc/paper/2021/hash/e4d2b6e6fdeca3e60e0f1a62fee3d9dd-Abstract.html) | Promptable metric that models human judgments on faithfulness besides precision and recall. | 3        |

## Pipeline

### Initial Search

<p float="left">
  <img src="output/figures/avg_citations.png" width="400" />
  <img src="output/figures/yearly_distribution.png" width="400" /> 
</p>

### Manual Filtering

We reduced 279 papers to 136 papers by reading their titles and abstracts.
You can download a PDF containing our relevance judgments [here](https://github.com/jonas-becker/review-on-machine-generated-text/blob/main/relevance_judgements.pdf).

---

## Setup

We recommend using Python 3.10 for this project.

First, install the requirements:
```pip install -r requirements.txt```

---

### Code

The project has multiple scripts included, each used for separate parts of the pipeline.

1) `setup.py`: Defines the parameters used for searching and filtering the scientific works.
1) `tokens.py`: You need an API key to use the Semantic Scholar API. This is the place to put it.
2) `search.py`: The initial retrieval of scientific works through the Semantic Scholar API.
3) `filter.py`: The automated filtering process that selects the top five works per query and year by influential citation counts.

## Citation
If you use this repository or our paper for your research work, please cite us in the following way.

```
@misc{becker2024text,
      title={Text Generation: A Systematic Literature Review of Tasks, Evaluation, and Challenges}, 
      author={Jonas Becker and Jan Philip Wahle and Bela Gipp and Terry Ruas},
      year={2024},
      eprint={2405.15604},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
