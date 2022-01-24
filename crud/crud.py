from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import Session
from traceback import format_exc
try:
    from ..stg import STG
except ImportError:
    from stg import STG
# from utils_common.manage_exceptions_decorator import manage_exceptions_decorator


class Crud:
    def __init__(self, **kwargs):

        self.connection_string = kwargs.get("connection_string") or kwargs['CONNECTION_STRING']
        self.encoding = kwargs.get("encoding") or kwargs.get("ENCODING", 'utf-8')
        self.pool_size = kwargs.get("pool_size") or kwargs.get("POOL_SIZE", 10)
        self.max_overflow = kwargs.get("max_overflow") or kwargs.get("MAX_OVERFLOW", 20)
        self.pool_recycle = kwargs.get("pool_recycle") or kwargs.get("POOL_RECYCLE", 3600)
        self.base = kwargs.get("base") or kwargs.get("BASE", None)

        self.engine = None
        self.session = None

    def initiate(self):
        self.create_engine()
        self.create_session()
        self.create_tables()

    def create_engine(self):
        self.engine = create_engine(
            url=self.connection_string,
            encoding=self.encoding
        )

    def create_session(self):
        self.session = Session(bind=self.engine)

    def create_tables(self):
        for key in self.base.metadata.tables.keys():
            if not inspect(self.engine).has_table(key):
                self.base.metadata.create_all(self.engine)

    def insert(self,
               instances,
               refresh=False):
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

    # @manage_exceptions_decorator(report_traceback=False)
    def __del__(self):
        self.close_session()
        self.close_all_connections()

    def close_session(self):
        try:
            self.session.close()
        except Exception:
            print(format_exc())
        else:
            self.session = None

    def close_all_connections(self):
        try:
            self.engine.dispose()
        except Exception:
            print(format_exc())
        else:
            self.engine = None
