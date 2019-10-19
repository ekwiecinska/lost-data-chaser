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


def time_series_with_nans(dataframe, column, class_column=None):
    """ Visualise a time series for an aggregate signal, or split the signal over classes.
    
    :param dataframe: Pandas DataFrame with a valid pd.DateTime index
    :type dataframe: pd.DataFrame
    
    :param column: Column name containing the signal
    :type column: str
    
    :param class_column: If None, plot all of the signals over classes as one trace. Otherwise, plot a trace 
    for each unique value in dataframe[class_column]
    :type class_column: str
    
    :return: A plotly figure of the time series with gaps for missing data.
    :rtype: plotly.graph_objects.Figure
    """
    if not class_column:
        data = [
            go.Scatter(x=dataframe.index, y=dataframe[column].values)
        ]
    else:
        class_ids = dataframe[class_column].unique()
        data = []
        for class_id in class_ids:
            class_df = dataframe.query(f'{class_column} == "{class_id}"')
            data.append(
                go.Scatter(x=class_df.index,
                           y=class_df[column].values,
                           name=f'{class_id}'
                          )
            )
            

    layout = go.Layout(
    title=dict(text=f"Time series with missing data. Double click on a legend item to isolate the trace (double click to clear)",
               font=dict(size=24)),
    autosize = True, 
    )

    fig = go.Figure(data=data, layout=layout)

    return fig