import streamlit as st 

st.set_page_config(layout="wide")
st.title("Admin Dashboard")


# Sidebar
st.sidebar.title ("Menu")

# seclect_menu_item = st.sidebar.radio ("Điều hướng", ["Trang chủ", "Báo cáo", "Người dùng", "Cài đặt"])
st.sidebar.write("app.py", label="Điều hướng")
st.sidebar.page_link("pages/bt_ontap.py") 
st.sidebar.page_link("pages/bao_cao.py",label="Báo cáo")
st.sidebar.page_link("pages/cai_dat.py",label="Cài đặt")
st.sidebar.page_link("pages/nguoi_dung.py",label="Người dùng")
st.sidebar.page_link("pages/bt2_menu.py",label="Menu KFC")

#Ẩn phần điều hướng ở trên sidebar 
st.markdown("""
    <style>
        [data-testid="stSidebarNav"] {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)
#Content page

#4 cột metric
with st.container():
    col1,col2,col3,col4 = st.columns(4)
    
    with col1:
        st.metric("Doanh thu hôm nay", "đ 12,5M","+5%")
        st.metric(label="Doanh thu hôm nay",value="12,5 M",delta="+ 5%") #Cách viết tường minh
    with col2:
        st.metric("Người dùng mới", "327","+12%")
    with col3:
        st.metric("Đơn hàng", "142","-3%")
    with col4:
        st.metric("Tỉ lệ chuyển đổi","3,8%", "+0.4")

st.markdown("<hr/>",True)

# 2 cột chart
with st.container():
    col5,col6 = st.columns(2)
    with col5:
        st.header("Doanh thu 7 ngày gần nhất")
        lst_doanh_thu = [6,14,5,15,10]
        st.line_chart(lst_doanh_thu)
    with col6:
        st.header("Số lượng đơn hàng theo trạng thái")
        lst_don_hang= [15,35,59,69]
        st.bar_chart(lst_don_hang)
        
       
