import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="ODIR Eye Disease AI", page_icon="👁️", layout="wide")

st.title("👁️ ODIR Eye Disease AI")
st.caption("Retinal disease screening — research showcase")
st.warning("Academic/research demonstration only. Not for clinical diagnosis.")

p1, p2, p3 = st.columns(3)
p1.metric("Feature Extractor", "ResNet50")
p2.metric("Classifier", "Random Forest")
p3.metric("Output Labels", "8")

tab1, tab2 = st.tabs(["Methodology", "Dataset"])

with tab1:
    st.subheader("Pipeline")
    st.markdown(
        "**Bilateral Fundus Images → ResNet50 → Global Average Pooling → "
        "Feature Fusion → Age + Sex → One-vs-Rest Random Forest → 8 Labels**"
    )
    st.markdown(
        "**Labels:** N, D, G, C, A, H, M, O\n\n"
        "The original notebook contains the complete training and evaluation "
        "workflow. Trained model files are intentionally not bundled."
    )

with tab2:
    path = Path("data/full_df.csv")
    if path.exists():
        df = pd.read_csv(path)
        st.write(f"**{len(df):,} rows × {len(df.columns)} columns**")
        st.dataframe(df.head(10), use_container_width=True)
    else:
        st.info("Dataset metadata not found.")
