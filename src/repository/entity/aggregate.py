import sqlalchemy

metadata = sqlalchemy.MetaData()

aggregates = sqlalchemy.Table(
    "aggregates",
    metadata,
    sqlalchemy.Column(
        "uuid", sqlalchemy.String(length=36), nullable=False, primary_key=True
    ),
    sqlalchemy.Column("version", sqlalchemy.Integer, default=1, nullable=False),
)
