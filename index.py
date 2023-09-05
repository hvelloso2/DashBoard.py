# Importando as bibliotecas necessárias
import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc

from app import *
from dash_bootstrap_templates import ThemeSwitchAIO

# Definindo URLs e templates de temas para uso posterior
url_theme1 = dbc.themes.CYBORG
url_theme2 = dbc.themes.LUX
template_theme1 = 'cyborg'
template_theme2 = 'lux'

# Lendo os dados do arquivo CSV
df = pd.read_csv('F1Drivers_Dataset.csv')  # Substitua 'seuarquivo.csv' pelo nome do seu arquivo CSV

# Inicializando a aplicação Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Definindo o layout da aplicação Dash
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            # Componente de troca de tema
             ThemeSwitchAIO(aio_id='theme', themes=[url_theme1, url_theme2]),
            # Título da página
            html.H3("Estatísticas de Pilotos de Automobilismo"),
            # Dropdown para seleção de país
            dcc.Dropdown(
                id='Country',
                value='Brazil',  # Substitua pelo país de sua escolha
                options=[{'label': country, 'value': country} for country in df['Nationality'].unique()],
                multi=False
            ),
        ])
    ]),
    dbc.Row([
        dbc.Col([
            # Gráfico de barras do número de campeonatos ganhos
            dcc.Graph(id='bar-graph-championships')
        ])
    ]),
    dbc.Row([
        dbc.Col([
            # Gráfico de barras do número de vitórias
            dcc.Graph(id='bar-graph-wins')
        ], width={'size': 8, 'offset': 2}),  # Ajuste o tamanho e o offset para controlar o tamanho do gráfico
    ])
])

# Callback para atualizar o gráfico de campeonatos ganhos
@app.callback(
    Output('bar-graph-championships', 'figure'),
    Input('Country', 'value'),
    Input(ThemeSwitchAIO.ids.switch('theme'),'value')
)
def update_championships_graph(selected_country, toggle):
    # Filtrando o DataFrame com base no país selecionado
    filtered_df = df[df['Nationality'] == selected_country]
    template = template_theme1 if toggle else template_theme2

    # Criando um gráfico de barras com Plotly Express para mostrar o número de campeonatos ganhos por piloto
    fig = px.bar(
        filtered_df,
        template=template,
        x='Driver',
        y='Championships',
        labels={'Driver': 'Piloto', 'Championships': 'Campeonatos Ganhos'},
        title=f'Campeonatos Ganhos por Piloto de {selected_country}'
    )
    
    # Definindo os ticks do eixo y para números inteiros
    fig.update_yaxes(tickvals=list(range(int(filtered_df['Championships'].max()) + 1)))
    
    return fig

# Callback para atualizar o gráfico de vitórias
@app.callback(
    Output('bar-graph-wins', 'figure'),
    Input('Country', 'value'),
    Input(ThemeSwitchAIO.ids.switch('theme'),'value')
)
def update_wins_graph(selected_country,toggle):
    # Filtrando o DataFrame com base no país selecionado
    filtered_df = df[df['Nationality'] == selected_country]
    template = template_theme1 if toggle else template_theme2
    # Criando um gráfico de barras com Plotly Express para mostrar o número de vitórias por piloto
    fig = px.bar(
        filtered_df,
        template=template,
        x='Driver',
        y='Race_Wins',
        labels={'Driver': 'Piloto', 'Race_Wins': 'Total de Vitórias'},
        title=f'Vitórias por Piloto de {selected_country}'
    )
    
    # Definindo os ticks do eixo y para números inteiros
    fig.update_yaxes(tickvals=list(range(int(filtered_df['Race_Wins'].max()) + 1)), tickangle=0)  # Não rotaciona os rótulos
    
    # Aumenta o tamanho do gráfico definindo a largura e altura
    fig.update_layout(height=1600)  # Ajuste a largura e altura conforme necessário
    
    return fig

# Inicialização da aplicação Dash
if __name__ == '__main__':
    app.run_server(debug=True, port=8052)
