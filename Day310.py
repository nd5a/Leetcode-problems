# Design Spreadsheet

class Spreadsheet(object):

    def __init__(self, rows):
        """
        :type rows: int
        """
        self.rows = rows
        self.grid = {}   # (row, col) -> value

    def _parse_cell(self, cell: str):
        """Convert Excel-like cell (A1, B2, AA10) into (row, col)."""
        col_str = ''
        row_str = ''
        for ch in cell:
            if ch.isalpha():
                col_str += ch.upper()
            elif ch.isdigit():
                row_str += ch
        # Convert column letters to number
        col = 0
        for c in col_str:
            col = col * 26 + (ord(c) - ord('A') + 1)
        col -= 1  # zero-based index
        row = int(row_str) - 1
        return row, col

    def setCell(self, cell, value):
        """Set a cell to a value."""
        row, col = self._parse_cell(cell)
        self.grid[(row, col)] = value

    def resetCell(self, cell):
        """Clear a cell value."""
        row, col = self._parse_cell(cell)
        if (row, col) in self.grid:
            del self.grid[(row, col)]

    def _get_cell_value(self, cell):
        """Get value of a single cell (default 0)."""
        row, col = self._parse_cell(cell)
        return self.grid.get((row, col), 0)

    def getValue(self, formula):
        """
        Evaluate a formula string like '=A1+B2+10' or '=A1:A3+5'.
        """
        if not formula.startswith("="):
            raise ValueError("Formula must start with '='")

        formula = formula[1:]  # remove '='
        parts = formula.split('+')

        total = 0
        for part in parts:
            part = part.strip()
            if not part:
                continue

            if part.isdigit():
                # Direct number
                total += int(part)
            elif ":" in part:
                # Handle range like A1:A3
                start, end = part.split(":")
                start_row, start_col = self._parse_cell(start)
                end_row, end_col = self._parse_cell(end)
                for r in range(start_row, end_row + 1):
                    for c in range(start_col, end_col + 1):
                        total += self.grid.get((r, c), 0)
            else:
                # Single cell
                total += self._get_cell_value(part)

        return total
