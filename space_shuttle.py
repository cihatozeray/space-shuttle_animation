# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 15:31:11 2020

@author: Cihat Özeray

Tkinter canvas study
"""

from tkinter import Tk, Canvas, mainloop
import random

master = Tk()
canvas1 = Canvas(master, width=800, height=800, bg="midnight blue")
canvas1.pack()


def create_spaceshuttle(y_tip):
    """
    creates spaceshuttle object for visualisation
    y_tip will be used later for the vertical movement of the shuttle
    That's why it is the main paramater
    """
    canvas_width = 800

    def rocket_coordinates(tip_position_x, tip_position_y, main_height, main_width):
        """
        generates edge point coordinates for a rocket like polygon (for general use)
        """
        x_tip = tip_position_x
        y_tip = tip_position_y
        x_tip_right = x_tip + main_width / 2
        y_tip_right = (y_tip + main_width / 2)
        x_tip_left = x_tip - main_width / 2
        y_tip_left = y_tip_right
        x_bottom_right = x_tip_right
        y_bottom_right = (y_tip + main_height)
        x_bottom_left = x_tip_left
        y_bottom_left = y_bottom_right
        coordinates = [x_tip, y_tip, x_tip_right, y_tip_right, x_bottom_right, y_bottom_right,\
            x_bottom_left, y_bottom_left, x_tip_left, y_tip_left]
        return coordinates

    def shuttle_coordinates(tip_position_x, tip_position_y, top_height, top_width,\
        middle_height, middle_width, bottom_height, bottom_width):
        """
        generates edge point coordinates for a shuttle like polygon (for general use)
        """
        x1 = tip_position_x
        y1 = tip_position_y
        x2 = tip_position_x + top_width / 2
        y2 = tip_position_y + top_height
        x3 = tip_position_x + middle_width / 2
        y3 = y2 + middle_height
        x4 = tip_position_x + bottom_width / 2
        y4 = y3 + bottom_height
        x5 = tip_position_x - bottom_width / 2
        y5 = y4
        x6 = tip_position_x - middle_width / 2
        y6 = y3
        x7 = tip_position_x - top_width / 2
        y7 = y2
        coordinates = [x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7]
        return coordinates

    def external_tank():
        """
        returns edge points of the external tank
        """
        tip_position_x = canvas_width / 2
        tip_position_y = y_tip
        main_height = 80
        main_width = 20
        return rocket_coordinates(tip_position_x, tip_position_y, main_height, main_width)

    def left_rocket():
        """
        returns edge points of the left rocket
        """
        tip_position_x = canvas_width / 2 - 15
        tip_position_y = y_tip + 20
        main_height = 62
        main_width = 8
        return rocket_coordinates(tip_position_x, tip_position_y, main_height, main_width)

    def right_rocket():
        """
        returns edge points of the right rocket
        """
        tip_position_x = canvas_width / 2 + 15
        tip_position_y = y_tip + 20
        main_height = 62
        main_width = 8
        return rocket_coordinates(tip_position_x, tip_position_y, main_height, main_width)

    def main_shuttle():
        """
        returns edge points of the space shuttle
        """
        tip_position_x = canvas_width / 2
        tip_position_y = y_tip + 13
        top_height = 10
        top_width = 16
        middle_height = 35
        middle_width = 30
        bottom_height = 17
        bottom_width = 68
        return shuttle_coordinates(tip_position_x, tip_position_y, top_height, top_width,\
        middle_height, middle_width, bottom_height, bottom_width)

    def main_shuttle_tip():
        """
        returns edge points of the tip of the shuttle
        """
        tip_position_x = canvas_width / 2
        tip_position_y = y_tip + 13
        top_height = 5
        top_width = 8
        middle_height = 1
        middle_width = 8
        bottom_height = 1
        bottom_width = 8
        return shuttle_coordinates(tip_position_x, tip_position_y, top_height, top_width,\
        middle_height, middle_width, bottom_height, bottom_width)

    def main_shuttle_body():
        """
        returns edge points of the shuttle body
        """
        tip_position_x = canvas_width / 2
        tip_position_y = y_tip + 13
        top_height = 10
        top_width = 14
        middle_height = 35
        middle_width = 14
        bottom_height = 12
        bottom_width = 14
        return shuttle_coordinates(tip_position_x, tip_position_y, top_height, top_width,\
        middle_height, middle_width, bottom_height, bottom_width)

    def main_shuttle_lines():
        """
        returns edge points of the shuttle for lining
        """
        tip_position_x = canvas_width / 2
        tip_position_y = y_tip + 15
        top_height = 8
        top_width = 14
        middle_height = 35
        middle_width = 26
        bottom_height = 15
        bottom_width = 65
        temp = shuttle_coordinates(tip_position_x, tip_position_y, top_height, top_width,\
        middle_height, middle_width, bottom_height, bottom_width)
        temp = temp + [tip_position_x, tip_position_y]
        return temp

    def main_shuttle_left_nozzle():
        """
        returns edge points of the left nozzle of the shuttle
        """
        tip_position_x = canvas_width / 2 - 8
        tip_position_y = y_tip + 65
        top_height = 2
        top_width = 8
        middle_height = 2
        middle_width = 10
        bottom_height = 10
        bottom_width = 12
        return shuttle_coordinates(tip_position_x, tip_position_y, top_height, top_width,\
        middle_height, middle_width, bottom_height, bottom_width)

    def main_shuttle_right_nozzle():
        """
        returns edge points of the right nozzle of the shuttle
        """
        tip_position_x = canvas_width / 2 + 8
        tip_position_y = y_tip + 65
        top_height = 2
        top_width = 8
        middle_height = 2
        middle_width = 10
        bottom_height = 10
        bottom_width = 12
        return shuttle_coordinates(tip_position_x, tip_position_y, top_height, top_width,\
        middle_height, middle_width, bottom_height, bottom_width)

    def left_rocket_nozzle():
        """
        returns edge points of the nozzle of left rocket
        """
        tip_position_x = canvas_width / 2 - 15
        tip_position_y = y_tip + 82
        top_height = 2
        top_width = 8
        middle_height = 8
        middle_width = 16
        bottom_height = 2
        bottom_width = 18
        return shuttle_coordinates(tip_position_x, tip_position_y, top_height, top_width,\
        middle_height, middle_width, bottom_height, bottom_width)

    def right_rocket_nozzle():
        """
        returns edge points of the nozzle of right rocket
        """
        tip_position_x = canvas_width / 2 + 15
        tip_position_y = y_tip + 82
        top_height = 2
        top_width = 8
        middle_height = 8
        middle_width = 16
        bottom_height = 2
        bottom_width = 18
        return shuttle_coordinates(tip_position_x, tip_position_y, top_height, top_width,\
        middle_height, middle_width, bottom_height, bottom_width)

    canvas1.create_polygon(external_tank(), fill="red", width=5)
    canvas1.create_polygon(left_rocket(), fill="ivory2", width=5)
    canvas1.create_polygon(right_rocket(), fill="ivory2", width=5)
    canvas1.create_polygon(main_shuttle(), fill="white", width=5)
    canvas1.create_polygon(main_shuttle_tip(), fill="black")
    canvas1.create_line(main_shuttle_lines(), width=1)
    canvas1.create_line(main_shuttle_body(), width=1, fill="grey")
    canvas1.create_polygon(left_rocket_nozzle(), fill="light grey")
    canvas1.create_polygon(right_rocket_nozzle(), fill="light grey")
    canvas1.create_polygon(main_shuttle_left_nozzle(), fill="grey")
    canvas1.create_polygon(main_shuttle_right_nozzle(), fill="grey")


def draw_polygons():
    """
    for imitating stars or sky particles
    """
    x1 = random.randint(1, 1000)
    y1 = random.randint(1, 1000)
    width = random.randint(2, 5)
    height = random.randint(2, 5)
    x2 = x1 + width / 2
    y2 = y1 + height / 2
    x3 = x1 + width
    y3 = y1 + height
    x4 = x1
    y4 = y1 + height / 3
    x5 = x1 - width / 2
    y5 = y1 + height / 2
    canvas1.create_polygon(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, fill="white")


def fire1():
    """
    creates thicker fire near nozzle
    """
    fire_color = ["red", "gold"]
    temp = len(fire_color)
    color_index = random.randint(0, temp-1)

    x1 = random.randint(400-20, 400-10)
    y1 = random.randint(393, 400)
    width = random.randint(1, 2)
    height = random.randint(1, 2)
    x2 = x1 + width
    y2 = y1 + height
    canvas1.create_rectangle(x1, y1, x2, y2, fill=fire_color[color_index], width=0)

    x1 = random.randint(400+10, 400+20)
    y1 = random.randint(393, 400)
    width = random.randint(1, 2)
    height = random.randint(1, 2)
    x2 = x1 + width
    y2 = y1 + height
    canvas1.create_rectangle(x1, y1, x2, y2, fill=fire_color[color_index], width=0)


def fire2():
    """
    creates mild fire after leaving nozzle
    """
    fire_color = ["gold", "white"]
    temp = len(fire_color)
    color_index = random.randint(0, temp-1)
    x1 = random.randint(400-18, 400-12)
    y1 = random.randint(400, 420)
    width = random.randint(1, 2)
    height = random.randint(1, 2)
    x2 = x1 + width
    y2 = y1 + height
    canvas1.create_rectangle(x1, y1, x2, y2, fill=fire_color[color_index], width=0)

    x1 = random.randint(400+12, 400+18)
    y1 = random.randint(400, 420)
    width = random.randint(1, 2)
    height = random.randint(1, 2)
    x2 = x1 + width
    y2 = y1 + height
    canvas1.create_rectangle(x1, y1, x2, y2, fill=fire_color[color_index], width=0)


def fire3():
    """
    creates thinner fire as getting further from nozzle
    """
    fire_color = ["white", "gold"]
    temp = len(fire_color)
    color_index = random.randint(0, temp-1)
    x1 = random.randint(400-16, 400-14)
    y1 = random.randint(420, 440)
    width = random.randint(1, 2)
    height = random.randint(1, 2)
    x2 = x1 + width
    y2 = y1 + height
    canvas1.create_rectangle(x1, y1, x2, y2, fill=fire_color[color_index], width=0)

    x1 = random.randint(400+14, 400+16)
    y1 = random.randint(420, 440)
    width = random.randint(1, 2)
    height = random.randint(1, 2)
    x2 = x1 + width
    y2 = y1 + height
    canvas1.create_rectangle(x1, y1, x2, y2, fill=fire_color[color_index], width=0)


def fire_core():
    """
    creates a triangle representing default core of fire near nozzle
    """
    width = random.randint(2, 4)
    height = random.randint(5, 7)
    x1 = 400 - 22 + width
    y1 = 393
    x2 = 385
    y2 = 400 + height
    x3 = 400 - 8 - width
    y3 = 393
    canvas1.create_polygon(x1, y1, x2, y2, x3, y3, fill="gold", width=0)

    x1 = 400 + 22 - width
    y1 = 393
    x2 = 415
    y2 = 400 + height
    x3 = 400 + 8 + width
    y3 = 393
    canvas1.create_polygon(x1, y1, x2, y2, x3, y3, fill="gold", width=0)


def dispatch():
    """
    visualization of the shapes
    """
    canvas1.delete("all")
    for i in range(20):
        draw_polygons()
    for i in range(30):
        fire1()
    for i in range(15):
        fire2()
    for i in range(4):
        fire3()
    fire_core()
    create_spaceshuttle(300)
    master.after(150, dispatch) # 0.15 seconds


dispatch()
mainloop()
