import streamlit as st
st.title("Simple and compound calculator")

#Input the value
P=st.number_input("Enter the principal Amount:",format="%.2f")
R=st.text_input("Enter the Annual rate:",value="")

try:
    if "%" in R:
        R = float(R.strip("%"))
    else:
        R = float(R)
        R *= 100  # Convert decimal to percent
except ValueError:
    st.warning("Wrong input Rate value")
    R = None

T=st.number_input("Enter the period of year:",format="%.2f")
Interest_type=st.radio("Choose the interest:",("Simple interest","Compound interest"))
Freq_compound=st.selectbox("Choose your compound period:",["Yearly",
"Half","Quartely","Monthly"])
map_Freq={"Yearly":1,
          "Half":6,
          "Quartely":6,
          "Monthly":12
}
def calculate_simple_interest(P, R, T):
    return (P * R * T) / 100

def calculate_compound_interest(P,R,T,N):
    #Convert R from percentage to decimal
    R = R / 100
    N=map_Freq[Freq_compound]
    return P * (1 + R / N) ** (N * T) - P
if st.button("Solve"):
    if P > 0 and R is not None and T > 0:
        if Interest_type =="Simple interest":
            SI = calculate_simple_interest(P, R, T)
            st.success(f"Simple Interest: ₦{SI:.2f}")
            st.info(f"Total Amount after {T} years: ₦{P + SI:.2f}")
        else:
            CI = calculate_compound_interest(P, R, T,Freq_compound)
            st.success(f"Compound Interest: ₦{CI:.2f}")
            st.info(f"Total Amount after {T} years: ₦{P + CI:.2f}")
    else:
        st.error("All inputs must be valid non-negative numbers.")
            

