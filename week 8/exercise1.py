import pymysql
import pandas as pd
from sqlalchemy import create_engine


con_str = 'mysql+pymysql://dev:ax2@lamseben.dk:3306/python'


def data_persister():
    engine = create_engine(con_str)
    df = pd.read_csv("week 8\crime.csv")
    df.to_sql('pythondemo',con=engine, if_exists='append', index = False)


def data_finder(date1, date2):
    engine = create_engine(con_str)

    # sql = "SELECT cdatetime, crimedescr FROM python.pythondemo WHERE cdatetime >= '1/1/06 0:00' AND cdatetime <= '1/2/06 0:00'"

    sql = 'SELECT cdatetime,crimedescr FROM pythondemo'

    df = pd.read_sql(sql, con=engine, parse_dates=['cdatetime'], columns=['cdatetime', 'crimedescr'])

    date_start = "2006-01-" + str(date1)
    date_end = "2006-01-" + str(date2)

    date_crimes = df.loc[(df['cdatetime'] >= date_start) & (df['cdatetime'] <= date_end)]

    amount_of_burglaries = df[df['crimedescr'].str.contains('BURGLARY')]

    crime_dict = {
        "Crimes within dates": len(date_crimes),
        "Total burglaries in january": len(amount_of_burglaries)
    }

    return crime_dict

# print(data_finder(1, 5))
