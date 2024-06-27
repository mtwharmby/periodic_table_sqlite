from sqlalchemy import (
    Column, Integer, String, ForeignKey, Table, MetaData
)

from ..shared import ATOMIC_NR, BLOCK, BLOCK_ID, LABEL, LABEL_ID


def period_table(metadata_obj: MetaData, prefix="", **kwargs) -> Table:
    return Table(
        f"{prefix}Period",
        metadata_obj,
        Column("number", Integer, primary_key=True)
    )


def group_table(metadata_obj: MetaData, prefix="", **kwargs) -> Table:
    return Table(
        f"{prefix}Group",
        metadata_obj,
        Column("number", Integer, primary_key=True),
        Column("label_eu", String, nullable=True),
        Column("label_us", String, nullable=True),
    )


def block_table(metadata_obj: MetaData, prefix="", **kwargs) -> Table:
    return Table(
        f"{prefix}Block",
        metadata_obj,
        Column(BLOCK_ID, Integer, primary_key=True),
        Column(BLOCK, String, nullable=False)
    )


def label_table(metadata_obj: MetaData, prefix="", **kwargs) -> Table:
    return Table(
        f"{prefix}Label",
        metadata_obj,
        Column(LABEL_ID, Integer, primary_key=True),
        Column(LABEL, String, nullable=False),
        Column("description", String, nullable=True)
    )


def label_to_element_table(metadata_obj: MetaData, prefix="") -> Table:
    return Table(
        f"{prefix}ElementLabel",
        metadata_obj,
        Column(
            LABEL_ID, Integer, ForeignKey(f"Label.{LABEL_ID}"),
            primary_key=True
        ),
        Column(
            ATOMIC_NR, Integer, ForeignKey(f"Element.{ATOMIC_NR}"),
            primary_key=True
        ),
    )
