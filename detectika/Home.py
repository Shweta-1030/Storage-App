import streamlit as st

st.title('DETECTIKA DOCUMENTATION')
st.markdown("""
NSEIT brings the power of fraud detection directly to your Snowflake account. Using Streamlit and Snowpark, the application enables you to detect fraudulent credit card transactions with no need to transfer files or share data outside of your Snowflake Data Cloud.

Using the fraud detection model built by NSEIT which is trained over 100k publicly available credit card transactions, the client can detect fraud using batch mode.

To experience the application using your own first-party data please see the expected workflow below.

Expected workflow for client specific outputs:

1. Customer sends email to NSEIT at: sample@nseit.com with the following information.
\n\n-type of transactions
\n\n-transaction table metadata ( for identifying customer specific features )

2. NSEIT will access client data and run it against NSEIT's proprietary algorithm to generate client specific machine learning model. (Estimated time to deliver is 20 business days)

3. NSEIT will notify client when they are able to run the application in their account to generate their client specific outputs.


Business Benefits

Batch mode fraud detection
- Analyze the fraudlent transactions from client specific historical data

Accelerated predictions
- making use of NSEIT's proprietary machine learning algorithm the client can start predicting fraud in no time

Zero development 
- The client does not have to handle any development activities as it is entirely handled by the NSEIT team

Security
- Consumer data is kept private and secure. After the app is installed, it is recommended by the provider to grant the following privileges as needed.
""")
