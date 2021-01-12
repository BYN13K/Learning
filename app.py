high = 1200
core = 400
width = 1800
cable = 25

reserve1 = (high - 2 * cable)
reserve15 = (high - 3 * cable)
reserve2 = (high - 4 * cable)
reserve3 = (high - 6 * cable)

no_cap = ((0.7854 * (high ** 2 - core ** 2) * width) / (1000 * (cable * cable)))
capacity1 = ((0.7854 * (reserve1 ** 2 - core ** 2) * width) / (1000 * (cable * cable)))
capacity15 = ((0.7854 * (reserve15 ** 2 - core ** 2) * width) / (1000 * (cable * cable)))
capacity2 = ((0.7854 * (reserve2 ** 2 - core ** 2) * width) / (1000 * (cable * cable)))
capacity3 = ((0.7854 * (reserve3 ** 2 - core ** 2) * width) / (1000 * (cable * cable)))

print(no_cap)