import streamlit as st 
import polars as pl
import pandas as pd

# Title of the app landing page

st.title =('CSV to Polars DataFrame with Streamlit')
uploadedFile = st.file_uploader('Upload a CSV File', type = ['csv'])

if uploadedFile is not None:
    # Read the file into a Pandas Dataframe:
    pandas_df = pd.read_csv(uploadedFile)

    # Convert to Polars Dataframe:
    df = pl.DataFrame(pandas_df)

    # Display the DataFrame:
    st.write('Uploaded Polars Dataframe')
    st.dataframe(df.to_pandas())

    # Add elements for interactivity
    st.write('Interactive Filters')

    # Get column names
    column_names = df.columns

    # Assuming the user wants to filter based on the first column

    if column_names:
        min_value = st.slider(f'Minimum value for {column_names[0]}', int(df[column_names[0]].min()), int(df[column_names[0]].max()), int(df[column_names[0]].min()))
        max_value = st.slider(f'Maximum value for {column_names[0]}', int(df[column_names[0]].min()), int(df[column_names[0]].max()), int(df[column_names[0]].max()))

        # Filter dataframe based on slider input:
        filtered_df = df.filter((pl.col(column_names[0]) >= min_value) & (pl.col(column_names[0]) <= max_value))

        st.write('Filtered Polars Dataframe')
        st.dataframe(filtered_df.to_pandas())
    else:
        st.write("Please upload a file.")
