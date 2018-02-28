from prettytable import PrettyTable


head_count = 40
slices_per_head = 4

budget = 8000
budget = budget / 1.18

non_veg = False

pizza_count = (head_count * slices_per_head) / 6
pizza_count = int(pizza_count)
pizza_price = budget / pizza_count


table = PrettyTable()
print("")
table.add_row(("Head Count", head_count))
table.add_row(("Max price of each pizza", pizza_price))
table.add_row(("No of medium pizzas", pizza_count))
table.add_row(("Total ", pizza_count * pizza_price))
table.add_row(("Total + Tax ", pizza_count * pizza_price * 1.18))

print(table)
