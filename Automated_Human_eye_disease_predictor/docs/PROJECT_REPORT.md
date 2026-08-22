# Project Report

## Automated Retinal Disease Screening

This project restructures the original ODIR notebook into a maintainable ML showcase.

### Dataset
`full_df.csv` contains 6,392 metadata records and 19 columns.

### Method
ResNet50 feature extraction is applied to bilateral fundus images. Image representations are combined with patient age and sex and classified using a One-vs-Rest Random Forest.

### Output
Eight labels: N, D, G, C, A, H, M, O.

The original notebook remains the source of truth for training and evaluation.
