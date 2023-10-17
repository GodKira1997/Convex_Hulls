"""
file: brute_force.py
description: This program implements the slow convex hull algorithm on given
input file containing points
language: python3
author: Anurag Kallurwar, ak6491@rit.edu
"""


import sys
from time import perf_counter
import math
import matplotlib.pyplot as plt


def read_input(file_name: str):
    """
    Read input from file
    :param file_name: name of file
    :return: None
    """
    lines = []
    points = []
    with open(file_name, 'r') as file:
        lines = file.readlines()
    number_of_points = int(lines[0])
    for line in lines[1:]:
        point = [float(a) for a in line.split(' ')]
        points.append(tuple(point))
    return number_of_points, points


def write_output(file_name: str, convex_hull: list):
    """
    Write convex hull points to a file
    :param file_name: name of file
    :param convex_hull: convex hull points
    :return: None
    """
    with open(file_name, 'w') as file:
        file.write(str(len(convex_hull)) + "\n")
        for point in convex_hull:
            x = "{:.2f}".format(point[0])
            y = "{:.2f}".format(point[1])
            file.write(x + " " + y + '\n')


def orient(pointP: tuple, pointQ: tuple, pointR):
    """
    Get the orientation between three points
    :param pointP: Point P
    :param pointQ: Point Q
    :param pointR: Point R
    :return: Integer
    """
    result = (pointQ[0] * pointR[1] - pointR[0] * pointQ[1]) - \
             (pointP[0] * pointR[1] - pointR[0] * pointP[1]) + \
             (pointP[0] * pointQ[1] - pointQ[0] * pointP[1])
    if result > 0: # Counter-Clockwise
        return 1
    elif result < 0: # Clockwise
        return -1
    return 0 # Collinear


def polar_angle(point: tuple, centroid: tuple):
    """
    Get the polar angle of point with respect to centroid
    :param point: input point
    :param centroid: calculated centroid for inputs
    :return: float polar angle
    """
    return math.atan2(point[1] - centroid[1], point[0] - centroid[0])


def sort_counter_clockwise(points: list):
    """
    Sort the given points in counter clockwise order
    :param points: input points
    :return: points in counter clockwise order
    """
    centroid_x = (sum(x for x, y in points)) / len(points)
    centroid_y = (sum(y for x, y in points)) / len(points)
    centroid = (centroid_x, centroid_y)
    counter_clockwise = sorted(points, key=lambda point: polar_angle(point,
                                                                centroid))
    return counter_clockwise


def slow_convex_hull(number_of_points: int, points: list):
    """
    Creates convex hull using slow convex hull algorithm
    :param number_of_points: number of points
    :param points: input points
    :return: convex hull points
    """
    if number_of_points < 3:
        return "Convex Hull not possible"
    convex_hull = []
    for index1 in range(number_of_points):
        for index2 in range(number_of_points):
            if points[index1] != points[index2]:
                valid = True
                for index3 in range(number_of_points):
                    # Check if P, Q and R are same
                    if points[index3] != points[index1] and points[index3] != \
                            points[index2]:
                        val =  orient(points[index1], points[index2], points[
                            index3])
                        # Check for points only on right (Clockwise)
                        if val == -1:
                            valid = False
                            break
                if valid: # If All the points are on left or hull
                    if points[index1] not in convex_hull:
                        convex_hull.append(points[index1])
                    if points[index2] not in convex_hull:
                        convex_hull.append(points[index2])
    return sort_counter_clockwise(convex_hull)


def plot_output(points: list, convex_hull: list):
    """
    Plot the points and convex hull
    :param points: input points
    :param convex_hull: convex hull
    :return: None
    """
    points_x = [point[0] for point in points]
    points_y = [point[1] for point in points]
    convex_hull_x = [point[0] for point in convex_hull] + [convex_hull[0][0]]
    convex_hull_y = [point[1] for point in convex_hull] + [convex_hull[0][1]]

    fig, ax = plt.subplots()
    ax.set_title("Slow Convex Hull")
    ax.plot(convex_hull_x, convex_hull_y, c='b', label='Convex Hull')
    ax.scatter(points_x, points_y, s=20, c='r', label='Points')
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_aspect('equal')
    ax.legend(bbox_to_anchor=(1.0, 1), loc='upper left', fontsize=7)
    plt.tight_layout()
    plt.show()


def main():
    """
    The main function
    :return: None
    """
    # Check for CLI paramters
    if len(sys.argv) < 2:
        print("Please provide an input file")
        print("USAGE: brute_force.py <filename.txt>")
        return
    file_name = str(sys.argv[1])
    output_file_name = "output_brute.txt"
    # file_name = input("Input file name: ")
    # Reading input
    number_of_points, points = read_input(file_name)
    start = perf_counter()
    # Convex Hull
    convex_hull = slow_convex_hull(number_of_points, points)
    elapsed_time = perf_counter() - start
    print("Running Time: {:.6f}".format(elapsed_time))
    print("Convex Hull: ")
    print(convex_hull)
    # Writing Output and plotting
    write_output(output_file_name, convex_hull)
    plot_output(points, convex_hull)


if __name__ == '__main__':
    main()  # Calling Main Function
