import streamlit as st
# Import Fungsi

from halaman.hal_utama import main_page as main_page
from halaman.hal_logout import logout_page as logout_page


main_page()

with st.sidebar:
    st.markdown('---')
    st.button("Logout", on_click=logout_page)



# Inisialisasi penanda halaman

# if 'current_page' not in st.session_state:
#     st.session_state.current_page = "page_one"


# if st.session_state.current_page == "page_one":
#     login_page()

# elif st.session_state.current_page == "page_two":
#     register_page()

# elif st.session_state.current_page == "page_three":
#     main_page()
    
   
#     with st.sidebar :
#         st.markdown('---')
#         st.button("Logout", on_click=logout_page)
            