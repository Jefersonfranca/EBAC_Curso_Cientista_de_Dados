# Projeto RFV

Este projeto utiliza a metodologia RFV (Recência, Frequência e Valor) para segmentação de clientes baseado no comportamento de compras dos clientes. A aplicação é construída utilizando Streamlit para a interface web e Pandas para manipulação de dados.

## Descrição

RFV é uma técnica de segmentação de clientes que agrupa os clientes com base na Recência (R), Frequência (F) e Valor (V) das suas compras. Esses grupos podem ser utilizados para direcionar ações de marketing mais eficientes e personalizadas.

## Funcionalidades

- Carregar um arquivo CSV ou Excel com os dados de compras dos clientes
- Calcular as métricas de Recência, Frequência e Valor
- Segmentar os clientes em grupos baseados em quartis
- Exibir a tabela RFV final e a distribuição dos clientes por grupos
- Gerar recomendações de ações de marketing/CRM para cada grupo
- Permitir o download da tabela RFV final em formato Excel

## Como Executar

### Pré-requisitos

- Python 3.7 ou superior
- Pip (gerenciador de pacotes do Python)

### Instalação

1. Clone o repositório:
   ```sh
   git clone https://github.com/Jefersonfranca/rfv-projeto/

2. Navegue até o diretório do projeto:
   ```sh
   cd rfv-projeto
   ```
3. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

### Executando a Aplicação

Para iniciar a aplicação Streamlit, execute o seguinte comando no terminal:
```sh
streamlit run app_RFV.py
```
Substitua `app_RFV.py` pelo nome do arquivo Python que contém o código do projeto.

## Estrutura do Projeto

- `app_RFV.py`: Arquivo principal do projeto que contém o código da aplicação.
- `requirements.txt`: Lista de dependências necessárias para executar o projeto.
- `README.md`: Este arquivo, contendo informações sobre o projeto.

## Exemplo de Uso

1. Carregue o arquivo de dados de compras (CSV ou Excel) através da barra lateral.
2. Veja as métricas de Recência, Frequência e Valor calculadas para cada cliente.
3. Visualize a tabela RFV final e a distribuição dos clientes por grupos.
4. Baixe a tabela RFV final em formato Excel.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
```

Certifique-se de ajustar os detalhes específicos do seu repositório, como o link do repositório e o nome do arquivo Python, conforme necessário.
