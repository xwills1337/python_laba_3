import pandas as pd
import datetime
import os


class DateIterator:
    def __init__(self):

        self.counter = 0
        self.df = pd.read_csv('data.csv', sep=';', encoding='cp1251')

    def __next__(self) -> tuple:
        if self.counter == self.df.shape[0]:
            return (self.df.loc[self.counter - 1][0], self.df.loc[self.counter - 1][1],
                    self.df.loc[self.counter - 1][2], self.df.loc[self.counter - 1][3],
                    self.df.loc[self.counter - 1][4], self.df.loc[self.counter - 1][5],
                    self.df.loc[self.counter - 1][6])
        elif self.counter < self.df.shape[0]:
            self.counter += 1
            return (self.df.loc[self.counter - 1][0], self.df.loc[self.counter - 1][1],
                    self.df.loc[self.counter - 1][2], self.df.loc[self.counter - 1][3],
                    self.df.loc[self.counter - 1][4], self.df.loc[self.counter - 1][5],
                    self.df.loc[self.counter - 1][6])


class DateIteratorXY:
    def __init__(self):

        self.counter = 0
        self.lf = pd.read_csv('X.csv', sep=';', encoding='cp1251')
        self.df = pd.read_csv('Y.csv', sep=';', encoding='cp1251')

    def __next__(self) -> tuple:
        if self.counter == self.df.shape[0]:
            return (self.lf.loc[self.counter - 1][0], self.df.loc[self.counter - 1][0],
                    self.df.loc[self.counter - 1][1], self.df.loc[self.counter - 1][2],
                    self.df.loc[self.counter - 1][3], self.df.loc[self.counter - 1][4],
                    self.df.loc[self.counter - 1][5])
        elif self.counter < self.df.shape[0]:
            self.counter += 1
            return (self.lf.loc[self.counter - 1][0], self.df.loc[self.counter - 1][0],
                    self.df.loc[self.counter - 1][1], self.df.loc[self.counter - 1][2],
                    self.df.loc[self.counter - 1][3], self.df.loc[self.counter - 1][4],
                    self.df.loc[self.counter - 1][5])


class DateIteratorYearOrWeek:

    def __init__(self, name):

        self.counter = 0
        self.df = pd.DataFrame()
        for root, dirs, files in os.walk(name):
            for file in files[0: -1: 1]:
                lf = pd.read_csv(name + file, sep=';', encoding='cp1251')
                self.df = pd.concat([self.df, lf], ignore_index=True)

    def __next__(self) -> tuple:
        if self.counter == self.df.shape[0]:
            return (self.df.loc[self.counter - 1][0], self.df.loc[self.counter - 1][1],
                    self.df.loc[self.counter - 1][2], self.df.loc[self.counter - 1][3],
                    self.df.loc[self.counter - 1][4], self.df.loc[self.counter - 1][5],
                    self.df.loc[self.counter - 1][6])
        elif self.counter < self.df.shape[0]:
            self.counter += 1
            return (self.df.loc[self.counter - 1][0], self.df.loc[self.counter - 1][1],
                    self.df.loc[self.counter - 1][2], self.df.loc[self.counter - 1][3],
                    self.df.loc[self.counter - 1][4], self.df.loc[self.counter - 1][5],
                    self.df.loc[self.counter - 1][6])


if __name__ == "__main__":
    # obj = DateIterator()
    # while(True):
    #     print(next(obj))
    # obj = DateIterator_X_Y()
    # while(True):
    #     print(next(obj))
    # obj = DateIterator_year_or_week('files_y/')
    # while(True):
    #    print(next(obj))
    obj = DateIteratorYearOrWeek('files_w/')
    while True:
        print(next(obj))
