import streamlit as st
import pandas as pd
import pickle
from io import BytesIO

# Função para carregar o modelo do arquivo .pkl
def load_model(model_file):
    with BytesIO(model_file.read()) as file:
        model = pickle.load(file)
    return model

# Função para fazer previsões
def score_data(model, data):
    predictions = model.predict(data)
    probabilities = model.predict_proba(data)[:, 1]
    return predictions, probabilities

def main():
    st.title("Modelo de Regressão Logística")

    st.write("Faça o upload do arquivo do modelo .pkl e do arquivo de dados .csv para escorar a base com o modelo treinado.")

    # Upload do arquivo do modelo
    model_file = st.file_uploader("Escolha um arquivo de modelo (.pkl)", type="pkl")
    if model_file is not None:
        model = load_model(model_file)
        st.write("Modelo carregado com sucesso!")

        # Upload do arquivo CSV
        data_file = st.file_uploader("Escolha um arquivo de dados (.csv)", type="csv")
        if data_file is not None:
            # Carregar dados
            data = pd.read_csv(data_file)
            st.write("Dados carregados:")
            st.write(data.head())

            try:
                # Fazer previsões
                predictions, probabilities = score_data(model, data)

                # Exibir resultados
                st.write("Predições:")
                st.write(predictions)

                st.write("Probabilidades:")
                st.write(probabilities)

                # Se você quiser salvar as previsões em um novo arquivo CSV
                result_df = data.copy()
                result_df['Prediction'] = predictions
                result_df['Probability'] = probabilities

                st.write("Download das previsões:")
                st.download_button(
                    label="Baixar previsões como CSV",
                    data=result_df.to_csv(index=False),
                    file_name='previsoes.csv',
                    mime='text/csv'
                )
            except Exception as e:
                st.error(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()
