import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from datetime import date

# Fungsi
from atribut.mark import simple_mark as sm
from atribut.expander import expander as expander
from halaman.page.hal_detaildata import detaildata_page as detaildata_page
from halaman.page.hal_klasterisasi import klaster_page as klaster_page
from halaman.page.hal_dashboard import dashboard_page as dashboard_page



today = date.today()

def main_page():

    st.set_page_config(page_title="Data", page_icon='📈')

    with st.sidebar:
        st.write("SELAMAT DATANG!! 😃")
        st.write("Tanggal hari ini : ", today)
        st.markdown('---')




    # --------------------- Konten Utama ---------------------------------
    if "halaman" not in st.session_state:
        st.session_state["halaman"] = 0

    with st.sidebar:
        selected = option_menu(
            menu_title="Halaman Menu",
            options=["Data", "Detail Data", "Klasterisasi", "Dashboard"]
        )



    # ------------------------------ Konten Halaman Data ------------------------------
    if selected == "Data" :

        st.title('Data📈')
        st.subheader('Silahkan Masukkan Dataset')

        if 'jenisData' not in st.session_state:
            st.session_state.jenisData = ''

        opsi_input_data = st.selectbox(
        'Pilih jenis data yang ingin diinputkan :',
        ('1. Data Acak', '2. Data Kemiskinan', '3. Data Uji Coba'))

        sm()

        if opsi_input_data == '1. Data Acak':

            st.session_state.jenisData = 'DataAcak'

            uploaded_file = st.file_uploader('Masukkan file dengan **format csv**', type='csv')


            if uploaded_file:

                df = pd.read_csv(uploaded_file)
                st.markdown('---')

                proses = st.button("Proses")

                if proses:

                    st.session_state["page"] = 1

                    if "upload_file" not in st.session_state:
                        st.session_state.upload_file = ""

                    st.session_state.upload_file = df


                    st.session_state["halaman"] = 1
                    st.success('Berhasil Memasukkan File!', icon="✅")



        if opsi_input_data == '2. Data Kemiskinan':

            st.session_state.jenisData = 'DataKemiskinan'
           
            uploaded_file = st.file_uploader('Masukkan file dengan **format csv**', type='csv')

            if uploaded_file:

                df = pd.read_csv(uploaded_file)
                st.warning('**🚨PENTING!!** Pastikan file data yang dimasukkan memiliki **format csv**, dan dengan **atribut/kolom** yang sesuai')

                st.markdown('---')

                proses = st.button("Proses")

                if proses:

                    st.session_state["page"] = 1

                    if "upload_file" not in st.session_state:
                        st.session_state.upload_file = ""

                    st.session_state.upload_file = df

                    arr1 = df.columns.tolist()
                    arr2 = ['Nama', 'Penghasilan(jt)', 'Jumlah Anggota Keluarga', 'Tingkat Pendidikan', 'Dinding Rumah', 'Lantai Rumah', 'Atap Rumah', 'Sumber Penerangan(VA)', 'Luas Lantai Rumah(m2)', 'Sumber Mata Air', 'Pengeluaran Kebutuhan Pangan', 'Pengobatan Tenaga Medis', 'Pembelian Pakaian(/tahun)', 'Kecamatan']
                            

                    if arr1 == arr2:

                        st.session_state["halaman"] = 1
                        st.success('Berhasil Memasukkan File!', icon="✅")

                                
                    else:
                        st.error('🚨Atribut atau Kolom Tidak Sama')
                        st.write('Kolom Atribut yang dimasukkan:',arr1,'Kolom Atribut yang dibutuhkan',arr2)
                        st.info('Silahkan memasukkan file dengan **Atribut/Kolom** yang sesuai')   

        if opsi_input_data == '3. Data Uji Coba':

            st.session_state.jenisData = 'DataKemiskinan'
           
            # uploaded_file = st.file_uploader('Masukkan file dengan **format csv**', type='csv')
            uploaded_file = st.button('Input Data Uji Coba')
            
            if uploaded_file:
                
                df = pd.read_csv('data/dataset_11(11 atribut).csv')
                st.session_state["page"] = 1

                if "upload_file" not in st.session_state:
                    st.session_state.upload_file = ""

                st.session_state.upload_file = df

                arr1 = df.columns.tolist()
                arr2 = ['Nama', 'Penghasilan(jt)', 'Jumlah Anggota Keluarga', 'Tingkat Pendidikan', 'Dinding Rumah', 'Lantai Rumah', 'Atap Rumah', 'Sumber Penerangan(VA)', 'Luas Lantai Rumah(m2)', 'Sumber Mata Air', 'Pengeluaran Kebutuhan Pangan', 'Pengobatan Tenaga Medis', 'Pembelian Pakaian(/tahun)', 'Kecamatan']
                            

                if arr1 == arr2:

                    st.session_state["halaman"] = 1
                    st.success('Berhasil Memasukkan File!', icon="✅")

                                
                else:
                    st.error('🚨Atribut atau Kolom Tidak Sama')
                    st.write('Kolom Atribut yang dimasukkan:',arr1,'Kolom Atribut yang dibutuhkan',arr2)
                    st.info('Silahkan memasukkan file dengan **Atribut/Kolom** yang sesuai')                     
                        
                         

        
    # ----------------------- Konten Halaman Detail Data -------------------------
    if selected == "Detail Data" :  
        
        if "hal_1" not in st.session_state:
            st.session_state.hal_1 = 0

        st.session_state.hal_1 = st.session_state["halaman"]
        
        if st.session_state.hal_1 != 1:
            st.warning('Belum Ada Data Saat ini 😥')

        else:

            if 'detail_data' not in st.session_state:
                st.session_state.detail_data = ""

            st.session_state.detail_data = st.session_state.upload_file

            df =  st.session_state.detail_data
            detaildata_page(df)
            

    # ---------------- Konten Halaman Klasterisasi --------------------
    if selected == "Klasterisasi": 

        # Identifikasi halaman dashboard
        if 'halaman2' not in st.session_state:
            st.session_state.halaman2 = 0

        # Identifikasi halaman klasterisasi
        if 'hal_page2' not in st.session_state:
            st.session_state.hal_page2 = 0

        st.session_state.hal_page2 = st.session_state["halaman"]

        if st.session_state.hal_page2 != 1:
            
            st.warning('Belum Ada Data Saat Ini 😥')


        else:
            
            klaster_page()
           

    # ---------------------- Konten Halaman Dashboard --------------------
    if selected == "Dashboard":
        
        # Mendefinisikan status halaman
        if 'hal_page3' not in st.session_state:
            st.session_state.hal_page3 = 0

        st.session_state.hal_page3 = st.session_state.halaman2


        # Status halaman
        if st.session_state.hal_page3 != 1:
            st.info('Silahkan Tentukan Nilai k Sebagai Nilai n Klaster pada Halaman Klasterisasi Terlebih Dahulu 😊')

        else:

            dashboard_page()