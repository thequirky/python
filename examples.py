import random


def make_pointcloud(fname, lines=10000):
    with open(fname, 'w+') as out_f:
        for line in range(lines):
            for i in range(5):
                x, y, z, dx, dy, dz = random.sample(range(0, 100), 6)
                f = 0.0001
                dx, dy, dz = dx*f, dy*f, dz*f
            out_f.write('%d,%d,%d,%.3f,%.3f,%.3f\n' % (x, y, z, dx, dy, dz))
