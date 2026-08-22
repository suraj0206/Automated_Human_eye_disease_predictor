# ODIR Eye Disease AI

A deep learning-based retinal disease screening system built using ResNet50 transfer learning and One-vs-Rest Random Forest classification. The system combines bilateral fundus images with patient metadata to predict eight ocular disease categories.

## 🚀 Demo

![ODIR Eye Disease AI](assets/sample_prediction.png)

> Academic/portfolio project demonstrating medical AI, computer vision, transfer learning, and multi-label classification.

---

## 📌 Project Overview

Retinal disease detection is an important computer vision task that aims to identify ocular abnormalities from fundus photographs.

This project formulates retinal disease prediction as a multi-label classification problem. A pretrained ResNet50 network is used to extract visual features from left and right fundus images. These image features are combined with patient-level metadata such as age and sex and passed to a One-vs-Rest Random Forest classifier.

### Input

- Left-eye fundus image
- Right-eye fundus image
- Patient age
- Patient sex

### Output

- 8 ocular disease categories
- Multi-label disease predictions
- Prediction probabilities for each category

---

## 🧠 Model Architecture

```text
Left Fundus Image ─────┐
                       │
                       ▼
                    ResNet50
                       │
                       ▼
             Global Average Pooling
                       │
                       ▼
              Left-eye Features
                       │
                       │
Right Fundus Image ────┐
                       │
                       ▼
                    ResNet50
                       │
                       ▼
             Global Average Pooling
                       │
                       ▼
             Right-eye Features
                       │
                       │
                       ▼
              Feature Concatenation
                       │
                       ▼
             Age + Sex Metadata
                       │
                       ▼
             Patient Feature Vector
                       │
                       ▼
          One-vs-Rest Random Forest
                       │
                       ▼
             8 Disease Predictions
