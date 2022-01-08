def print_table(table ,h_sep = "|", v_sep = "—", margin = 1):
    v_lengths = [0 for _ in table[0]]

    for row in table:
        index = 0
        for item in row:
            if v_lengths[index]-2 * margin < len(str(item)):
                v_lengths[index] = len(str(item)) + margin * 2
            
            index += 1

    to_print = ""

    for row in table:
        index = 0
        row_str = ""
        for item in row:
            row_str += "".join([" " for _ in range(margin)])
            row_str += str(item)
            row_str += "".join([" " for _ in range(v_lengths[index] - len(str(item)) - 2 * margin)])
            row_str += "".join([" " for _ in range(margin)])
            if not index == len(table[0])-1:
                row_str += h_sep
            index += 1
        to_print += row_str + "\n" + "".join([v_sep for _ in range(sum(v_lengths) + len(v_lengths) - 1)]) + "\n"
    
    print(to_print)