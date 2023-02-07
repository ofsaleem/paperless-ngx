import logging
import uuid
from typing import Optional


class LoggingMixin:

    logging_group: Optional[uuid.UUID] = None

    logging_name: Optional[str] = None

    def renew_logging_group(self) -> None:
        self.logging_group = uuid.uuid4()

    def log(self, level: str, message: str, **kwargs) -> None:
        if self.logging_name:
            logger = logging.getLogger(self.logging_name)
        else:
            name = ".".join([self.__class__.__module__, self.__class__.__name__])
            logger = logging.getLogger(name)

        getattr(logger, level)(message, extra={"group": self.logging_group}, **kwargs)
