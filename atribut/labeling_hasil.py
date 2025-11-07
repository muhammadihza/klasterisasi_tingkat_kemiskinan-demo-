import streamlit as st
import numpy as np

def labeling_result(n, df):
    
    labels = []

    for i in range(n):
        huruf = chr(65 + i)  # Mengonversi indeks ke huruf (A, B, C, ...)
        label = st.text_input(f"Masukkan label untuk klaster {i+1} (misalkan {huruf}):")
        labels.append(label)

    df['Cluster'] = df['Cluster'].astype('object')
    
    conditions = [(df['Cluster'] == i) for i in range(n)]
    choices = labels[:n]
    
    df['Cluster'] = np.select(conditions, choices)

    return df
