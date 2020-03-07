function_list = ['start', 'start_over', 'select_tea', 'select_sugar',
                 'select_ice', 'select_toppings', 'so_far', 'view_cart',
                 'delete', 'ask_address', 'save_address', 'confirm_bill',
                 'pay']

for i in range(len(function_list)):
    print('{:-^20} {}'.format(function_list[i], i))

    # -------start --------- 0
    # -----start_over ------ 1
    # -----select_tea ------ 2
    # ----select_sugar ----- 3
    # -----select_ice ------ 4
    # --select_toppings ---- 5
    # -------so_far -------- 6
    # -----view_cart ------- 7
    # -------delete -------- 8
    # ----ask_address ------ 9
    # ----save_address ----- 10
    # ----confirm_bill ----- 11
    # --------pay ---------- 12