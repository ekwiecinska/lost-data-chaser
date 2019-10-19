import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import pandas as pd


def missing_value_heatmap(dataframe, name):
    """
    Generates a plotly heatmap to graphically display missing values in a pandas dataframe

    :param dataframe: Pandas dataframe, missing values should be of type `numpy.nan`
    :type dataframe: Pandas DataFrame

    :return: Plotly figure of the missing data heatmap
    :rtype: plotly.graph_objects.Figure

    """
    val_array = np.array(dataframe.fillna(-99).values)
    val_array[np.where(val_array != -99)] = 0
    val_array[np.where(val_array == -99)] = 1

    data = [
        go.Heatmap(
            z=val_array,
            x=dataframe.columns,
            y=np.arange(dataframe.shape[0]),
            colorscale='purp',
            hovertemplate='Column: %{x}\n Missing?: %{z}',
            name=f'{name}'
        )
    ]

    layout = go.Layout(
    title=dict(text=f"Missing data heatmap ({name}): Hover to see column names and indices with missing values.",
               font=dict(size=24)),
    autosize = True, 
    xaxis=dict(
        showticklabels=True, 
        ticks="", 
        showgrid=False,
        zeroline=False,
        automargin=False,
        tickmode='array',
    ),
    yaxis=dict(
        autorange=True,
        tickmode='array',
        showgrid=False,
        zeroline=False,
        showline=False,
        ticks="",
        automargin=False,
        showticklabels=False),
    )

    fig = go.Figure(data=data, layout=layout)

    return fig

from plotly.subplots import make_subplots


def missing_data_ratios(dataframes, names):
    """ 
    Plot the ratio of missing data for multiple dataframes or a single dataframe.
    
    :param dataframes: A single dataframe or iterable of dataframes
    :type dataframes: list, pd.DataFrame
    
    :param names: A list of names for each plot, which will be applied in the same order as dataframes
    :type names: list
    
    :return: A plotly figure of the missing data ratios.
    :rtype: plotly.graph_objects.Figure
    """
    if isinstance(dataframes, list):
        fig = make_subplots(rows=1, cols=len(dataframes), subplot_titles=names, specs=[[{"type": "domain"} for x in range(len(dataframes))]])
    elif isinstance(dataframes, pd.DataFrame):
        fig = make_subplots(rows=1, cols=1, subplot_titles=names, specs=[{"type": "domain"}])
    else:
        raise ValueError("Dataframe should be a list of dataframes or a single dataframe")
    
    labels = ['Present', 'Missing']
    
    for col, df in enumerate(dataframes, start=1):
        values = [df.notnull().sum().sum(), df.isnull().sum().sum()]
        fig.add_trace(
            go.Pie(labels=labels, values=values, name=names[col-1]),
            row=1, col=col
        )

    fig.update_layout(autosize=True, title_text="Missing data ratios across each dataset")

    return fig