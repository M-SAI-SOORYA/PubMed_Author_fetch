import streamlit as st
import pandas as pd
from get_papers.fetch import fetch_pubmed_ids, fetch_pubmed_details
from get_papers.filter import filter_papers

st.title("📚 PubMed Paper Fetcher")

st.markdown("Fetch PubMed research papers with authors from pharmaceutical or biotech companies.")

# Sample queries
sample_queries = [
    "cancer immunotherapy",
    "covid-19 vaccine",
    "AI drug discovery",
    "CRISPR gene editing",
    "CAR-T cell therapy",
    "synthetic biology",
    "monoclonal antibodies",
    "Alzheimer's treatment",
    "oncology clinical trials",
    "diabetes drug development"
]

# UI components
query_select = st.selectbox("Choose a sample query (optional):", [""] + sample_queries)

if not query_select:
    query_input = st.text_input("Or type your own  query:")

filename = st.text_input("Enter a CSV filename (your wish) (e.g., papers.csv):")

# Choose final query
final_query = query_select.strip() if query_select else query_input

if st.button("🔍 Fetch Papers"):
    if final_query and filename:
        with st.spinner("Fetching papers..."):
            ids = fetch_pubmed_ids(final_query)
            details = fetch_pubmed_details(ids)
            filtered = filter_papers(details)
            df = pd.DataFrame(filtered)

            if df.empty:
                st.warning("No results found with non-academic affiliations.")
            else:
                csv = df.to_csv(index=False)
                st.success(f"✅ Fetched {len(df)} papers!")
                st.download_button(
                    label="⬇️ Download CSV",
                    data=csv,
                    file_name=filename,
                    mime="text/csv"
                )
    else:
        st.warning("Please enter a query and filename to continue.")
