import streamlit as st

def calcula_resistividade(resistencia,  largura, area):
    DADOS = f'DADOS:---------------------------------------------------------'
    DADOS2 = f'A= ?;'
    DADOS3 = f'r= {resistencia} ohm mm²/m'
    DADOS4 = f'L= {largura} m'
    DADOS5 = f'R= {area} ohm'
    FORMULA3 = f'FORMULA:-----------------------------------------------------'
    FORMULA = f'A=r * L / R (AREA = RESISTENCIA(r) vezes(*) LARGURA a dividir por(/) RESISTIVIDADE(R)'
    RESOLUÇÃO = f'RESOLUÇAO:--------------------------------------------------'
    passo1 = f'Passo 1: Multiplicar a resistência ({resistencia} ohm mm² pela largura ({largura} m)'
    passo2 = f'Passo 2: Dividir o resultado pelo valor da resistividade ({area} ohm)'
    resistividade = (resistencia * largura) / area
    return resistividade, [DADOS, DADOS2, DADOS3, DADOS4, DADOS5,FORMULA3, FORMULA, RESOLUÇÃO, passo1, passo2]

st.title('Calculadora de Area,ligado a resistividade')

resistencia= st.number_input('Insira o valor da resistência (ohm mm²/m)')
largura = st.number_input('Insira o valor da largura (m)')
area = st.number_input('Insira o valor da resisitvidade (ohm)')

if st.button('Calcular a Area'):
    resistividade, passos = calcula_resistividade(resistencia, largura, area)
    st.write('Passos para calcular a Area:')
    for passo in passos:
        st.write(passo)
    st.write(f'A Area é: {resistividade} m²')
    st.write('OBRIGADO POR USAR ESTE SITE, SE HOUVER ALGUM PROBLEMA OU CRITICA CONSTRUTIVA'
             'CONTACTE 841038887/868787572')

