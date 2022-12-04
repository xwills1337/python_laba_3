import pandas as pd


def create_data_2(df: pd.DataFrame) -> pd.DataFrame:
    """ Adds a new column of years to the DataFrame
    Args:
        df (pd.DataFrame): this DataFrame
    Returns:
        pd.DataFrame: DataFrame with new column
    """
    df['data_2'] = df['Дата'].dt.year
    df['Дата'] = df['Дата'].dt.date

    return df


def create_file(df: pd.DataFrame, year: int, output_directory: str) -> None:
    """ Creates a .csv file with single year data
    Args:
        df (pd.DataFrame): this DataFrame
        year(int): Data is collected for this year
    Returns:
        None
    """
    lf = df[df['data_2'] == year]
    data = str(lf['Дата'].iloc[0]).replace('-', '') + "_" + str(lf['Дата'].iloc[lf.shape[0] - 1]).replace('-', '')
    del lf['data_2']
    lf.to_csv(output_directory + '/' + data + ".csv", sep=';', encoding='cp1251', index=False)


if __name__ == "__main__":

    pf = pd.read_csv('data.csv', sep=';', encoding='cp1251')

    pf = create_data_2(pf)

    first_year = pf['data_2'][0]
    last_year = pf['data_2'][pf.shape[0] - 1]

    for first_year in range(first_year, last_year+1):
        create_file(pf, first_year)

