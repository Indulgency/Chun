"""
kmeans聚类方法：
1. 设定一个k值
2. 随机生成k个center
3. 找到所有离k1，k2，k3，...最近的点
4. 算出这些点的均值(k1', k2', k3', ...) 如果与(k1, k2, k3, ...)已经很接近，就停止
如果不接近，则(k1', k2', k3', ...)为新的center并重复step3，4
"""

import matplotlib.pyplot as plt
import numpy as np
import random
from icecream import ic
from matplotlib.colors import BASE_COLORS
from collections import defaultdict

points0 = np.random.normal(size=(100, 2))
points1 = np.random.normal(loc=1, size=(100, 2))
points2 = np.random.normal(loc=2, size=(100, 2))
points3 = np.random.normal(loc=5, size=(100, 2))

points = np.concatenate([points0, points1, points2, points3])


# 生成随机的k个center
def random_center(k, points):
    # step-01
    for i in range(k):
        yield random.choice(points[:, 0]), random.choice(points[:, 1])


def mean(points):
    all_x, all_y = [x for x, y in points], [y for x, y in points]
    return np.mean(all_x), np.mean(all_y)


def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return np.sqrt((x1-x2)**2 + (y1-y2)**2)


def kmeans(k, points, centers=None):
    colors = list(BASE_COLORS.values())

    if not centers:
        centers = list(random_center(k=k, points=points))

    ic(centers)

    for i, c in enumerate(centers):
        plt.scatter([c[0]], [c[1]], s=90, marker='*', color=colors[i]) # 画出k个center

    plt.scatter(*zip(*points)) # 对points进行拆分

    # 保存属于每个center的points
    centers_neighbor = defaultdict(set)

    # 找到最近的center
    for p in points:
        closest_c = min(centers, key=lambda c: distance(p, c))  # 利用distance来找到最近的center
        centers_neighbor[closest_c].add(tuple(p))

    # 找到每一个center附近的points
    for i,c in enumerate(centers):
        _points = centers_neighbor[c]
        all_x, all_y = [x for x, y in _points], [y for x, y in _points]
        plt.scatter(all_x, all_y, color=colors[i])

    plt.show()

    new_centers = []

    # 找到均值，并把这些均值保存到new_centers中
    for c in centers_neighbor:
        new_c = mean(centers_neighbor[c])
        new_centers.append(new_c)

    threshold = 1 # 设定一个极值
    distance_old_and_new = [distance(c_old, c_new) for c_old, c_new in zip(centers, new_centers)]
    ic(distance_old_and_new)
    if all(c < threshold for c in distance_old_and_new):
        return centers_neighbor
    else:
        kmeans(k, points, new_centers)

kmeans(2, points)