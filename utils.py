def mark_table_cell_by_column_by_func(table, column_ids, func):
    new_table = []

    column_processor = ColumnProcessFunc(column_ids, func)

    for row in table:
        column_processor.read(row)

    column_processor.process()

    for row in table:
        new_row = column_processor.produce(row)
        new_table.append(new_row)

    return new_table


class ColumnProcessFunc:
    def __init__(self, column_ids, func_class):
        self.column_ids = column_ids

        self.column_data = {i: [] for i in self.column_ids}
        self.func_class_list = {i: func_class() for i in self.column_ids}

    def read(self, row):
        for column_id in self.column_ids:
            cell = row[column_id]
            self.column_data[column_id].append(cell)

    def produce(self, row):
        new_row = []
        for column_id in range(len(row)):
            cell = row[column_id]

            if column_id in self.column_ids:
                func_instance = self.func_class_list[column_id]
                new_cell = func_instance.produce(cell)
            else:
                new_cell = cell

            new_row.append(new_cell)

        return new_row

    def process(self):
        for k, v in self.column_data.items():
            func_instance = self.func_class_list[k]
            func_instance.read(v)


def make_a_value_function(value_func, left_append='**', right_append='**'):
    class ValueFuncClass:
        def __init__(self, value_func=value_func, left_append=left_append, right_append=right_append):
            self.value_func = value_func
            self.interested_value = None
            self.left_append = left_append
            self.right_append = right_append

        def read(self, column_cell_list):
            self.interested_value = self.value_func(column_cell_list)

        def produce(self, cell):
            if cell == self.interested_value:
                return "{}{}{}".format(self.left_append, cell,
                                       self.right_append)
            return cell

    return ValueFuncClass


if __name__ == "__main__":
    table = [
        [1, 3],
        [2, 4]
    ]

    new_table = mark_table_cell_by_column_by_func(table, [0, 1], make_a_value_function(max))

    print(new_table)

    table = [
        [1, 3],
        [2, 4]
    ]

    new_table = mark_table_cell_by_column_by_func(table, [1], make_a_value_function(max))

    print(new_table)
