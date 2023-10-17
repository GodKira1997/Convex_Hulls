"""
file: graham_scan.py
description: This program implements the graham scan algorithm on given
input file containing points
language: python3
author: Anurag Kallurwar, ak6491@rit.edu
"""


import sys
from time import perf_counter
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


def half_hull(points: list):
    """
    Creates half a hull from given points
    :param points: input points
    :return: Half hull
    """
    stack = []
    stack.append(points[0])
    stack.append(points[1])
    for index in range(2, len(points)):
        while len(stack) >= 2 and orient(points[index], stack[-1], stack[-2])\
                <= 0:
            stack.pop()
        stack.append(points[index])
    return stack


def graham_scan(number_of_points: int, points: list):
    """
    Creates convex hull using graham scan algorithm
    :param number_of_points: number of points
    :param points: input points
    :return: convex hull points
    """
    if number_of_points < 3:
        return "Convex Hull not possible"
    sorted_by_x = sorted(points, key = lambda point : point[0])
    convex_hull = half_hull(sorted_by_x) + half_hull(sorted_by_x[::-1])[1:-1]
    return convex_hull[::-1]


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
    ax.set_title("Graham Scan")
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
    output_file_name = "output_graham.txt"
    # file_name = input("Input file name: ")
    # Reading input
    number_of_points, points = read_input(file_name)
    start = perf_counter()
    # Convex Hull
    convex_hull = graham_scan(number_of_points, points)
    elapsed_time = perf_counter() - start
    print ("Running Time: {:.6f}".format(elapsed_time))
    print("Convex Hull: ")
    print(convex_hull)
    # Writing Output and plotting
    write_output(output_file_name, convex_hull)
    plot_output(points, convex_hull)


if __name__ == '__main__':
    main()  # Calling Main Function
