from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session , sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer , String , DateTime, text
import pandas as pd

engine = create_engine( 'sqlite:///gt.db', convert_unicode=True)
db_session = scoped_session( sessionmaker( autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    Base.metadata.create_all( bind=engine)

    class Revenue_Analysis(Base):
        __tablename__ = 'Revenue_Analysis'
        activity_date = Column ( DateTime, primary_key=True)
        member_id = Column (Integer)
        game_id = Column (Integer)
        wager_amount = Column (Integer)
        number_of_wagers = Column (Integer)
        win_amount = Column (Integer)
        activity_year_month = Column ( Integer)
        bank_type_id = Column (Integer)


    file_name = 'Revenue_Analysis_Test_Data.csv'
    df = pd.read_csv(file_name)
    df.to_sql ( con=engine, index_label='id', name=Revenue_Analysis.__tablename__, if_exists='replace')

    class Calendar (Base):
        __tablename__ = 'Calendar'
        calendar_date = Column ( DateTime, primary_key=True)
        calendar_year = Column ( Integer)
        calendar_month_number = Column ( Integer)
        calendar_month_name = Column ( String (100))
        calendar_day_of_month = Column ( Integer)
        calendar_day_of_week = Column ( Integer)
        calendar_day_of_name = Column ( String ( 100))
        calendar_year_month = Column ( Integer)

    file_name = 'Calendar_Test_Data.csv'
    df = pd.read_csv ( file_name )
    df.to_sql ( con=engine, index_label='id', name=Calendar.__tablename__ , if_exists='replace')
