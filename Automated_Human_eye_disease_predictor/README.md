# ODIR Eye Disease AI

**End-to-end retinal disease screening showcase using ResNet50 transfer learning, bilateral fundus features, patient metadata, and One-vs-Rest Random Forest classification.**

> Academic/research demonstration only. This project is not a medical diagnostic device.

## Overview

This repository restructures the original Jupyter notebook into a clean, GitHub-ready machine-learning project.

**Pipeline**

```text
Left Fundus + Right Fundus
          |
       ResNet50
          |
Global Average Pooling
          |
Bilateral Feature Fusion
          |
Age + Sex Metadata
          |
One-vs-Rest Random Forest
          |
8 Ocular Disease Labels
```

## Labels

| Code | Disease |
|---|---|
| N | Normal |
| D | Diabetic Retinopathy |
| G | Glaucoma |
| C | Cataract |
| A | Age-related Macular Degeneration |
| H | Hypertension |
| M | Pathological Myopia |
| O | Other Abnormality |

## Dataset

The included `data/full_df.csv` contains **6,392 rows** and **19 columns**.

It contains patient information, left/right fundus filenames, diagnostic keywords, labels, target vectors, and file paths.

The original retinal images are **not included** because of their large size.

## Model

The original notebook uses:

- ImageNet-pretrained ResNet50
- `224 x 224 x 3` input
- Global Average Pooling
- Bilateral eye feature fusion
- Age and sex metadata
- One-vs-Rest Random Forest

Recorded notebook feature representation: **6392 x 4098**.

Recorded split: **5113 train / 1279 test**.

## Repository

```text
.
├── app.py
├── README.md
├── requirements.txt
├── Dockerfile
├── LICENSE
├── .gitignore
├── notebooks/
│   └── ML_Project.ipynb
├── data/
│   ├── full_df.csv
│   └── README.md
├── src/
├── scripts/
├── assets/
├── docs/
└── models/
```

## Run the showcase

```bash
pip install -r requirements.txt
streamlit run app.py
```

The Streamlit interface presents the project methodology and dataset information. Since trained model artifacts are not included, it does not falsely claim live prediction.

## Reproduce training

After obtaining the original retinal image dataset:

```bash
python scripts/train.py --data-dir /path/to/ODIR-5K
```

The original notebook is preserved at `notebooks/ML_Project.ipynb`.

## Technologies

Python • TensorFlow/Keras • ResNet50 • scikit-learn • Random Forest • OpenCV • Pandas • Streamlit

## Author

**Suraj Ahirwar**
