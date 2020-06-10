"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Jacob Oblazny.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    two_circles()
    circle_and_rectangle()
    lines()
    # Test your functions by putting calls to them here:


def two_circles():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    window = rg.RoseWindow()

    # Circle1 Instance Variables
    center1 = rg.Point(100, 150)
    radius1 = 20

    # Circle2 Instance Variables and Attachment
    center2 = rg.Point(70, 150)
    radius2 = 50

    # Construct and attach both circles
    # Fill Circle1
    Circle1 = rg.Circle(center1, radius1)
    Circle1.fill_color = 'red'
    Circle1.attach_to(window)
    Circle2 = rg.Circle(center2, radius2)
    Circle2.attach_to(window)

    window.render()
    window.close_on_mouse_click()
    # ------------------------------------------------------------------
    # DONE: 2. Implement this function, per its doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.txt  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # ------------------------------------------------------------------


def circle_and_rectangle():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    window = rg.RoseWindow()

    # Sets circle Instance Variables
    center = rg.Point(180, 115)
    radius1 = 20

    # Sets rectangle Instance Variables and Attachment
    corner1 = rg.Point(70, 50)
    corner2 = rg.Point(300, 200)

    # Constructs and attaches both circles ro window
    # Fills circle
    circle = rg.Circle(center, radius1)
    circle.fill_color = 'blue'
    circle.attach_to(window)
    rectangle = rg.Rectangle(corner1, corner2)
    rectangle.attach_to(window)

    # prints circle information
    print(circle.outline_thickness)
    print(circle.fill_color)
    print(circle.center)
    print((circle._get_coordinates_for_drawing()[2]+circle._get_coordinates_for_drawing()[0])/2)  # X coordinate
    print((circle._get_coordinates_for_drawing()[3]+circle._get_coordinates_for_drawing()[1])/2)  # Y coordinate

    # prints rectangle information
    print(rectangle.outline_thickness)
    print(rectangle.fill_color)
    print(rectangle.get_center())
    print((rectangle._get_coordinates_for_drawing()[2] + rectangle._get_coordinates_for_drawing()[0]) / 2)  # X coordinate
    print((rectangle._get_coordinates_for_drawing()[3] + rectangle._get_coordinates_for_drawing()[1]) / 2)  # Y coordinate

    window.render()
    window.close_on_mouse_click()
    # ------------------------------------------------------------------
    # DONE: 3. Implement this function, per its doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # ------------------------------------------------------------------


def lines():
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    window = rg.RoseWindow()

    # Sets line1 start and end
    start1 = rg.Point(80,90)
    end1 = rg.Point(300, 200)

    # Sets line2 start and end
    start2 = rg.Point(100, 100)
    end2 = rg.Point(121, 200)

    # Constructs and attaches both circles to window
    # Sets line2 thickness
    line1 = rg.Line(start1, end1)
    line1.attach_to(window)
    line2 = rg.Line(start2, end2)
    line2.thickness = 7
    line2.attach_to(window)

    # prints line2 midpoint information
    print(line2.get_midpoint())
    print((line2._get_coordinates_for_drawing()[2] + line2._get_coordinates_for_drawing()[0]) / 2)  # X coordinate
    print((line2._get_coordinates_for_drawing()[3] + line2._get_coordinates_for_drawing()[1]) / 2)  # Y coordinate

    window.render()
    window.close_on_mouse_click()
    # ------------------------------------------------------------------
    # DONE: 4. Implement and test this function.
    # ------------------------------------------------------------------


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
