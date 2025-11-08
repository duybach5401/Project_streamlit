import streamlit as st 

st.set_page_config(layout="wide")
st.title("MENU KFC MINI")


# Sidebar
st.sidebar.title ("Menu")

st.sidebar.write("Điều hướng")
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
#Dữ liệu các món ăn(st.session_state.lst_mon_an)
if "lst_mon_an" not in st.session_state:
    st.session_state.lst_mon_an = []

# Chọn món ăn
menu_gia = {
    "ga_ran": 35000,
    "burger": 45000,
    "khoai": 25000,
    "pepsi": 15000,
    "kem": 20000,
}

# menu_chon = {
#     "ga_ran": 1,
#     "burger": 1,
#     "khoai": 1,
#     "pepsi": 1,
#     "kem": 1,
# }
# Khởi session_state cho từng món (nếu chưa có)
for key in menu_gia.keys():
    if key not in st.session_state:
        st.session_state[key] = 0  # mặc định = 0

# Hàm reset (gán lại về 0)
def reset_all():
    for key in menu_gia.keys():
        st.session_state[key] = 0

# Nút reset ở đầu (không nằm trong form)
st.button("🔁 Reset chọn món", on_click=reset_all)
#Chia cột
col1,col2 = st.columns(2)

# CỘt chọn món
with col1:
    frm_mon_an = st.form("frm_mon_an")
    with frm_mon_an:
        st.header("Chọn món ăn: ")
        menu_chon = {}
        st.number_input("Gà rán (35,000 VND)", min_value=0, step=1, key="ga_ran", value=st.session_state["ga_ran"])
        st.number_input("Burger bò (45,000 VND)", min_value=0, step=1, key="burger", value=st.session_state["burger"])
        st.number_input("Khoai tây chiên (25,000 VND)", min_value=0, step=1, key="khoai", value=st.session_state["khoai"])
        st.number_input("Pepsi (15,000 VND)", min_value=0, step=1, key="pepsi", value=st.session_state["pepsi"])
        st.number_input("Kem vani (20,000 VND)", min_value=0, step=1, key="kem", value=st.session_state["kem"])

        st.markdown("<hr/>", True)
        st.text("Nhập số lượng món bạn muốn mua")
        button = st.form_submit_button("Tính tiền")
    
    
#Cột Hóa đơn
with col2: 
    st.header("Hóa đơn của bạn:")
    if button==True:
        lst_mon_an = []
        tong_cong = 0
        # Duyệt các món đã nhập (menu_chon có dữ liệu vì ta đã gán)
        for mon, don_gia in menu_gia.items():
            so_luong = st.session_state[mon] 
    
            if so_luong > 0:
                don_gia = menu_gia[mon]
                thanh_tien = don_gia * so_luong
                item= {
                "Món ăn": mon,
                "Đơn giá": f"{don_gia:,}",
                "Số lượng": so_luong,
                "Thành tiền": f"{thanh_tien:,}"
                }
                lst_mon_an.append(item)
                tong_cong += thanh_tien
    # st.table(lst_mon_an)

# Hiển thị bảng nếu có món
        if lst_mon_an:
            st.table(lst_mon_an)

            # Tính thuế VAT và tổng thanh toán
            thue = tong_cong * 0.1
            tong_tien = tong_cong + thue

            st.subheader(f"Tổng cộng: {tong_cong:,} VND")
            st.write(f"Thuế VAT (10%): {thue:,.0f} VND")
            st.success(f"Tổng thanh toán: {tong_tien:,.0f} VND")
        else:
            st.warning("Bạn chưa chọn món nào.")
    else:
        st.info("Nhập số lượng món rồi nhấn 'Tính tiền' để xem hóa đơn.")        
# for item in lst_mon_an:
#     tong_cong += item["Thành tiền"]
#     tong_tien *= tong_cong*thue
  
