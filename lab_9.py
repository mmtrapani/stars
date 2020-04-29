__author__ = 'mmt58'
# Matt Trapani and Landon Davis
# CS126-L
# Lab 9
# 10/29/2014

import turtle

coord_dict = {}
magnitude_dict = {}
name_dict = {}
cassiopea = {}
cygnet = {}
big_dipper = {}
bootes = {}
gemini = {}
hydra = {}
ursa_major = {}
ursa_minor = {}
fh = open("stars.txt", "r")
cassiopeia_handle = open("Cas_lines.txt", "r")
cygnet_handle = open("Cyg_lines.txt", "r")
big_dipper_handle = open("BigDipper_lines.txt", "r")
bootes_handle = open("Bootes_lines.txt", "r")
gemini_handle = open("Gemini_lines.txt", "r")
hydra_handle = open("Hydra_lines.txt", "r")
ursa_major_handle = open("UrsaMajor_lines.txt", "r")
ursa_minor_handle = open("UrsaMinor_lines.txt", "r")


def read_coord(file):
    coord_dict = {}
    magnitude_dict = {}
    name_dict = {}
    star_list = []
    # append each line of the file to star_list
    for line in file:
        star_list.append(line.strip())
    # convert each element from a string to a list
    for i in range(len(star_list)):
        star_list[i] = star_list[i].split(' ')
    # loop through star_list and fill the dictionaries: name_dict,
    # coord_dict, and magnitude_dict
    for star in star_list:
        coord_dict[star[3]] = (star[0], star[1])
        magnitude_dict[star[3]] = star[4]
        if len(star) >= 7:
            # create a string to hold the names of the stars
            name_string = ''
            # loop through star, starting at index 6 and going to
            # the length of star
            for index in range(6, len(star)):
                name_string = name_string + ' ' + star[index]
            name_list = name_string.split(';')
            for i in range(len(name_list)):
                name_dict[name_list[i].strip()] = star[3]
    return (coord_dict, magnitude_dict, name_dict)


def plot_plain_stars(picture_size, coord_dict):
    turtle.screensize(picture_size, picture_size, 'black')
    for star in coord_dict:
        turtle.penup()
        # position turtle at the x and y coordinate for the star
        turtle.setx(float(coord_dict[star][0]) * picture_size)
        turtle.sety(float(coord_dict[star][1]) * picture_size)
        turtle.pencolor("white")
        turtle.pendown()
        turtle.speed(10)
        draw_square(2)


def draw_square(size):
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)


def plot_by_magnitude(picture_size, coord_dict, magnitude_dict):
    turtle.screensize(picture_size, picture_size, "black")
    for star in coord_dict:
        star_size = round(10.0 / (float(magnitude_dict[star]) + 2))
        if star_size > 8:
            star_size = 8
        turtle.penup()
        # position turtle at the x and y coordinate for the star
        turtle.setx(float(coord_dict[star][0]) * picture_size)
        turtle.sety(float(coord_dict[star][1]) * picture_size)
        turtle.pencolor("white")
        turtle.fillcolor("white")
        turtle.tracer(50)
        turtle.speed(0)
        turtle.pendown()
        turtle.begin_fill()
        draw_square(star_size)
        turtle.end_fill()


def read_constellation_lines(file):
    constellation = {}
    constellation_list = file.readlines()
    for index in range(len(constellation_list)):
        constellation_list[index] = \
            constellation_list[index].strip().split(',')
    for star_to_star in constellation_list:
        # check if star is already in the constellation dictionary,
        # if it is, append the next star to the
        # constellation[star_to_star[0]] list
        if star_to_star[0] in constellation:
            constellation[star_to_star[0]].append(star_to_star[1])
        # if it is not in the list, make star_to_star[1] the first element in
        # the constellation[star_to_star[0]] list
        else:
            constellation[star_to_star[0]] = [star_to_star[1]]
    return constellation


def plot_constellations(pic_size, star_names, star_coords, constellations):
    turtle.screensize(pic_size, pic_size, "black")
    turtle.pencolor("yellow")
    # make list of the constellation keys
    starting_star = list(constellations.keys())
    # loop through the stars in the list
    for star in starting_star:
        # loop through each point_to_star in the constellations[star] list
        for point_to_star in constellations[star]:
            henry_draper = star_names[star]
            turtle.penup()
            # set x and y position for the starting point
            start_x = float(star_coords[henry_draper][0]) * pic_size
            start_y = float(star_coords[henry_draper][1]) * pic_size
            turtle.goto(start_x, start_y)
            turtle.pendown()
            henry_draper = star_names[point_to_star]
            # set x and y position for the ending point
            end_x = float(star_coords[henry_draper][0]) * pic_size
            end_y = float(star_coords[henry_draper][1]) * pic_size
            turtle.goto(end_x, end_y)


coord_dict, magnitude_dict, name_dict = read_coord(fh)
cassiopea = read_constellation_lines(cassiopeia_handle)
bootes = read_constellation_lines(bootes_handle)
big_dipper = read_constellation_lines(big_dipper_handle)
cygnet = read_constellation_lines(cygnet_handle)
gemini = read_constellation_lines(gemini_handle)
hydra = read_constellation_lines(hydra_handle)
ursa_minor = read_constellation_lines(ursa_minor_handle)
ursa_major = read_constellation_lines(ursa_major_handle)
plot_by_magnitude(200, coord_dict, magnitude_dict)
plot_constellations(200, name_dict, coord_dict, cassiopea)
plot_constellations(200, name_dict, coord_dict, bootes)
plot_constellations(200, name_dict, coord_dict, big_dipper)
plot_constellations(200, name_dict, coord_dict, cygnet)
plot_constellations(200, name_dict, coord_dict, gemini)
plot_constellations(200, name_dict, coord_dict, hydra)
plot_constellations(200, name_dict, coord_dict, ursa_minor)
plot_constellations(200, name_dict, coord_dict, ursa_major)
# used to keep the turtle graphic up until the user wants to quit
input("Press any key to continue...")
fh.close()
cassiopeia_handle.close()
cygnet_handle.close()
big_dipper_handle.close()
bootes_handle.close()
gemini_handle.close()
hydra_handle.close()
ursa_major_handle.close()
ursa_minor_handle.close()
