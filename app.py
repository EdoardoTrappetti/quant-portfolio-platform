import streamlit as st

# Configurazione della pagina
st.set_page_config(
    page_title="Quant Portfolio Platform",
    page_icon="📈",
    layout="wide"
)

# Titolo principale
st.title("Quant Portfolio Platform")

st.subheader("Personalized Investment Strategies")

st.write(
    "A quantitative platform for personalized "
    "ETF portfolio optimization and investment analytics."
)

# Prima interazione con l'utente
capital = st.number_input(
    "Initial Investment Capital (€)",
    min_value=0,
    value=10000,
    step=1000
)

risk_profile = st.selectbox(
    "Risk Profile",
    ["Conservative", "Moderate", "Aggressive"]
)

if st.button("Generate Portfolio"):
    st.success("Portfolio generation completed!")

    st.write(f"Initial Capital: €{capital:,.2f}")
    st.write(f"Risk Profile: {risk_profile}")