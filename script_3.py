import pandas as pd


def create_file1(df: pd.DataFrame, mas: list[int], output_directory: str) -> None:
    """ Creates a .csv file with single week data
    Args:
        df (pd.DataFrame): this DataFrame
        mas (list[int]): List of indices for which data is selected
    Returns:
        None
    """
    lf = df.loc[mas[0]:mas[-1]]
    data = lf['Дата'].iloc[0].replace('-', '') + "_" + lf['Дата'].iloc[lf.shape[0] - 1].replace('-', '')
    lf.to_csv(output_directory + '/' + data + ".csv", sep=';', encoding='cp1251', index=False)


if __name__ == "__main__":

    pf = pd.read_csv('data.csv', sep=';', encoding='cp1251')
    mas_1 = list(range(7))
    max_1 = pf.shape[0]

    while max_1 > 0:
        create_file1(pf, mas_1)
        mas_1 = [i + 7 for i in mas_1]
        max_1 = max_1 - 7

