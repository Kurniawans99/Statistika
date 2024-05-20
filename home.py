import streamlit as st
import main


data = []
st.title('Statistika')

with st.form(key='data_form'):
    intRate = st.number_input("Tingkat Suku Bunga (0-1) ", min_value=0.0, max_value=1.0,value= 0.0 , step = .1,)
    instalment = st.number_input(" Angsuran bulanan yang harus dibayarkan (cicilan) ", min_value=100, max_value=100000,value= 100 , step = 50,)
    dti = st.number_input("Rasio Pendapatan", min_value=0.0, max_value=1.0,value= 0.0 , step = .1,)
    fico = st.number_input("Skor Kredit (300-850)", min_value=300, max_value=850,value= 350 , step = 10,)
    daysWithCrLine = st.number_input("hari pertama peminjam memiliki akun kredit aktif (hari)", min_value=1, max_value=100000,value= 120 , step = 30,)
    revolBal = st.number_input("jumlah hutang yang belum dibayar pada akhir siklus penagihan kartu kredit.", min_value=100, max_value=100000,value= 100 , step = 50,)
    revolUtil = st.number_input("Penggunaan Kredit", min_value=1, max_value=100,value= 1 , step = 1,)
    delinq2yrs = st.number_input("Jumlah kali peminjam terlambat membayar lebih dari 30 hari dalam 2 tahun terakhir.", min_value=0, max_value=1000,value= 0 , step = 1,)
    inqLast6mths = st.number_input("Jumlah penyelidikan kredit oleh kreditur dalam 6 bulan terakhir.", min_value=0, max_value=10000,value= 0 , step = 1,)

    submit_button = st.form_submit_button(label='Submit')

if submit_button:

   input_data = {
        'int.rate': intRate,
        'installment': instalment,
        'dti': dti,
        'fico': fico,
        'days.with.cr.line': daysWithCrLine,
        'revol.bal': revolBal,
        'revol.util': revolUtil,
        'delinq.2yrs': delinq2yrs,
        'inq.last.6mths': inqLast6mths
    }
   st.write(main.main(input_data))



