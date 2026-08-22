LABEL_NAMES = ["N", "D", "G", "C", "A", "H", "M", "O"]

def describe_pipeline():
    return {
        "feature_extractor": "ResNet50",
        "pooling": "GlobalAveragePooling2D",
        "classifier": "OneVsRestClassifier(RandomForestClassifier)",
        "labels": LABEL_NAMES,
    }
