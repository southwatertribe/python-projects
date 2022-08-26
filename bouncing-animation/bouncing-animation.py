# Imports
import numpy as np
import sys
import random
import pygame
import os

# Any files imports will automatically assum to be in the bouncing-animation folder
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def bouncing_object_userinput(speed_factor=5, x0=0, y0=0):

    # Randomised x direction
    x_direction = random.choice([-1, 1])
    # Slightly randomised step sizes for x, y directions to vary simulations
    x_step, y_step = x_direction*random.randint(8, 10), -random.randint(8, 10)
    screen_size = (screen_width, screen_height) = (800, 600)
    white = (255, 255, 255)
    object_size = 30

    # For information for user
    print("The forward horizontal step size is  x_step = {}".format(x_step))
    print("The forward vertical step size is    y_step = {}".format(y_step))

    # Used for the pause time in the animation while loop below
    frames_per_second = 10 + 10*speed_factor
    clock = pygame.time.Clock()

    # Set up the animation
    pygame.init()
    screen = pygame.display.set_mode(screen_size)
    # Put the title and instructions for the animation in the title bar of the animation.
    caption = 'Bouncing object'
    caption += '                              '
    caption += '(Keystroke:  \'Space\' to start or pause)'
    pygame.display.set_caption(caption)
    # We use an image file for the object: must be in present working folder
    object = pygame.image.load("object_dvd.png")
    # We resize the image object 'object'
    object = pygame.transform.scale(object, (object_size, object_size))
    # The rectangle object_rect is used for displaying the object where (x0, y0)
    # is the top left hand corner of the rectangle (and length of sides given)
    object_rect = pygame.Rect(x0, y0, object_size, object_size)

    # object is motionless to start with
    screen.fill(white)
    # Overlay the object image on screen
    screen.blit(object, object_rect)
    # Now re-initialise the display (to show the object etc.)
    pygame.display.flip()

    # We keep going for ever in this program (until quit is input - e.g. Ctrl-Q - by user ).
    keep_running = True
    # Use the following  as switch to move the object or not using the space bar.
    move_object = False

    # Animation loop
    while keep_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keep_running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                move_object = not move_object

        # Pressing the space bar changes the value of move_object ^^^
        # So you can toggle move/not move with the space bar
        # The object is also affected by bouncing on the wall
        if move_object:
            # Move the object a step
            object_rect.x += x_step
            object_rect.y += y_step
            if object_rect.left < 0 or object_rect.right > screen_width:
                x_step = - x_step
            if object_rect.top < 0 or object_rect.bottom > screen_height:
                y_step = - y_step

        screen.fill(white)

        screen.blit(object, object_rect)

        pygame.display.flip()
        # Wait a clock tick until starting next iteration of animation loop
        clock.tick(frames_per_second)

    pygame.quit()
    return None


def run_bouncing_object_userinput():
    min_speed_factor, max_speed_factor = 1, 10
    default_speed_factor = 5

    # Get speed factor
    while True:

        speed_factor = int(input("Enter a speed (from {} to {}): ".format(
            min_speed_factor, max_speed_factor)))

        if min_speed_factor <= speed_factor and speed_factor <= max_speed_factor:

            x0 = int(
                input("Enter an x-coordinate starting position (from 0 to 770)"))

            if 0 <= x0 and x0 <= 770:

                y0 = int(
                    input("Enter a y-coordinate starting position (from 0 to 570)"))

                if 0 <= y0 and y0 <= 570:
                    bouncing_object_userinput(speed_factor, x0, y0)
                    return None

                else:
                    print("There was a problem with your y0 input.")
                    print("Using default y0 coordinate:0. ")
                    y0 = 0
                    bouncing_object_userinput(speed_factor, x0, 0)
                    return None

            else:
                print("There was a problem with your x0 input.")
                print("Using default x0 coordinate:0. ")
                x0 = 0

                y0 = int(
                    input("Enter a y-coordinate starting position (from 0 to 570)"))

                if 0 <= y0 and y0 <= 570:
                    bouncing_object_userinput(speed_factor, x0, y0)
                    return None

                else:
                    print("There was a problem with your y0 input.")
                    print("Using default y0 coordinate:0. ")
                    y0 = 0
                    bouncing_object_userinput(speed_factor, x0, 0)
                    return None

        else:
            print("There was a problem with your input.", end=" ")
            print("Using default speed speed factor:{}".format(
                default_speed_factor))
            speed_factor = default_speed_factor

            x0 = int(
                input("Enter an x-coordinate starting position (from 0 to 770)"))

            if 0 <= x0 and x0 <= 770:

                y0 = int(
                    input("Enter a y-coordinate starting position (from 0 to 570)"))

                if 0 <= y0 and y0 <= 570:
                    bouncing_object_userinput(speed_factor, x0, y0)
                    return None

                else:
                    print("There was a problem with your y0 input.")
                    print("Using default y0 coordinate:0. ")
                    y0 = 0
                    bouncing_object_userinput(speed_factor, x0, 0)
                    return None

            else:
                print("There was a problem with your x0 input.")
                print("Using default x0 coordinate:0. ")
                x0 = 0

                y0 = int(
                    input("Enter a y-coordinate starting position (from 0 to 570)"))

                if 0 <= y0 and y0 <= 570:
                    bouncing_object_userinput(speed_factor, x0, y0)
                    return None

                else:
                    print("There was a problem with your y0 input.")
                    print("Using default y0 coordinate:0. ")
                    y0 = 0
                    bouncing_object_userinput(speed_factor, x0, 0)
                    return None


run_bouncing_object_userinput()
