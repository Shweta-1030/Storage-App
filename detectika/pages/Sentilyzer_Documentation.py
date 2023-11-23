import streamlit as st

st.set_page_config(layout="wide")

st.title('SENTILYZER DOCUMENTATION')

st.header('Introduction')
st.markdown("""
NSEIT brings the power of sentiment analysis directly to your Snowflake account. Using Streamlit and Snowpark, the application enables you to detect sentiment from user feedback or reviews with no need to transfer files or share data outside of your Snowflake Data Cloud. The application also provides visualizations in the streamlit interface.

Using the sentiment analysis model built by NSEIT which is trained over publicly available user reviews, the client can detect sentiment using batch mode.

To experience the application using your own first-party data please see the expected workflow below.

""")

st.header('Description')
st.subheader('Business Benefits:')
st.markdown("""
Batch mode sentiment detection
- Analyze the sentiments of user feedback/reviews from client specific historical data.

Accelerated predictions
- Making use of NSEIT's proprietary machine learning algorithm the client can start performing sentiment analysis in no time.

Inbuilt Visualization
- The application contains visualizations like sentiment over time, word cloud in the streamlit interface.

Zero development
- The client does not have to handle any development activities as it is entirely handled by the NSEIT team.

Security
- Consumer data is kept private and secure. After the app is installed, it is recommended by the provider to grant the following privileges as needed.
""")

st.header('Steps to Use')
st.subheader('Expected workflow for client specific outputs:')
st.markdown("""
1. Customer installs the application from snowflake marketplace

2. Customer can start using the application for sentiment analysis. A sample dataset is provided as part of the application.

3. Customer provides SELECT access to the table containing the user reviews/feedback for the streamlit application.
""")

st.header('Sample Queries')
code = '''select PRODUCT_REVIEW, 
predict_sentiment_vect(PRODUCT_REVIEW) as SENTIMENT 
from SENTILYZER.CODE_SCHEMA.NEW_REVIEWS'''
st.code(code, language='sql')
