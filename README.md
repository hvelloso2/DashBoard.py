# Estatísticas de Pilotos de Automobilismo

Este é um projeto de aplicativo web Dash que apresenta estatísticas de pilotos de automobilismo com base em um conjunto de dados de pilotos de Fórmula 1. O aplicativo permite que os usuários selecionem um país e visualize gráficos de barras que mostram o número de campeonatos ganhos e o número de vitórias por piloto desse país.

# Visão Geral
Este projeto utiliza o framework Dash para criar uma interface web interativa que permite aos usuários:

.Selecionar um país de origem de pilotos de automobilismo.
.Visualizar o número de campeonatos ganhos por piloto desse país em um gráfico de barras.
.Visualizar o número de vitórias por piloto desse país em outro gráfico de barras.

#Requisitos
Certifique-se de que você tenha as seguintes bibliotecas Python instaladas:

/Dash
/Plotly
/pandas
/dash-bootstrap-components
Você também precisará de um arquivo CSV contendo os dados dos pilotos de automobilismo (consulte F1Drivers_Dataset.csv no código) ou substitua-o pelo seu próprio conjunto de dados.

# Uso
Selecione um país no menu suspenso.
O gráfico de barras "Campeonatos Ganhos por Piloto" mostrará o número de campeonatos ganhos por pilotos desse país.
O gráfico de barras "Vitórias por Piloto" mostrará o número de vitórias por pilotos desse país.
