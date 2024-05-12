import logging

from sqlalchemy import Engine, MetaData, insert

from .. import PeriodicTableDBBase
from .data.group_data import groups as group_values
from .schema import (
    period_table, group_table, block_table, label_table, label_to_element_table
)

logger = logging.getLogger(__name__)


class PeriodicTableDB(PeriodicTableDBBase):

    def __init__(self, engine: Engine, md: MetaData, **kwargs) -> None:
        super().__init__(engine, md, extended=True, kwargs=kwargs)

        self.period = period_table(self.metadata_obj, **kwargs)
        self.group = group_table(self.metadata_obj, **kwargs)
        self.block = block_table(self.metadata_obj, **kwargs)
        self.label = label_table(self.metadata_obj, **kwargs)
        self.label_element = label_to_element_table(
            self.metadata_obj, **kwargs
        )

    def add_groups(self):
        with self.engine.connect() as conn:
            logger.info(
                f"Adding group numbers, names and labels to {self.group.name} "
                "table."
            )
            conn.execute(
                insert(self.group), group_values
            )
            conn.commit()
