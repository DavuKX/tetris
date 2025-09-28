from colors import Colors
from block import Block


class BlockBuilder:
    def __init__(self):
        self.block_id = 0
        self.cells = {}
        self.cell_size = 30
        self.rotation_state = 0
        self.colors = Colors.get_cell_colors()
        self.row_offset = 0
        self.column_offset = 0

    def set_block_id(self, block_id):
        self.block_id = block_id

    def set_cells(self, cells):
        self.cells = cells

    def set_cell_size(self, cell_size):
        self.cell_size = cell_size

    def set_rotation_state(self, rotation_state):
        self.rotation_state = rotation_state

    def set_colors(self, colors):
        self.colors = colors

    def set_row_offset(self, row_offset):
        self.row_offset = row_offset

    def set_column_offset(self, column_offset):
        self.column_offset = column_offset

    def build(self):
        block = Block(self.block_id)
        block.cells = self.cells
        block.cell_size = self.cell_size
        block.rotation_state = self.rotation_state
        block.colors = self.colors
        block.row_offset = self.row_offset
        block.column_offset = self.column_offset
        return block
