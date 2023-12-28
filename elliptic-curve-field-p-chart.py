import numpy as np
import matplotlib.pyplot as plt

parameters = {'x_min':0, 'x_max':97, 'skip':2, 'module':43.5, 'curve':'x**3 + 7','positive_dot_color':'black', 'negative_dot_color':'red'}

#x_min: Determines the minimum value of x. It always need to be over 0
#x_max: Determines the maximum value of x. 
#skip: Determines the number of points in the chart. For example, with the value 2, the number of values is halved. 
#With 3, the number of points is iqual to the third part of the total.
#curve: Determines the type of elliptic curve. One extra example is 'x**3 - x + 1' . Always use spaces between characters. 
#positive_dot_color: Determines the color of the points that correspond to the positive part of the ellipic curve.
#negative_dot_color: Determines the color of the points that correspond to the negative part of the ellipic curve.



def elliptic_curve_p(lr, ur, sk, md, crv):

#Creates the first four lists of numbers that belong to the coordinates of the curve

  x1 = []
  y1 = []
  x2 = []
  y2 = []

 
  for i in range(lr,ur,sk):
    y1.append(curva_pos(i, crv))
    x1.append(i)
    y2.append(curva_neg(i, crv))
    x2.append(i)

  x1_mod = mod_valores(x1, md)
  y1_mod = mod_valores(y1, md)
  x2_mod = mod_valores(x2, md)
  y2_mod = mod_valores(y2, md)

  plt.plot(x1_mod, y1_mod, marker='o', linestyle='None', color=parameters['positive_dot_color'], markersize=3, label='Positive Part of the Curve')
  plt.plot(x2_mod, y2_mod, marker='o', linestyle='None', color=parameters['negative_dot_color'], markersize=3, label='Negative Part of the Curve')

  plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.18), ncol=2)
  plt.title(f'Elliptic Curve "{str(crv)}" over Field P = {md}')
  plt.axhline(y=(md/2), color='black', linestyle='--', linewidth=0.5)
  plt.show()


def curva_pos(x, curve):
  y = np.sqrt(eval(curve))
  return y

def curva_neg(x, curve):
  y_neg = -np.sqrt(eval(curve))
  return y_neg

def mod_valores(list1, mod):
    new_list = []
    for i in range(len(list1)):
        new_list.append(list1[i] % mod)
    return new_list

elliptic_curve_p(parameters['x_min'], parameters['x_max'], parameters['skip'], parameters['module'], parameters['curve'])
