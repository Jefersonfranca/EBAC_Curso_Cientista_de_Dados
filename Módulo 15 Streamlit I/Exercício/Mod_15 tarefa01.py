import streamlit as st
import pandas as pd
import numpy as np
import time
from datetime import date

st.set_page_config(layout='wide', page_title ='Mod 15 Exercicio', 
                   page_icon='https://raichu-uploads.s3.amazonaws.com/logo_ebac-escola-britanica-de-artes-criativas_3R8AGG.png')

st.sidebar.success("Módulo 15 Streamlit")

st.markdown("# EBAC - Curso de Ciência de dados 👋")
st.sidebar.header("Exercício Streamlit")
st.write(
    """
Esta demonstração ilustra uma combinação de plotagem e animação com Streamlit. Estamos gerando 
uma série de números aleatórios em um loop por cerca de 5 segundos. Aproveite!"""
)

progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
last_rows = np.random.randn(1, 1)
chart = st.line_chart(last_rows)

for i in range(1, 101):
    new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    status_text.text("%i%% Complete" % i)
    chart.add_rows(new_rows)
    progress_bar.progress(i)
    last_rows = new_rows
    time.sleep(0.05)

progress_bar.empty()

st.markdown(
    """    
    O Streamlit é uma excelente ferramenta para cientistas de dados por sua capacidade de 
    transformar scripts de Python em aplicativos web interativos e intuitivos. Uma das 
    maiores vantagens do Streamlit é sua simplicidade e rapidez na criação de dashboards e 
    visualizações de dados. Ao contrário de outras ferramentas que requerem conhecimentos 
    profundos de web development, o Streamlit permite que cientistas de dados se concentrem 
    exclusivamente na análise e visualização dos dados, sem a necessidade de aprender HTML, 
    CSS ou JavaScript. Com poucos comandos, é possível gerar gráficos, tabelas e outros 
    elementos interativos que ajudam a comunicar insights de maneira clara e eficaz.

    Além disso, o Streamlit facilita a colaboração e a disseminação de resultados. Uma vez 
    que o aplicativo é criado, ele pode ser compartilhado facilmente com colegas e 
    stakeholders, permitindo que eles interajam diretamente com os dados e visualizações. 
    Isso não só melhora a transparência, mas também promove um ambiente de trabalho mais 
    colaborativo, onde feedbacks e ajustes podem ser feitos rapidamente. O Streamlit 
    também suporta a integração com diversas bibliotecas populares de Python, como Pandas, 
    Matplotlib, Plotly, e TensorFlow, tornando-se uma ferramenta versátil que atende às 
    diversas necessidades dos projetos de ciência de dados. 
    """
)
st.write('## Exemplo de Uber pickups em Nova York')
DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data



# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')

if st.checkbox('Mostrar o raw data'):
    st.subheader('Raw data')
    st.write(data)


hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]

st.bar_chart(hist_values)

st.subheader('Map of all pickups')
st.map(data)

hour_to_filter = 17
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)


dataframe = pd.DataFrame(np.random.randn(10, 20), columns=('col %d' % i for i in range(20)))
st.table(dataframe)


x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

data_df = pd.DataFrame(
    {
        "sales": [200, 550, 1000, 80],
    }
)

st.sidebar.data_editor(
    data_df,
    column_config={
        "sales": st.column_config.ProgressColumn(
            "Volume de vendas",
            help="The sales volume in USD",
            format="$%f",
            min_value=0,
            max_value=1000,
        ),
    },
    hide_index=True,
)

data_df = pd.DataFrame(
    {
        "Aniversários": [
            date(1990, 3, 12),
            date(2003, 10, 9),
            date(2011, 5, 19),
            date(2018, 8, 17),
        ]
    }
)

st.sidebar.data_editor(
    data_df,
    column_config={
        "Aniversários": st.column_config.DateColumn(
            "Aniversários",
            min_value=date(1900, 1, 1),
            max_value=date(2020, 1, 1),
            format="DD.MM.YYYY",
            step=1,
        ),
    },
    hide_index=True,
)


st.sidebar.button("Re-run")
