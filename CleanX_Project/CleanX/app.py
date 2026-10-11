import os
import pandas as pd
import streamlit as st
from cleaner import profile_data, clean_data, build_quality_report

st.set_page_config(page_title="CleanX | Smart Data Cleaning", page_icon="🧹", layout="wide")
st.markdown("""
<style>
.block-container{padding-top:2rem;max-width:1200px}
.hero{padding:1.5rem 1.7rem;border-radius:18px;background:linear-gradient(120deg,#eff6ff,#f5f3ff);border:1px solid #e0e7ff;margin-bottom:1.2rem}
.hero h1{margin:0;color:#172554;font-size:2.4rem}.hero p{margin:.5rem 0 0;color:#475569}
div[data-testid="stMetric"]{background:white;border:1px solid #e2e8f0;padding:1rem;border-radius:12px}
</style>
<div class="hero"><h1>🧹 CleanX</h1><p>Smart Data Cleaning Tool · Inspect, clean, and export CSV datasets with confidence.</p></div>
""", unsafe_allow_html=True)
st.write("Upload a CSV file to review data quality, choose cleaning options, and download a cleaned version.")
uploaded_file = st.file_uploader("Upload your CSV dataset", type=["csv"])

if uploaded_file is None:
    st.info("No file uploaded yet. Start with the included sample_data.csv file.")
    sample_path = os.path.join(os.path.dirname(__file__), "sample_data.csv")
    if os.path.exists(sample_path):
        with open(sample_path, "rb") as sample_file:
            st.download_button("⬇️ Download sample CSV", sample_file, file_name="sample_data.csv", mime="text/csv")
    st.markdown("### What CleanX can do")
    c1, c2, c3 = st.columns(3)
    c1.markdown("**🔎 Data profiling**\n\nRows, columns, missing cells, and duplicate rows.")
    c2.markdown("**🧼 Flexible cleaning**\n\nRemove duplicates and handle missing values.")
    c3.markdown("**📄 Quality report**\n\nCompare dataset quality before and after cleaning.")
    st.stop()

try:
    raw_df = pd.read_csv(uploaded_file)
except Exception as error:
    st.error(f"Could not read this CSV file: {error}")
    st.stop()

st.subheader("1. Dataset preview")
st.dataframe(raw_df.head(100), use_container_width=True, hide_index=True)
before = profile_data(raw_df)
cols = st.columns(4)
cols[0].metric("Rows", f"{before['rows']:,}")
cols[1].metric("Columns", f"{before['columns']:,}")
cols[2].metric("Missing cells", f"{before['missing_cells']:,}")
cols[3].metric("Duplicate rows", f"{before['duplicate_rows']:,}")

with st.expander("View missing values by column"):
    missing_table = pd.DataFrame({
        "Column": before["missing_by_column"].index,
        "Missing values": before["missing_by_column"].values,
        "Missing %": (before["missing_by_column"].values / max(len(raw_df), 1) * 100).round(2)
    })
    st.dataframe(missing_table, use_container_width=True, hide_index=True)

st.subheader("2. Choose cleaning options")
left, right = st.columns(2)
with left:
    remove_duplicates = st.checkbox("Remove duplicate rows", value=True)
    trim_text = st.checkbox("Trim extra spaces from text", value=True)
with right:
    missing_strategy = st.selectbox("Handle missing values", [
        "Keep missing values", "Drop rows with any missing value",
        "Fill text with 'Unknown' and numbers with median", "Fill all missing values with 0"
    ])
    st.caption("Review your data before choosing a strategy; different datasets need different rules.")

if st.button("✨ Clean dataset", type="primary", use_container_width=True):
    cleaned_df, changes = clean_data(raw_df, remove_duplicates, trim_text, missing_strategy)
    st.session_state["cleaned_df"] = cleaned_df
    st.session_state["changes"] = changes
    st.session_state["source_name"] = uploaded_file.name.rsplit(".", 1)[0]

if "cleaned_df" in st.session_state:
    cleaned_df = st.session_state["cleaned_df"]
    changes = st.session_state["changes"]
    after = profile_data(cleaned_df)
    st.subheader("3. Cleaning results")
    cols = st.columns(4)
    cols[0].metric("Rows after cleaning", f"{after['rows']:,}", delta=f"{after['rows'] - before['rows']:,} rows")
    cols[1].metric("Missing cells after", f"{after['missing_cells']:,}", delta=f"{after['missing_cells'] - before['missing_cells']:,}")
    cols[2].metric("Duplicate rows after", f"{after['duplicate_rows']:,}", delta=f"{after['duplicate_rows'] - before['duplicate_rows']:,}")
    cols[3].metric("Changes recorded", f"{len(changes):,}")
    st.dataframe(cleaned_df.head(100), use_container_width=True, hide_index=True)
    st.subheader("4. Download results")
    csv_bytes = cleaned_df.to_csv(index=False).encode("utf-8")
    report_bytes = build_quality_report(raw_df, cleaned_df, changes).to_csv(index=False).encode("utf-8")
    a, b = st.columns(2)
    with a:
        st.download_button("⬇️ Download cleaned CSV", csv_bytes,
                           file_name=f"{st.session_state.get('source_name', 'dataset')}_cleaned.csv",
                           mime="text/csv", use_container_width=True)
    with b:
        st.download_button("⬇️ Download quality report", report_bytes,
                           file_name=f"{st.session_state.get('source_name', 'dataset')}_quality_report.csv",
                           mime="text/csv", use_container_width=True)
    with st.expander("View cleaning log"):
        if changes:
            st.dataframe(pd.DataFrame(changes), use_container_width=True, hide_index=True)
        else:
            st.write("No changes were required or selected for this dataset.")
