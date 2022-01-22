from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import Session
from db.models import base
from traceback import format_exc
from stg import report
import stg
from ..manage_exceptions_decorator import manage_exceptions_decorator


class Crud:
    def __init__(

            self,
            connection_string=None
    ):
        report.debug("")
        self.connection_string = \
            connection_string or \
            stg.MAIN_DATABASE['CONNECTION_STRING']
        self.engine = None
        self.session = None

    def initiate(self):
        report.debug("")
        self.create_engine()
        self.create_session()
        self.create_tables()

    def create_engine(self):
        report.debug("")
        self.engine = create_engine(
            url=self.connection_string,
            encoding=stg.MAIN_DATABASE['ENCODING']
        )

    def create_session(self):
        report.debug("")
        self.session = Session(bind=self.engine)

    def create_tables(self):
        report.debug("")
        for key in base.metadata.tables.keys():
            if not inspect(self.engine).has_table(key):
                base.metadata.create_all(self.engine)

    def insert(
            self,
            instances,
            refresh=False
    ):
        try:
            self.session.add(instances)
            self.session.commit()
            self.session.flush()
            if refresh:
                self.session.refresh(instances)
            return instances
        except Exception:
            report.warning(format_exc())
            self.session.rollback()
            raise

    def find(
            self,
            query='',
            filter_str='',
            fetch='one'
    ):
        """
        :param query:should be name of the class in models.py
        :param filter_str: should be based on name of classes in models.py
        :param fetch: 'one' or 'all'
        self.session.query(Files).filter(Files.id==1).all()
        :return:
        """
        if not self.session:
            self.create_session()

        query = self.session.query(eval(query))
        if filter_str:
            query = query.filter(eval(filter_str))

        if fetch in ('one', 1,):
            return [query.one()]
        elif fetch in ('all',):
            return query.all()
        else:
            raise

    @manage_exceptions_decorator(report_traceback=False)
    def __del__(self):
        self.close_session()
        self.close_all_connections()

    def close_session(self):
        report.debug("")
        try:
            self.session.close()
        except Exception:
            print(format_exc())
        else:
            self.session = None

    def close_all_connections(self):
        report.debug("")
        try:
            self.engine.dispose()
        except Exception:
            print(format_exc())
        else:
            self.engine = None
