import streamlit as st 
import json 

if "lst_sp" not in st.session_state:
    st.session_state.lst_sp = [
        {"Tên sản phẩm": "Áo thun nam cổ tròn", "Số lượng bán": 3200, "Danh mục": "Quần áo", "Giá bán": "250,000 VND", "Tình trạng": "Còn hàng"},
        {"Tên sản phẩm": "Giày sneaker nữ trắng", "Số lượng bán": 2850, "Danh mục": "Giày dép", "Giá bán": "650,000 VND", "Tình trạng": "Còn hàng"},
        {"Tên sản phẩm": "Balo laptop 15 inch", "Số lượng bán": 2100, "Danh mục": "Phụ kiện", "Giá bán": "480,000 VND", "Tình trạng": "Còn hàng"},
        {"Tên sản phẩm": "Tai nghe Bluetooth T5", "Số lượng bán": 1900, "Danh mục": "Điện tử", "Giá bán": "850,000 VND", "Tình trạng": "Còn hàng"},
        {"Tên sản phẩm": "Áo somi caro nữ", "Số lượng bán": 1630, "Danh mục": "Quần áo", "Giá bán": "290,000 VND", "Tình trạng": "Sắp hết hàng"}
    ]
sp = {}


st.set_page_config(layout="wide")
st.title ("TOP 5 SẢN PHẨM BÁN CHẠY NHẤT")

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
# Ẩn phần điều hướng ở trên sidebar 
st.markdown("""
    <style>
        [data-testid="stSidebarNav"] {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)


#Thêm sản phẩm mới
with st.expander("Thêm mặt hàng mới", True):
    frm = st.form("frm")
    with frm:
        sp['Tên sản phẩm'] = st.text_input("Tên sản phẩm mới")
        sp['Số lượng bán'] = st.number_input("Số lượng bán", max_value=10000, min_value=0)
        sp['Danh mục'] = st.selectbox("Danh mục", [
            "Quần áo", "Giày dép", "Phụ kiện", "Điện tử"
        ])
        sp['Giá bán'] = st.text_input("Giá bán (VD: 250,000 VND)")
        sp['Tình trạng'] = st.selectbox("Tình trạng", [
            "Còn hàng", "Sắp hết hàng", "Hết hàng"
        ])

        submit_button = st.form_submit_button("Thêm mặt hàng")
         

#Lưu file data sản phẩm
if submit_button:
    if sp['Tên sản phẩm'] != "" and sp['Giá bán'] != "":
        st.session_state.lst_sp.append(sp)
        st.success("Đã thêm vào danh sách sản phẩm")
       
    else:
        st.error("Vui lòng điền đầy đủ tên sản phẩm và giá bán")
#lưu dữ liệu người dùng vào jsson file
with open ("data_sp.json", "w", encoding="utf-8") as json_file: 
    json.dump(st.session_state.lst_sp,json_file, ensure_ascii=False)

st.divider()
st.text_input("Tìm sản phẩm:")

st.table(data=st.session_state.lst_sp)


