import streamlit as st

# ----------------------------------------------------- sidebar
st.sidebar.image('logo.png')
 
st.sidebar.title('BritSpeed CAR')

carros = ['Audi', 'Rolls-Royce', 'Aston Martin', 'Maybach']

modelo = st.sidebar.selectbox('Selecione o carro desejado!', carros )


# ----------------------------------------------------- Principal
st.title('BRITSPEED CAR')
st.markdown(f'## Voce escolheu o modelo: {modelo}')
st.image(f'{modelo}.png')

if modelo == 'Audi': 
    diaria = 500 

elif modelo == 'Rolls-Royce':
    diaria = 850

elif modelo == 'Aston Martin':
    diaria =  1000

elif modelo == 'Maybach':
    diaria = 900

dias = st.text_input(f'Por quantos dias voce alugou o {modelo}?')
km = st.text_input(f'Quantos km voce roudou com o veiculo?')

if st.button('Calcular'):
    dias = int(dias)
    km = float(km)

    total_dias = dias * diaria
    total_km = km * 0.30
    aluguel = total_dias + total_km
    st.warning(f'Voce alugou o {modelo} por {dias} dias e rodou {km} km. o valor do aluguel sera R${aluguel}')
















