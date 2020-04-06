def distorted_pointcloud(input_file, factor=1):
    """Accepts a nominal pointcloud and point deviations and returns the
    distorted pointcloud. Use a factor of -1 to reverse distortion"""

    with open(input_file, 'r') as f:
        lines = f.readlines()

    with open('output.txt', 'w+') as out_f:
        for line in lines:
            x, y, z, dx, dy, dz = [float(i) for i in line.split(',')[:6]]
            out_f.write(f"{x+factor*dx},{y+factor*dy},{z+factor*dz}\n")

    return
