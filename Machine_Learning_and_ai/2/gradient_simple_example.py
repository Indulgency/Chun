import random
from icecream import ic

def loss(xs, w, b, ys):
    return ((xs * w + b) - ys) ** 2

def gradient(x, w, b, y):
    return 2 * (w * x + b - y) * x
    # 对loss关于w进行偏导

w, b = random.randint(-10, 10), random.randint(-10, 10)

x, y = 10, 0.35

ic(loss(x, w, b, y))

lr = 1e-3

for i in range(100):
    w_gradient = gradient(x, w, b, y)
    w = w + -1 * w_gradient * lr

    ic(w)
    ic(loss(x, w, b, y))


