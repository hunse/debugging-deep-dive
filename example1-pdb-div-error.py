def process_list(xx):
    y = []
    for a, b in zip(xx, xx[1:]):
        y.append(compute_val(a, b))

    return y


def compute_val(x, y):
    q = x + y
    r = x - y
    return q / r


data = [1, 3, 5, 2, 2, 1]

yy = process_list(data)

print(f"Program result -- {yy}")
