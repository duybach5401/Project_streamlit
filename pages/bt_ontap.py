import streamlit as st 

st.title("Ví dụ st.tab") #expander là dạng nội dung tab sổ xuống có nội dung bên trong

tab1,tab2,tab3 = st.tabs(["Giới thiệu", "Biểu đồ", " Dữ liệu"])
with tab1:
    st.header("Giới thiệu về sản phẩm A")
    st.write("Mô tả ngắn")
    
with tab2:
    st.header("Biểu đồ 1")
    st.write("Doanh thu quý")
    lst_doanh_thu = [100_000_000,200_000_000,300_000,000,400_000_000]
    st.area_chart(lst_doanh_thu)
    
with tab3:
    st.write("Dữ liệu doanh thu")
    st.table(lst_doanh_thu)
    st.data_editor(lst_doanh_thu,num_rows=True)
    
    
    
    