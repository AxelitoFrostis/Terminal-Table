class Table:
    def __init__(self, table = [[]]):
        self.set_table(table)
        
    
    def set_table(self, table):
        self.table = table
        
        return self


    def print(self, *args, **kwargs):
        try:
            self.set_table(args[0])
        except IndexError:
            pass
        
        self.h_sep = kwargs.get('h_sep', '|')
        self.v_sep = kwargs.get('v_sep', '—')
        self.c_sep = kwargs.get('c_sep', '+')
        self.margin = kwargs.get('margin', 1)


        longest_value = 0

        
        # Gets each string length of the values
        for row in self.table:
            for item in row:
                if len(str(item)) > longest_value:
                    longest_value = len(str(item))
                

        # to_print is what's getting typed out
        to_print = "\n"

        col_nr = 0
        for row in self.table:
            row_nr = 0
            row_str = "" # Is a single line added to the to_print
            for item in row: # Runs for each value

                row_str += " " * self.margin
                row_str += str(item).rjust(longest_value)
                row_str += " " * self.margin
                if row_nr != len(self.table[0])-1:
                    row_str += self.h_sep
                row_nr += 1

            to_print += row_str + "\n"
            if col_nr != len(self.table) - 1:
                to_print += (len(self.table[0]) * (self.v_sep * (longest_value + self.margin * 2) + self.c_sep)) [:-1] + "\n"

            col_nr += 1
        
        print(to_print)