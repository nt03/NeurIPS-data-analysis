**filename description**:

1. `scrape_nips.py`: Code to scrape the NIPS data for the years 2016-2019
2. `nips{yy}_track.ipynb`: jupyter notebooks with an yearwise analysis of track data to create a `main_track` column
3. `/models/eda.ipynb`: Performs exploratory data analysis on the dataset
4. `/models/modeling.ipynb`: Run ML classification models: Naive Bayes and XGBoost on the complete dataset
5. `/models/modeling_subset`.ipynb: Run ML classification models: Naive Bayes and XGBoost on a subset of dataset (with 3 tracks instead of 8)
6. `fastbert_attempt.ipynb`: implementation of Fastbert model on the dataset
7. `/bert-uncased/`: readme.md details the BERT model implementation
