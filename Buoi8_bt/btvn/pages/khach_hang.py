import streamlit as st 
import time

st.set_page_config(layout="wide")


#sidebar
st.sidebar.title("Trình quản lý cửa hàng")
st.sidebar.header("Menu chính")
st.sidebar.write("Bảng điều khiển")

st.sidebar.page_link("dashboard.py", label="🏠 Trang chủ")
st.sidebar.page_link("pages/add_product.py",label="Thêm mặt hàng")
st.sidebar.page_link("pages/don_hang.py",label="Báo cáo bán hàng")
st.sidebar.page_link("pages/doanh_thu.py",label="Doanh thu & Lợi nhuận")
st.sidebar.page_link("pages/khach_hang.py",label="Nhân viên và khách hàng")
# #Ẩn phần điều hướng ở trên sidebar 
st.markdown("""
    <style>
        [data-testid="stSidebarNav"] {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)

