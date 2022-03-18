import random
import matplotlib.pyplot as plt 
import numpy as np
import time
repeats = 10000

SCALE = 0.005

circle_points, square_points = 0,0
figure,axes = plt.subplots()

GREEN = (0.1, 0.9, 0.1, 1)
BLUE = (0.2, 0.2, 0.9, 1)
def draw_circle():
    x_range = np.linspace(-1, 1, 150)
    y_range = np.linspace(-1, 1, 150)
    a,b = np.meshgrid(x_range,y_range)
    C = a**2 + b**2 -0.98
    axes.contour(a,b,C,[0])
    axes.set_aspect(1)
    plt.title(f"Pi Estimation={pi}")
    plt.show()
    
    
    

RUN = True
while RUN:
    for i in range(repeats):
        rand_x =random.uniform(-1, 1)
        rand_y =random.uniform(-1, 1)
        origin_dist = rand_x**2 + rand_y**2
        
        if origin_dist <= 1:
            COLOR = GREEN
        else:
            COLOR = BLUE
            
        xy_circle = plt.Circle((rand_x, rand_y), SCALE, color=COLOR)
        axes.set_aspect(1)
        axes.add_artist(xy_circle)
        
        
        
        
        if origin_dist <= 1:
            circle_points += 1
        
        square_points += 1
        
        pi = 4 * circle_points/square_points
        
    
    draw_circle()
    RUN=False



print("Pi estimation= ", pi)