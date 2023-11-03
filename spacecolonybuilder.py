"""
    Space Colony Builder 0.1
"""
import pygame, random, sys
# sys.path.append("./popup_menu/gamelib/")
from popup_menu.gamelib.popup_menu import PopupMenu, NonBlockingPopupMenu, USEREVENT

# Define the VERSION
VERSION = "0.1"

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ORE = (53, 40, 0)
GOLD = (245, 198, 56)
BLUE = (0, 0, 255)
EARTH = (148, 62, 15)
LAVA = (207, 16, 32)
colors = {1:ORE, 2:GOLD, 3:BLUE, 4:EARTH, 5:LAVA}

LEFT = 1
MIDDLE = 2
RIGHT = 3

materials = {1:"earth", 2:"earth", 3:"iron", 4:"water", 5:"oxygen", 6:"earth", 7:"earth", 8:"earth"}

ROWS = 20
COLUMNS = 20

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20

# This sets the margin between each cell
MARGIN = 2

class GameBoard():

    # Define a structure to hold surface elements
    class Surface(object):
        x = 0
        y = 0
        material = ""
        def __init__(self, material):
            self.material = material

    def colorize(self, formerColor):
        if formerColor == BLUE:
            if ( random.randint(1, 5) <= 2 ):
                return BLUE
        return colors.get(random.randint(1, 5))

    def materialize(self, color):
        if color == BLUE:
            material = "water"
        elif color == ORE:
            material = "iron"
        else:
            material = materials.get(random.randint(1, 8))

    def main(self):
        # Create a 2 dimensional array. A two dimensional
        # array is simply a list of lists.
        grid = []
        for row in range(ROWS):
            # Add an empty array that will hold each cell
            # in this row
            grid.append([])
            for column in range(COLUMNS):
                grid[row].append(0)  # Append a cell

        # Set row 1, cell 5 to one. (Remember rows and
        # column numbers start at zero.)
        # grid[1][5] = 1

        # Initialize pygame
        pygame.init()

        # Set the HEIGHT and WIDTH of the screen
        WINDOW_SIZE = [((WIDTH+MARGIN)*ROWS), ((HEIGHT+MARGIN)*COLUMNS)]
        screen = pygame.display.set_mode(WINDOW_SIZE)

        # Set title of screen
        pygame.display.set_caption("Space Colony Builder " + VERSION)

        # Loop until the user clicks the close button.
        done = False

        # Used to manage how fast the screen updates
        clock = pygame.time.Clock()

        # Draw the grid
        color = EARTH
        for row in range(ROWS):
            for column in range(COLUMNS):
                color = self.colorize(color)
                pygame.draw.rect(screen,
                                 color,
                                 [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                  WIDTH,
                                  HEIGHT])

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # -------- Main Program Loop -----------
        while not done:
            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    done = True  # Flag that we are done so we exit this loop
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                    # User clicks the mouse. Get the position
                    pos = pygame.mouse.get_pos()
                    # Change the x/y screen coordinates to grid coordinates
                    column = pos[0] // (WIDTH + MARGIN)
                    row = pos[1] // (HEIGHT + MARGIN)
                    # Set that location to one
                    grid[row][column] = 1
                    print("Click ", pos, "Grid coordinates: ", row, column)
                    print("Clicked left button at (%d, %d)" % event.pos)
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:
                    menu_data = ['Main', 'Item 0', ['Submenu', 'Item 0'], 'Quit']
#                    while 1:
                        # game stuff...
#                        NonBlockingPopupMenu(menu_data)
                    PopupMenu(menu_data)
                    print("event.type ", event.type ," event.code ", event.code)
                    if event.type == USEREVENT and event.code == 'MENU':
                        printf('menu event: %s.%d: %s' % (e.name,e.item_id,e.text))
                        if (event.name,event.text) == ('Main','Quit'):
                            quit()
                        else:
                            # handle all game events normally
                            pass

                    print("Clicked right button at (%d, %d)" % event.pos)
                    self.doPopup()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == MIDDLE:
                    print("Clicked middle button at (%d, %d)" % event.pos)

            # Set the screen background
        #    screen.fill(BLACK)

            # Limit to 60 frames per second
            clock.tick(60)

            # Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

        # Be IDLE friendly. If you forget this line, the program will 'hang'
        # on exit.
        pygame.quit()


if __name__ == "__main__":
    game = GameBoard()
    game.main()
