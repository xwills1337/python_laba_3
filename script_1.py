import pandas as pd


def create_x_y(file_path: str, output_directory: str) -> None:
    """ Splits source csv file into X.csv and Y.csv file
    Args:
        df (pd.DataFrame): this DataFrame
    Returns:
        None
    """
    df = pd.read_csv(file_path, sep=';', encoding='cp1251')
    df['Дата'].to_csv(output_directory + '/' + 'X.csv', sep=';', encoding='cp1251', index=False)
    del df['Дата']
    df.to_csv(output_directory + '/' + 'Y.csv', sep=';', encoding='cp1251', index=False)


if __name__ == "__main__":
    create_x_y('data.csv')
