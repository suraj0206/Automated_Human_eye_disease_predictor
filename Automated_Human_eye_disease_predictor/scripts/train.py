import argparse

parser = argparse.ArgumentParser(description="Training entry point for ODIR Eye Disease AI")
parser.add_argument("--data-dir", required=True)
parser.add_argument("--model-dir", default="models")
args = parser.parse_args()

print("Dataset:", args.data_dir)
print("Model output:", args.model_dir)
print("Use notebooks/ML_Project.ipynb for the complete original training workflow.")
