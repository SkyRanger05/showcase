# -*- coding: "utf-8" -*-
import pandas as pd

class Viz:

    def __init__(self):
        pass

    def dt(self, dataframe):
        dataframe["date"] = pd.DatetimeIndex(dataframe['date'])
        dt = dataframe.set_index("date")

        return dt

    def plot(self, dataframe, chart, title):
        plt = dataframe.plot(kind=chart, figsize=(15, 10), title=title, rot=35)

        return plt;

    def overlay(self, dataframe1, dataframe2, chart, title, label1, label2):
        dataframe1.plot(kind=chart, legend=True, figsize=(15, 10), title=title, rot=35, label=label1)
        dataframe2.plot(kind=chart, legend=True, figsize=(15, 10), rot=35, label=label2)
                
