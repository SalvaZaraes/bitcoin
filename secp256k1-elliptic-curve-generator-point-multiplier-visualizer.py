import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# DUPLICATE (TANGENT)

def dup(tangent_coordinates, function):

    # Take the positive or negative part of the function based on the y-value of the coordinates to duplicate
    if tangent_coordinates[1] > 0:
        selected_function = function
    elif tangent_coordinates[1] < 0:
        selected_function = -(function)

    # Calculate the derivative of the function with respect to x
    expr_slope_tangent = sp.diff(selected_function, x)

    # Slope value
    slope_value = expr_slope_tangent.subs(x, tangent_coordinates[0])

    # Possible x-coordinates of the Intersection Point of the Tangent with the Curve
    pcx_tangent = sp.solve((((slope_value * (x - tangent_coordinates[0])) + tangent_coordinates[1])**2 - (function**2)), x)

    # Convert values to real, removing the imaginary part
    pc_real_tangent = [sp.re(a) for a in pcx_tangent]

    # Remove values of x similar to the coordinates to be duplicated
    point_c_x = [x_val for x_val in pc_real_tangent if abs(x_val - tangent_coordinates[0]) > 1e-4][0]

    # Calculate its y-coordinate with the remaining x value
    point_c_y = ((slope_value * (point_c_x - tangent_coordinates[0])) + tangent_coordinates[1])

    # Take the reflected value, which is the true result of duplication (e.g., 2G) and not its negative version (e.g., -2G)
    reflected_tangent_point = (point_c_x, -point_c_y)

    return reflected_tangent_point

# SUM POINTS

def sum_pt(lower_x, upper_x, function):

    # Define values
    values = [lower_x, upper_x]

    # Slope value
    slope_value_sum = ((values[1][1] - values[0][1]) / (values[1][0] - values[0][0]))

    # Possible x-coordinates of the Crossing Point of the Line that adds two pairs of Coordinates on the Curve
    pcx_sum = sp.solve((((slope_value_sum * (x - values[0][0])) + values[0][1])**2 - (function**2)), x)

    # Convert values to real, removing the imaginary part
    pc_real_sum = [sp.re(a) for a in pcx_sum]

    # Remove values of x similar to the two pairs of coordinates to be summed
    point_c_sum_x = [x_val for x_val in pc_real_sum if all(abs(x_val - val[0]) > 1e-4 for val in values)][0]

    # Calculate its y-coordinate with the remaining x value
    point_c_sum_y = ((slope_value_sum * (point_c_sum_x - values[0][0])) + values[0][1])

    # Take the reflected value, which is the true result of summing (e.g., 3G) and not its negative version (e.g., -3G)
    reflected_sum_point = (point_c_sum_x, -point_c_sum_y)

    return reflected_sum_point

# STEPS
# This function allows us to determine how many times the Generator Point has to be duplicated and/or summed to find the desired multiple.
# The multiple of G is divided by two, and depending on the remainder, if it is 0, it will be duplicated, and if it is 1, it will be duplicated and then the original G point will be summed.

def steps(num):
    actions_list = []
    if multiplo_g == 1:
        print('You already have the point')
    else:
        while num > 1:
            if num % 2 == 0:
                actions_list.append(0)
                num = num / 2
            elif num % 2 == 1:
                actions_list.append(1)
                actions_list.append(0)
                num = (num - 1) / 2
            # 0 Implies Duplicate
            # 1 Implies Add the Original G Point
        # Reverse the list.
        actions_list = actions_list[::-1]

    return actions_list

# LIST TO BE PRINTED BY GRAPH
# This function creates the list of orders that will be passed to the print function
# This list takes the previous list of actions composed of 0s and 1s, and depending on that value, it will call the dup() or sum_pt() function to perform
# the necessary calculations. Once it obtains the result, it stores it in a list (list_points).

def create_point_list(actions_list, coordinates_G):
    list_points = []
    starting_coordinates = coordinates_G

    for i in range(0, len(actions_list)):

        if actions_list[i] == 0:
            reflected_point = dup(starting_coordinates, expr_func)
            list_points.append(([starting_coordinates], [reflected_point]))
            starting_coordinates = reflected_point

        else:
            if starting_coordinates[0] < coordinates_G[0]:
                reflected_point = sum_pt(starting_coordinates, coordinates_G, expr_func)
                list_points.append(([starting_coordinates], [reflected_point]))
                starting_coordinates = reflected_point
            elif starting_coordinates[0] > coordinates_G[0]:
                reflected_point = sum_pt(coordinates_G, starting_coordinates, expr_func)
                list_points.append(([starting_coordinates], [reflected_point]))
                starting_coordinates = reflected_point

    return list_points


def plot_graph(list_points, steps_to_print):

    

    # Here we can adjust the range of values that x takes from the elliptic curve. You can adjust it to draw the curve in a larger domain.
    # np.linspace(smaller_x_range, larger_x_range, number of points taken to draw the curve)
    values_x = np.linspace(-10, 10, 1000)

    # Calculate the curve for both sides
    y_positive = np.sqrt(values_x**3 + 7)
    y_negative = -np.sqrt(values_x**3 + 7)

    fig, ax = plt.subplots()
    # Draw the curve for both sides
    ax.plot(values_x, y_positive, color="blue", label="Elliptic Curve secp256k1")
    ax.plot(values_x, y_negative, color="blue")

    # Add data to the legend
    red_line = Line2D([0], [0], color='red', linewidth=2, label='Duplicate the point')
    green_line = Line2D([0], [0], color='green', linewidth=2, label='Sum points')
    ax.legend(handles=[red_line, green_line])
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    # Adjust the font and label placements
    font = 7
    xy = (0, 10)

    for i in range(0, len(steps_to_print)):
        # Print the lines of duplications and the respective points on the screen
        if steps_to_print[i] == 0:
            ax.plot([list_points[i][0][0][0], list_points[i][1][0][0]], [list_points[i][0][0][1], -list_points[i][1][0][1]], 'r-', color='red')
            ax.plot([list_points[i][1][0][0], list_points[i][1][0][0]], [list_points[i][1][0][1], -list_points[i][1][0][1]], 'r--', color='grey')
            ax.scatter([list_points[i][0][0][0], list_points[i][1][0][0], list_points[i][1][0][0]], [list_points[i][0][0][1], list_points[i][1][0][1], -list_points[i][1][0][1]], color='black', s=20)
            ax.scatter([list_points[0][0][0][0]], [list_points[0][0][0][1]], color='orange', s=40, zorder=10)

        # Print the lines of sums and the respective points on the screen
        if steps_to_print[i] == 1:
            ax.plot([list_points[i][0][0][0], list_points[i][1][0][0]], [list_points[i][0][0][1], -list_points[i][1][0][1]], 'r-', color='green')
            ax.plot([list_points[0][0][0][0], list_points[i][1][0][0]], [list_points[0][0][0][1], -list_points[i][1][0][1]], 'r-', color='green')

            ax.plot([list_points[i][1][0][0], list_points[i][1][0][0]], [list_points[i][1][0][1], -list_points[i][1][0][1]], 'r--', color='grey')
            ax.scatter([list_points[i][1][0][0], list_points[i][1][0][0]], [list_points[i][1][0][1], -list_points[i][1][0][1]], color='black', s=20)

    G_counter = 1
    for i in range(0, len(steps_to_print)):

        # Print on screen the Labels of the Generator Point and its multiples
        if steps_to_print[i] == 0 and i == 0:

            ax.annotate('G', (list_points[i][0][0][0], list_points[i][0][0][1]), textcoords="offset points", xytext=(0, 5), ha='center', fontsize=font)

            G_counter += 1

            ax.annotate(f'{G_counter}G', (list_points[i][1][0][0],list_points[i][1][0][1]), textcoords="offset points", xytext=xy, ha='center', fontsize=font)
  
            ax.annotate(f'-{G_counter}G', (list_points[i][1][0][0],-list_points[i][1][0][1]), textcoords="offset points", xytext=xy, ha='center', fontsize=font)
        
        if steps_to_print[i] == 0 and i != 0:  

            G_counter = G_counter * 2

            ax.annotate(f'{G_counter}G', (list_points[i][1][0][0],list_points[i][1][0][1]), textcoords="offset points", xytext=xy, ha='center', fontsize=font)
      
            ax.annotate(f'-{G_counter}G', (list_points[i][1][0][0],-list_points[i][1][0][1]), textcoords="offset points", xytext=xy, ha='center', fontsize=font)
      
        if steps_to_print[i] == 1:

            G_counter += 1
            ax.annotate(f'{G_counter}G', (list_points[i][1][0][0],list_points[i][1][0][1]), textcoords="offset points", xytext=xy, ha='center', fontsize=font)
      
            ax.annotate(f'-{G_counter}G', (list_points[i][1][0][0],-list_points[i][1][0][1]), textcoords="offset points", xytext=xy, ha='center', fontsize=font)
      

    # Set aspect ratio
    # You can remove these lines to let matplotlib adjust the aspect ratio
    plt.ylim(-7, 7)
    plt.xlim(-7, 7)

    plt.show()

if __name__ == '__main__':

    # Define the symbol
    x = sp.symbols('x')

    # Define the symbolic function with sp.sqrt
    expr_func = (x**3 + 7)**(1/2)

  

    generator_point = (-1, sp.sqrt(6))

    # generator_multiple = int(input('What is the multiple of the Generator Point?'))
    generator_multiple = 3
    

    graph_input1 = create_point_list(steps(generator_multiple), generator_point)
    graph_input2 = steps(generator_multiple)

    plot_graph(graph_input1, graph_input2)
