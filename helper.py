import pandas 

def get_sql(sql, connector):
    """Return pandas DataFrame."""
    cur = connector.cursor()
    cur.execute(sql)
    return pandas.DataFrame(cur.fetchall(), columns=[c[0] for c in cur.description])