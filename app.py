import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from fetcher import fetch_posts
from sentiment import analyze_sentiments
from config import MODEL_ID, AWS_REGION


def main():
    st.set_page_config(page_title="Social Listening Tool", layout="wide")
    st.title("📊 Social Listening Dashboard")
    st.markdown(
        """
        Enter a topic or keyword to fetch recent social media posts, analyze sentiment,
        and generate a quick report with example posts and charts.
        """
    )

    # Sidebar controls
    with st.sidebar:
        keyword = st.text_input("Keyword or Theme", value="AI agent employment impact")
        limit   = st.slider("Number of posts to analyze", 20, 200, 100)
        show_raw = st.checkbox("Show raw DataFrame", value=False)
        generate = st.button("Analyze now")

    if generate and keyword:
        with st.spinner("Fetching posts & analyzing sentiments (~15-20 min)..."):
            df = fetch_posts(keyword, limit)
            df['sentiment'] = analyze_sentiments(df['text'].tolist())

        # Compute shares
        pos_share = (df['sentiment'] == 'POSITIVE').mean()
        neg_share = (df['sentiment'] == 'NEGATIVE').mean()

        # Plot
        fig, ax = plt.subplots()
        ax.bar(['Positive', 'Negative'], [pos_share, neg_share])
        ax.set_ylabel('Share')
        ax.set_ylim(0, 1)
        st.subheader(f"Sentiment Share for '{keyword}'")
        st.pyplot(fig)

        # Optional raw data
        if show_raw:
            st.subheader("Raw Data")
            st.dataframe(df)

        # Display examples
        st.subheader("Sample Positive Posts")
        for t in df[df['sentiment']=='POSITIVE']['text'].head(5):
            st.write(f"- {t}")

        st.subheader("Sample Negative Posts")
        for t in df[df['sentiment']=='NEGATIVE']['text'].head(5):
            st.write(f"- {t}")

        st.markdown("---")
        st.caption("*Report generated via Streamlit + AWS Bedrock (Nova Micro/Lite)*")

if __name__ == '__main__':
    main()
