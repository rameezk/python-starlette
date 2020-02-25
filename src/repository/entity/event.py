import sqlalchemy

metadata = sqlalchemy.MetaData()

events = sqlalchemy.Table(
    "events",
    metadata,
    sqlalchemy.Column(
        "uuid", sqlalchemy.String(length=36), nullable=False, primary_key=True
    ),
    sqlalchemy.Column(
        "aggregate_uuid",
        sqlalchemy.String(length=36),
        sqlalchemy.ForeignKey("aggregates.uuid"),
        nullable=False,
        index=True,
    ),
    sqlalchemy.Column("name", sqlalchemy.String(length=50), nullable=False),
    sqlalchemy.Column("data", sqlalchemy.JSON),
)
