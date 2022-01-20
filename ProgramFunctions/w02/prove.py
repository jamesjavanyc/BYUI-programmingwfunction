# -*- coding: utf-8 -*-
# @Time    : 2022/1/8 18:14
# @Author  : Junzhou Liu
# @FileName: prove.py
# @Software: PyCharm
# Import the functions from the Draw 2-D library
# so that they can be used in this program.
import random

from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    scene_width = 800
    scene_height = 500

    canvas = start_drawing("Scene", scene_width, scene_height)

    draw_sky(canvas, 800, 500)
    draw_ground(canvas, 800, 500)

    finish_drawing(canvas)


# requirement 1 The scene must be outdoor and include part of the sky.
def draw_sky(canvas, scene_width, scene_height):
    """Draw the sky and all the objects in the sky."""
    draw_rectangle(canvas, 0, scene_height / 3, scene_width, scene_height, width=0, fill="sky blue")
    # requirements 3  The scene must include repetitive objects, such as blades of grass, trees, leaves on a tree, birds, flowers, insects, fish, pickets in a fence, dashed lines on a road, buildings, bales of hay, snowmen, snowflakes, or icicles.
    draw_cloud(canvas, 500, 400, 170, 40)
    draw_cloud(canvas, 100, 350, 220, 60)
    draw_cloud(canvas, 190, 390, 180, 40)
    draw_sun(canvas, 300, 400)


def draw_ground(canvas, scene_width, scene_height):
    """Draw the ground and all the objects on the ground."""
    draw_rectangle(canvas, 0, 0, scene_width, scene_height / 3, width=0, fill="green")
    draw_mountain(canvas, scene_width, scene_height)
    draw_house(canvas, 400, 100, 180, 120)
    draw_tree(canvas, scene_width, 0)


# requirements 2 The sky must have clouds
def draw_cloud(canvas, x, y, width, height):
    draw_oval(canvas, x, y, x + width, y + 2 * height / 3, outline="snow1", fill="snow1")
    draw_oval(canvas, x + 0.2 * width, y + 0.5 * height, x + 0.8 * width, y + height, outline="snow1", fill="snow1")


def draw_house(canvas, x, y, width, height):
    draw_rectangle(canvas, x + 0.1 * width, y, x + 0.9 * width, 0.67 * height + y, width=0, fill="cornsilk2")
    draw_polygon(canvas, x, y + 0.67 * height, x + width, y + 0.67 * height, x + 0.5 * width, y + height, outline="brown", fill="brown")


def draw_sun(canvas, x, y):
    draw_oval(canvas, x, y, x + 50, y + 50, outline="gold", fill="gold")


def draw_mountain(canvas, scene_width, scene_height):
    x, y = 0, 0
    while x < scene_width:
        width, height = random.randint(180, 280), random.randint(50, 80)
        draw_polygon(canvas, x + 0.2 * width, scene_height / 3, x + 0.5 * width, scene_height / 3 + height, x + 0.8 * width, scene_height / 3, outline="snow1", fill="snow1")
        draw_polygon(canvas, x, scene_height / 3, x + 0.5 * width, scene_height / 3 + 0.9 * height, x + width, scene_height / 3, outline="black", fill="antiqueWhite4")
        x = x + 0.8 * width


# exceeding requirements: recursion calling to draw the tree
def draw_tree(canvas, scene_width, x):
    y = random.randint(0, 100)
    if x >= scene_width - 30:
        return
    elif x == 0:
        x = random.randint(50, 150)
    draw_rectangle(canvas, x, y, x + 5, y + 30, width=0, fill="brown")
    draw_polygon(canvas, x-10, y + 30, x + 3, y + 60, x + 15, y + 30, outline="springGreen1", fill="springGreen1")
    draw_tree(canvas, scene_width, x + random.randint(50, 150))


main()
