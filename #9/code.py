def n_adj_sum(int_list, mode="trivial")
    if mode == "trivial":
        if len(int_list) < 3:
            raise Exception("List too small");