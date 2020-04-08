def distort_pointcloud(from_file, factor=1, separator=','):
    """
    Accepts a nominal pointcloud and point deviations and returns the
    distorted pointcloud. Use a factor of -1 to reverse distortion or a factor
    of 2 to magnify distortion
    """

    with open(from_file, 'r') as f:
        lines = f.readlines()

    with open('output.txt', 'w+') as out_f:
        for line in lines:
            x, y, z, dx, dy, dz = [float(i) for i in line.split(separator)[:6]]
            dx, dy, dz = factor*dx, factor*dy, factor*dz
            out_f.write('%.3f,%.3f,%.3f\n' % (x+dx, y+dy, z+dz))

    return


if __name__ == "__main__":

    from examples import make_pointcloud

    make_pointcloud(fname='original_pointcloud.txt')
    distort_pointcloud(from_file="original_pointcloud.txt")
