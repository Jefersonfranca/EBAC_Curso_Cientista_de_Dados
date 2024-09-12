# Modelo de Regressão Logística e Aplicação Streamlit

Este projeto envolve o treinamento de um modelo de regressão logística e a criação de uma aplicação Streamlit para escorar novos dados com o modelo treinado. O pipeline de pré-processamento e o modelo são salvos em um arquivo `.pkl`, que pode ser carregado e utilizado pela aplicação Streamlit.

[Clique aqui para acessar o app diretamente do Streamlit.](https://jeferson-pycaret-modelo-de-regressao-logistica.streamlit.app)

## Estrutura do Projeto

- **train_and_save_model.py**: Script para treinar e salvar o modelo de regressão logística.
- **app.py**: Aplicação Streamlit para carregar o modelo e fazer previsões em novos dados.
- **requirements.txt**: Arquivo com as dependências do projeto.
- **README.md**: Documentação do projeto.

## Requisitos

Certifique-se de que você tenha o Python 3.6 ou superior instalado. Instale as dependências necessárias usando o arquivo `requirements.txt`.

Para instalar as dependências, execute:

```bash
pip install -r requirements.txt


## Treinamento e Salvamento do Modelo

Para treinar o modelo e salvá-lo, execute o script `train_and_save_model.py`:

```bash
python train_and_save_model.py
```

Esse script treinará o modelo de regressão logística e salvará o modelo treinado em um arquivo chamado `model_final.pkl`.

## Executando a Aplicação Streamlit

Para rodar a aplicação Streamlit e fazer previsões em novos dados, execute o seguinte comando:

```bash
streamlit run app.py
```

## Uso da Aplicação Streamlit

1. **Faça upload do arquivo do modelo (`model_final.pkl`)**: A aplicação precisa do arquivo `.pkl` contendo o modelo treinado.
2. **Faça upload do arquivo de dados CSV**: A aplicação aceita um arquivo CSV com os dados que você deseja escorar.
3. **Visualize os resultados**: Após o upload dos dados, a aplicação exibirá as previsões e probabilidades. Você também pode baixar um arquivo CSV com as previsões e probabilidades geradas.

## Exemplo de Arquivo CSV

O arquivo CSV deve conter os seguintes campos (dependendo do seu pré-processamento):

- `sexo`
- `posse_de_veiculo`
- `posse_de_imovel`
- `tipo_renda`
- `educacao`
- `estado_civil`
- `tipo_residencia`
- `qtd_filhos`
- `idade`
- `tempo_emprego`
- `qt_pessoas_residencia`
- `renda`

## Vídeo do Projeto

Assista ao vídeo de demonstração do projeto para ver como o modelo é treinado e como a aplicação Streamlit funciona:

[![Assista ao vídeo](https://img.youtube.com/vi/YOUR_VIDEO_ID_HERE/0.jpg)](https://www.youtube.com/watch?v=YOUR_VIDEO_ID_HERE)

**Descrição do vídeo:** O vídeo fornece uma visão geral do processo de treinamento do modelo e uma demonstração prática da aplicação Streamlit para escorar novos dados.

## Licença

Este projeto é fornecido sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
