import datetime
import logging
import os
import sys
from dotenv import load_dotenv
from peewee import Model, IntegerField, CharField, TextField, TimestampField
from playhouse.db_url import connect

# .envの読み込み
load_dotenv(override=True)

logger = logging.getLogger("peewee")
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)
# データベースへの接続設定
# db = SqliteDatabase("peewee_db.sqlite")  # SQLite固定の場合(この場合はインポートが必要 from peewee import SqliteDatabase)
db = connect(os.environ.get("DATABASE"))  # 環境変数に合わせて変更する場合
# db = connect(os.environ.get("DATABASE") or "sqlite:///peewee_db.sqlite")  # 環境変数が無い場合にデフォルト値として値を設定することも可能3


class Message(Model):
    """Message Model"""

    id = IntegerField(primary_key=True)
    user = CharField()
    content = TextField()
    pub_date = TimestampField(default=datetime.datetime.now())

    class Meta:
        database = db
        table_name = "messages2"


db.create_tables([Message])
