from pathlib import Path

def artifacts_available(model_dir="models"):
    p = Path(model_dir)
    return (p/"odir_rf_ovr.joblib").exists() and (
        (p/"resnet50_feat_model.keras").exists() or
        (p/"resnet50_feat_model.h5").exists()
    )
