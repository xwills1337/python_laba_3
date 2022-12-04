import pandas as pd


def create_x_y(df: pd.DataFrame) -> None:
    """ Splits source csv file into X.csv and Y.csv file
        Args:
        df (pd.DataFrame): this DataFrame
    Returns:
        None
    """
    df['Дата'].to_csv('X.csv', sep=';', encoding='cp1251', index=False)
    del df['Дата']
    df.to_csv('Y.csv', sep=';', encoding='cp1251', index=False)


if __name__ == "__main__":
    create_x_y(pd.read_csv('data.csv', sep=';', encoding='cp1251'))
