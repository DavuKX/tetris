from position import Position


class BlockDirector:
    def __init__(self, builder):
        self.builder = builder

    def create_l_block(self):
        self.builder.set_block_id(1)
        self.builder.set_cells({
            0: [Position(0, 2), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(1, 1), Position(2, 1), Position(2, 2)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 0)],
            3: [Position(0, 0), Position(0, 1), Position(1, 1), Position(2, 1)]
        })
        self.builder.set_row_offset(0)
        self.builder.set_column_offset(3)

        return self.builder.build()

    def create_j_block(self):
        self.builder.set_block_id(2)
        self.builder.set_cells({
            0: [Position(0, 0), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(0, 2), Position(1, 1), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 2)],
            3: [Position(0, 1), Position(1, 1), Position(2, 0), Position(2, 1)]
        })
        self.builder.set_row_offset(0)
        self.builder.set_column_offset(3)

        return self.builder.build()

    def create_i_block(self):
        self.builder.set_block_id(3)
        self.builder.set_cells({
            0: [Position(1, 0), Position(1, 1), Position(1, 2), Position(1, 3)],
            1: [Position(0, 2), Position(1, 2), Position(2, 2), Position(3, 2)],
            2: [Position(2, 0), Position(2, 1), Position(2, 2), Position(2, 3)],
            3: [Position(0, 1), Position(1, 1), Position(2, 1), Position(3, 1)]
        })
        self.builder.set_row_offset(-1)
        self.builder.set_column_offset(3)

        return self.builder.build()

    def create_o_block(self):
        self.builder.set_block_id(4)
        self.builder.set_cells({
            0: [Position(0, 0), Position(0, 1), Position(1, 0), Position(1, 1)],
        })
        self.builder.set_row_offset(0)
        self.builder.set_column_offset(4)

        return self.builder.build()

    def create_s_block(self):
        self.builder.set_block_id(5)
        self.builder.set_cells({
            0: [Position(0, 1), Position(0, 2), Position(1, 0), Position(1, 1)],
            1: [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 2)],
            2: [Position(1, 1), Position(1, 2), Position(2, 0), Position(2, 1)],
            3: [Position(0, 0), Position(1, 0), Position(1, 1), Position(2, 1)]
        })
        self.builder.set_row_offset(0)
        self.builder.set_column_offset(3)

        return self.builder.build()

    def create_z_block(self):
        self.builder.set_block_id(6)
        self.builder.set_cells({
            0: [Position(0, 0), Position(0, 1), Position(1, 1), Position(1, 2)],
            1: [Position(0, 2), Position(1, 1), Position(1, 2), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(2, 1), Position(2, 2)],
            3: [Position(0, 1), Position(1, 0), Position(1, 1), Position(2, 0)]
        })
        self.builder.set_row_offset(0)
        self.builder.set_column_offset(3)

        return self.builder.build()

    def create_t_block(self):
        self.builder.set_block_id(7)
        self.builder.set_cells({
            0: [Position(0, 1), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 1)],
            3: [Position(0, 1), Position(1, 0), Position(1, 1), Position(2, 1)]
        })
        self.builder.set_row_offset(0)
        self.builder.set_column_offset(3)

        return self.builder.build()
