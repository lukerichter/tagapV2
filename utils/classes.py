from dataclasses import dataclass
from typing import Optional

from utils.constants import ERROR_MESSAGES


@dataclass
class Error:
    err_id: int
    col: Optional[str] = None
    row: Optional[int] = None
    val: Optional[str] = None

    def __str__(self):
        err = f'Fehler: {ERROR_MESSAGES[self.err_id]}'
        err += f'\n - Wert: "{self.val}"' if self.val else ''
        err += f'\n - Spalte: "{self.col}"' if self.col else ''
        err += f'\n - Zeile: {self.row + 1}' if self.row else ''
        return err + '\n'
