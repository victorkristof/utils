import pandas as pd

from sqlalchemy import create_engine


def read_table(table_name, db_path):
    # Read sqlite query results into a pandas DataFrame
    engine = create_engine(db_path)
    df = pd.read_sql_table(table_name, engine)
    return df
