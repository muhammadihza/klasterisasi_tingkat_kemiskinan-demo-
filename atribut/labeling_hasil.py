import streamlit as st
import numpy as np

def labeling_result(n, df):
    labels = []

    for i in range(n):
        huruf = chr(65 + i)
        label = st.text_input(f"Masukkan label untuk klaster {i+1} (misalkan {huruf}):")
        labels.append(label)

    if "" in labels:
        st.warning("Mohon isi semua label klaster sebelum melanjutkan.")
        return df

    df['Cluster'] = df['Cluster'].astype('object')  # agar bisa terima string

    for i in range(n):
        df.loc[df['Cluster'] == i, 'Cluster'] = labels[i]

    return df
