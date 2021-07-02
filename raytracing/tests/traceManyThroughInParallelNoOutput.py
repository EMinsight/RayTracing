import envtest

from raytracing import *

if __name__ == '__main__':
    rays = [Ray(y, y) for y in range(20_000)]
    m = Space(d=1)
    m.traceManyThroughInParallel(rays, processes=2, progress=False)
