from unittest.mock import Mock
from datetime import date
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

date = Mock()
date.today = Mock(return_value='21 августа 1990 года')

logger.debug(date.today())