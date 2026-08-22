import argparse

parser = argparse.ArgumentParser(description="Evaluation entry point")
parser.add_argument("--data-dir", required=True)
args = parser.parse_args()

print("Evaluation dataset:", args.data_dir)
print("See notebooks/ML_Project.ipynb for the original evaluation workflow.")
