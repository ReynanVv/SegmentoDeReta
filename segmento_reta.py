import streamlit as st
import matplotlib.pyplot as plt

def plot_segmento(ponto_inicial, ponto_final):
    x1, y1 = ponto_inicial
    x2, y2 = ponto_final

    if x1 == x2 and y1 == y2:
        st.write("O segmento é composto por apenas um ponto.")
    elif y1 == y2:
        st.write("O segmento é paralelo ao eixo das abcissas.")
    elif x1 == x2:
        st.write("O segmento é paralelo ao eixo das ordenadas.")
    elif abs(x2 - x1) == abs(y2 - y1):
        st.write("O segmento é uma diagonal perfeita.")
    else:
        st.write("O segmento não é paralelo a nenhum eixo nem uma diagonal perfeita.")

    fig, ax = plt.subplots()
    ax.plot([x1, x2], [y1, y2], marker='o')
    ax.set_xlim(min(x1, x2) - 1, max(x1, x2) + 1)
    ax.set_ylim(min(y1, y2) - 1, max(y1, y2) + 1)
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.grid(True)
    ax.set_aspect('equal', adjustable='box')

    st.pyplot(fig)

st.title("Plotar Segmento de Reta")

st.subheader("Ponto Inicial")
x1 = st.number_input("Coordenada x do ponto inicial", value=0)
y1 = st.number_input("Coordenada y do ponto inicial", value=0)

# Subtítulo para o ponto final
st.subheader("Ponto Final")
x2 = st.number_input("Coordenada x do ponto final", value=0)
y2 = st.number_input("Coordenada y do ponto final", value=0)

if st.button("Gerar Gráfico"):
    ponto_inicial = (x1, y1)
    ponto_final = (x2, y2)
    plot_segmento(ponto_inicial, ponto_final)
