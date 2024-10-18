# Statistics Analysis Notebooks

This repository contains a collection of Jupyter notebooks demonstrating various statistical analysis techniques using Python. Each notebook focuses on a specific method and provides a practical example using a real-world dataset.

**Key libraries used:** pandas, scikit-learn, statsmodels

## Notebooks

### 1. Exploratory Data Analysis of Nails Dataset

This notebook explores the chemical composition of different types of nails. Using Hotelling's T-squared statistic, we analyze the differences between two groups of nails to determine if their chemical profiles are statistically distinct.

### 2. Factor Analysis of Salesperson Performance

This study uses factor analysis to identify underlying factors linking sales performance and aptitude test scores in 50 salespeople. Performance measures include sales growth, profitability, and new accounts. Aptitude tests cover creativity, mechanical reasoning, abstract reasoning, and mathematics. The analysis compares two- and three-factor models, examining factor loadings, model fit, and predictive ability for a new salesperson.

### 3. Discriminant Analysis of Cod Populations

This study utilizes discriminant analysis to classify cod as either coastal or arctic based on elliptic Fourier coefficients of their otolith shapes. The analysis aims to develop and evaluate classification rules, considering potential differences in misclassification costs.

### 4. K-means Clustering of Iris Data with PCA

This notebook explores the effectiveness of k-means clustering in classifying the Iris dataset, which contains data on three species of Iris flowers. The analysis focuses on using three clusters in k-means, corresponding to the known number of species.



Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
