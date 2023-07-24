# %%
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import seaborn as sns
# %%
def scartterplot(df):
    fig = make_subplots(
    rows=5, cols=2,
    specs=[[{}, {}], [{}, {}], [{}, {}], [{}, {}], [{"colspan": 2}, None]],
    subplot_titles=[
        'Nível de satisfação do colaborador com a empresa',
        'Última avaliação',
        'Média de horas mensais trabalhadas',
        'Tempo de empresa',
        'Acidente de trabalho',
        'Promoção nos últimos 5 anos',
        'Número de projetos',
        'Salário',
        'Departamento'
    ])
    sl_counts = df.groupby(['satisfaction_level', 'left'])['left'].count().reset_index(name='count')
    le_counts = df.groupby(['last_evaluation', 'left'])['left'].count().reset_index(name='count')
    amh_counts = df.groupby(['average_montly_hours', 'left'])['left'].count().reset_index(name='count')
    tsc_counts = df.groupby(['time_spend_company', 'left'])['left'].count().reset_index(name='count')
    wa_counts = df.groupby(['Work_accident', 'left'])['left'].count().reset_index(name='count')
    pl_counts = df.groupby(['promotion_last_5years', 'left'])['left'].count().reset_index(name='count')
    np_counts = df.groupby(['num_project', 'left'])['left'].count().reset_index(name='count')
    s_counts = df.groupby(['salary', 'left'])['left'].count().reset_index(name='count')
    d_counts = df.groupby(['depto', 'left'])['left'].count().reset_index(name='count')

    fig.add_trace(
        go.Scatter(
            mode='markers',
            x=sl_counts['satisfaction_level'],
            y=sl_counts['left'],
            marker_size= 10 + ((sl_counts['count'] - sl_counts['count'].min()) / (sl_counts['count'].max() - sl_counts['count'].min())) * 25,
            text=sl_counts['count']
        ),
        row=1,
        col=1
    )
    fig.add_trace(
        go.Scatter(
            mode='markers',
            x=le_counts['last_evaluation'],
            y=le_counts['left'],
            marker_size= 10 + ((le_counts['count'] - le_counts['count'].min()) / (le_counts['count'].max() - le_counts['count'].min())) * 25,
            text=le_counts['count']
        ),
        row=1,
        col=2
    )
    fig.add_trace(
        go.Scatter(
            mode='markers',
            x=amh_counts['average_montly_hours'],
            y=amh_counts['left'],
            marker_size= 10 + ((amh_counts['count'] - amh_counts['count'].min()) / (amh_counts['count'].max() - amh_counts['count'].min())) * 25,
            text=amh_counts['count']
        ),
        row=2,
        col=1
    )
    fig.add_trace(
        go.Scatter(
            mode='markers',
            x=tsc_counts['time_spend_company'],
            y=tsc_counts['left'],
            marker_size= 10 + ((tsc_counts['count'] - tsc_counts['count'].min()) / (tsc_counts['count'].max() - tsc_counts['count'].min())) * 35,
            text=tsc_counts['count']
        ),
        row=2,
        col=2
    )
    fig.add_trace(
        go.Scatter(
            mode='markers',
            x=wa_counts['Work_accident'],
            y=wa_counts['left'],
            marker_size= 10 + ((wa_counts['count'] - wa_counts['count'].min()) / (wa_counts['count'].max() - wa_counts['count'].min())) * 35,
            text=wa_counts['count']
        ),
        row=3,
        col=1
    )
    fig.add_trace(
        go.Scatter(
            mode='markers',
            x=pl_counts['promotion_last_5years'],
            y=pl_counts['left'],
            marker_size= 10 + ((pl_counts['count'] - pl_counts['count'].min()) / (pl_counts['count'].max() - pl_counts['count'].min())) * 35,
            text=pl_counts['count']
        ),
        row=3,
        col=2
    )
    fig.add_trace(
        go.Scatter(
            mode='markers',
            x=np_counts['num_project'],
            y=np_counts['left'],
            marker_size= 10 + ((np_counts['count'] - np_counts['count'].min()) / (np_counts['count'].max() - np_counts['count'].min())) * 35,
            text=np_counts['count']
        ),
        row=4,
        col=1
    )
    fig.add_trace(
        go.Scatter(
            mode='markers',
            x=s_counts['salary'],
            y=s_counts['left'],
            marker_size= 10 + ((s_counts['count'] - s_counts['count'].min()) / (s_counts['count'].max() - s_counts['count'].min())) * 35,
            text=s_counts['count']
        ),
        row=4,
        col=2
    )
    fig.add_trace(
        go.Scatter(
            mode='markers',
            x=d_counts['depto'],
            y=d_counts['left'],
            marker_size= 10 + ((d_counts['count'] - d_counts['count'].min()) / (d_counts['count'].max() - d_counts['count'].min())) * 35,
            text=d_counts['count']
        ),
        row=5,
        col=1
    )
    fig.update_layout(title_text='Distribuição de atributos por saiu ou não da empresa', showlegend=False, height=700)
    fig.show()
# %%
def boxplots_comparacao(df_left, df_non_left):
    fig = make_subplots(rows=5, cols=2, subplot_titles=[
        'Nível de satisfação do colaborador com a empresa',
        'Nível de satisfação do colaborador com a empresa',
        'Última avaliação',
        'Última avaliação',
        'Média de horas mensais trabalhadas',
        'Média de horas mensais trabalhadas',
        'Tempo de empresa',
        'Tempo de empresa',
        'Número de projetos',
        'Número de projetos'
    ])
    fig.add_trace(go.Box(x=df_left['satisfaction_level'], name='Left', boxpoints='outliers', showlegend=False), row=1, col=1)
    fig.add_trace(go.Box(x=df_non_left['satisfaction_level'], name='Non Left', boxpoints='outliers', showlegend=False), row=1, col=2)
    fig.add_trace(go.Box(x=df_left['last_evaluation'], name='Left', boxpoints='outliers', showlegend=False), row=2, col=1)
    fig.add_trace(go.Box(x=df_non_left['last_evaluation'], name='Non Left', boxpoints='outliers', showlegend=False), row=2, col=2)
    fig.add_trace(go.Box(x=df_left['average_montly_hours'], name='Left', boxpoints='outliers', showlegend=False), row=3, col=1)
    fig.add_trace(go.Box(x=df_non_left['average_montly_hours'], name='Non Left', boxpoints='outliers', showlegend=False), row=3, col=2)
    fig.add_trace(go.Box(x=df_left['time_spend_company'], name='Left', boxpoints='outliers', showlegend=False), row=4, col=1)
    fig.add_trace(go.Box(x=df_non_left['time_spend_company'], name='Non Left', boxpoints='outliers', showlegend=False), row=4, col=2)
    fig.add_trace(go.Box(x=df_left['num_project'], name='Left', boxpoints='outliers', showlegend=False), row=5, col=1)
    fig.add_trace(go.Box(x=df_non_left['num_project'], name='Non Left', boxpoints='outliers', showlegend=False), row=5, col=2)
    fig.update_layout(title_text='Comparação por saiu ou não da empresa', height=700)
    fig.show()
# %%
def countplots_comparacao(df_left, df_non_left):
    plt.figure(figsize = (16,8))
    plt.subplot(2,2,1)
    sns.countplot(x = "Work_accident", palette = "Paired", data = df_left)
    plt.xlabel('Acidente de trabalho')
    plt.ylabel('Left')
    plt.subplot(2,2,2)
    sns.countplot(x = "Work_accident", palette = "Paired", data = df_non_left)
    plt.xlabel('Acidente de trabalho')
    plt.ylabel('Non Left')
    plt.subplot(2,2,3)
    sns.countplot(x = "promotion_last_5years", palette = "Paired", data = df_left)
    plt.xlabel('Promoção nos últimos 5 anos')
    plt.ylabel('Left')
    plt.subplot(2,2,4)
    sns.countplot(x = "promotion_last_5years", palette = "Paired", data = df_non_left)
    plt.xlabel('Promoção nos últimos 5 anos')
    plt.ylabel('Non Left')
    plt.tight_layout()
    plt.show()
# %%
def histplots_comparacao(df_left, df_non_left):
    plt.figure(figsize = (16,16))
    plt.subplot(10,2,1)
    sns.histplot(x="satisfaction_level", data=df_left, bins=10, kde=True) #type: ignore
    plt.xlabel('Nível de satisfação do colaborador com a empresa')
    plt.ylabel('Left')
    plt.subplot(10,2,2)
    sns.histplot(x="satisfaction_level", data=df_non_left, bins=10, kde=True) #type: ignore
    plt.xlabel('Nível de satisfação do colaborador com a empresa')
    plt.ylabel('Non Left')
    plt.subplot(10,2,3)
    sns.histplot(x="last_evaluation", data=df_left, bins=10, kde=True) #type: ignore
    plt.xlabel('Última avaliação')
    plt.ylabel('Left')
    plt.subplot(10,2,4)
    sns.histplot(x="last_evaluation", data=df_non_left, bins=10, kde=True) #type: ignore
    plt.xlabel('Última avaliação')
    plt.ylabel('Non Left')
    plt.subplot(10,2,5)
    sns.histplot(x="average_montly_hours", data=df_left, bins=10, kde=True) #type: ignore
    plt.xlabel('Média de horas mensais trabalhadas')
    plt.ylabel('Left')
    plt.subplot(10,2,6)
    sns.histplot(x="average_montly_hours", data=df_non_left, bins=10, kde=True) #type: ignore
    plt.xlabel('Média de horas mensais trabalhadas')
    plt.ylabel('Non Left')
    plt.subplot(10,2,7)
    sns.histplot(x="time_spend_company", data=df_left, bins=10, kde=True) #type: ignore
    plt.xlabel('Tempo de empresa')
    plt.ylabel('Left')
    plt.subplot(10,2,8)
    sns.histplot(x="time_spend_company", data=df_non_left, bins=10, kde=True) #type: ignore
    plt.xlabel('Tempo de empresa')
    plt.ylabel('Non Left')
    plt.subplot(10,2,9)
    sns.histplot(x="num_project", data=df_left, bins=10, kde=True) #type: ignore
    plt.xlabel('Número de projetos')
    plt.ylabel('Left')
    plt.subplot(10,2,10)
    sns.histplot(x="num_project", data=df_non_left, bins=10, kde=True) #type: ignore
    plt.xlabel('Número de projetos')
    plt.ylabel('Non Left')
    plt.tight_layout()
    plt.show()
# %%
def boxplots(df):
    fig = make_subplots(rows=3, cols=2, subplot_titles=[
        'Nível de satisfação do colaborador com a empresa',
        'Última avaliação',
        'Média de horas mensais trabalhadas',
        'Tempo de empresa',
        'Número de projetos'
    ])
    fig.add_trace(go.Box(x=df['satisfaction_level'], name="", boxpoints='outliers', showlegend=False), row=1, col=1)
    fig.add_trace(go.Box(x=df['last_evaluation'], name="", boxpoints='outliers', showlegend=False), row=1, col=2)
    fig.add_trace(go.Box(x=df['average_montly_hours'], name="", boxpoints='outliers', showlegend=False), row=2, col=1)
    fig.add_trace(go.Box(x=df['time_spend_company'], name="", boxpoints='outliers', showlegend=False), row=2, col=2)
    fig.add_trace(go.Box(x=df['num_project'], name="", boxpoints='outliers', showlegend=False), row=3, col=1)
    fig.show()
# %%
def countplots(df):
    plt.figure(figsize = (16, 4))
    plt.subplot(1,3,1)
    sns.countplot(x='Work_accident', palette = "Paired", data=df)
    plt.xlabel('Acidente de trabalho')
    plt.subplot(1,3,2)
    sns.countplot(x='left', palette = "Paired", data=df)
    plt.xlabel('Saiu da empresa')
    plt.subplot(1,3,3)
    sns.countplot(x='promotion_last_5years', palette = "Paired", data=df)
    plt.xlabel('Promoção nos últimos 5 anos')
    plt.tight_layout()
    plt.show()
# %%