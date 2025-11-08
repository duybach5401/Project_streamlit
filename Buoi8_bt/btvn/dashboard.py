import streamlit as st 

st.set_page_config(layout="wide")
st.title("Bảng điều khiển doanh thu cửa hàng")
st.caption("Theo dõi doanh thu, đơn hàng, khách hàng và sản phẩm bán chạy")

#sidebar
st.sidebar.title("Trình quản lý cửa hàng")
st.sidebar.header("Menu chính")
st.sidebar.write("Bảng điều khiển")

st.sidebar.page_link("dashboard.py", label="🏠 Trang chủ")
st.sidebar.page_link("pages/add_product.py",label="Thêm sản phẩm")
st.sidebar.page_link("pages/don_hang.py",label="Báo cáo bán hàng")
st.sidebar.page_link("pages/doanh_thu.py",label="Doanh thu & Lợi nhuận")
st.sidebar.page_link("pages/khach_hang.py",label="Nhân viên và khách hàng")

st.sidebar.divider()
st.sidebar.write("Đăng nhập: Quản lý - Đăng Duy Bách")
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
col1,col2,col3,col4, = st.columns(4)

with col1:
    st.success("Doanh thu tháng này")
    st.metric("Tổng doanh thu", "856,000,000 VND", "+12%")
    st.page_link("pages/doanh_thu.py",label="Xem chi tiết doanh thu")
    # st.markdown('<div style="background-color: #d7f3d7; padding: 15px; border-radius: 8px; height: 150px;"></div>', True)
with col2:
    st.warning("Đơn hàng")
    st.metric("Số đơn hàng", "1254", "+8%")
    st.page_link("pages/don_hang.py",label="Xem chi tiết đơn hàng")

with col3:
    st.info("Khách hàng mới")
    st.metric("Khách hàng đăng ký mới", "327", "+5%")
    st.page_link("pages/khach_hang.py",label="Xem chi tiết khách hàng")

with col4:
    st.error("Sản phảm bán chạy")
    st.metric("Số sản phẩm bán ra", "15430", "-3%")
    st.page_link("pages/doanh_thu.py",label="Xem chi tiết doanh thu")

st.markdown("<hr/>", True)

#2 cột chart
col5,col6 = st.columns(2)

with col5:
    st.header("Biểu đồ doanh thu theo ngày")
    lst_doanh_thu = [58_000_000, 30_000_000, 65_000_000, 38_000_000, 59_000_000, 20_000_000, 70_000_000]
    st.area_chart(lst_doanh_thu)

with col6:
    st.header("Biểu đồ doanh thu 6 tháng gần nhất")
    lst_dtthang = [500,620,710,790,850,900]
    st.bar_chart(lst_dtthang)

st.divider()

#Table data
st.title("TOP 5 SẢN PHẨM BÁN CHẠY")
st.text_input("Tìm sản phẩm:")

if "lst_sp" not in st.session_state:
    st.session_state.lst_sp = [
        {"Tên sản phẩm": "Áo thun nam cổ tròn", "Số lượng bán": 3200, "Danh mục": "Quần áo", "Giá bán": "250,000 VND", "Tình trạng": "Còn hàng"},
        {"Tên sản phẩm": "Giày sneaker nữ trắng", "Số lượng bán": 2850, "Danh mục": "Giày dép", "Giá bán": "650,000 VND", "Tình trạng": "Còn hàng"},
        {"Tên sản phẩm": "Balo laptop 15 inch", "Số lượng bán": 2100, "Danh mục": "Phụ kiện", "Giá bán": "480,000 VND", "Tình trạng": "Còn hàng"},
        {"Tên sản phẩm": "Tai nghe Bluetooth T5", "Số lượng bán": 1900, "Danh mục": "Điện tử", "Giá bán": "850,000 VND", "Tình trạng": "Còn hàng"},
        {"Tên sản phẩm": "Áo somi caro nữ", "Số lượng bán": 1630, "Danh mục": "Quần áo", "Giá bán": "290,000 VND", "Tình trạng": "Sắp hết hàng"}
    ]

st.table(data=st.session_state.lst_sp)

st.divider() #== st.markdown("<hr/>", True)





