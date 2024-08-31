import streamlit as st
import requests
import sys
sys.path.append('D:\DS-Industrial-Workshop\Final Project\iiuc-industrial-training-49-main (1)\iiuc-industrial-training-49-main\session-2\streamlit-app')
from utils import get_news_list, get_summary_by_id

#def app():
st.title("Summary Page")

news_list = get_news_list()
news_titles = {news['title']: news for news in news_list}
selected_title = st.selectbox("Select News Title", list(news_titles.keys()))

if selected_title:
    news = news_titles[selected_title]
    st.write(news['id'])
    st.write(news['title'])
    st.write(news['body'])
    st.write(f"Link: {news['link']}")
    st.write(f"Date: {news['datetime']}")
    st.write(f"Category: {news['category']}")
    st.write(f"Reporter: {news['reporter']}")
    st.write(f"Publisher: {news['publisher']}")

if st.button("Generate Summary", type='primary'):
            # Fetch summary using the actual news ID
        summary = get_summary_by_id(news['id'])
        
        if summary:
            # Ensure 'summary_text' key exists
            if 'summary_text' in summary:
                st.write("**Summary:**")
                st.write(summary['summary_text'])
            else:
                st.write("Summary text not available.")
        else:
            st.write("No summary generated.")