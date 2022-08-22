import pygame
import random
import time

class Program:
    def __init__(self, screen_size, font_size, background_colour):
        self.__screen_size = screen_size
        self.__font_size = font_size
        self.__screen = pygame.display.set_mode(screen_size)
        self.__caption = "Sorting Algorithms"
        self.__background_colour = background_colour
        self.__bars = []

    def run(self):
        pygame.font.init()
        text_font = pygame.font.SysFont('Calibri', self.__font_size)
        
        pygame.display.set_caption(self.__caption)
        self.__screen.fill(self.__background_colour)
        clock = pygame.time.Clock()
        
        # create the bars to be drawn on screen
        self.create_bars(100)
        # randomise the positions of the bars
        self.randomise_bar_position()
        # rearrange the order of bars in the __bars list, in order to match the visual list
        self.__bars = self.rearrange_bars_list()

        end = False
        while not end:
            clock.tick(60)
           

            self.bubble_sort()
            input()
            break
          

            # QUIT
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    end = True

    def draw_screen(self):
        # DRAWING LOGIC HAPPENS HERE
        self.__screen.fill(self.__background_colour)
        for bar in self.__bars:
            bar.draw()
            
        pygame.display.update()

    def create_bars(self, amount):
        for i in range(0, amount):
            self.__bars.append(Bar(self.__screen, i, self.__screen_size[0]*((i)/(amount)), self.__screen_size[1]*((amount-(i+1))/amount), self.__screen_size[0]/amount, (255*((amount-i)/amount), 255*(i/amount), 0)))
        return self.__bars

    def randomise_bar_position(self):
        for i in range(1000):
            for bar in self.__bars:
                temp_bar1 = random.choice(self.__bars)
                temp_x1 = temp_bar1.get_x()
                temp_bar2 = random.choice(self.__bars)
                temp_bar1.set_x(temp_bar2.get_x())
                temp_bar2.set_x(temp_x1)

    def bubble_sort(self):
        swap_made = False
        limiter_index = len(self.__bars) - 1
        while True:
            for i in range(0, len(self.__bars)-1):
                if limiter_index <= 0:
                    return True
                if i < limiter_index:
                    # change colour temporarily while shapes are swapped or checked
                    temp_col1 = self.__bars[i].get_colour()
                    temp_col2 = self.__bars[i+1].get_colour()
                    self.__bars[i].set_colour((255, 255, 255))
                    self.__bars[i+1].set_colour((255, 255, 255))
                    self.draw_screen()
                    #time.sleep(0.3)

                    if self.__bars[i].get_id() > self.__bars[i+1].get_id():
                        # changing positions
                        temp_x = self.__bars[i].get_x()
                        self.__bars[i].set_x(self.__bars[i+1].get_x())
                        self.__bars[i+1].set_x(temp_x)

                        # rearrange the order of bars in the __bars list, in order to match the visual list
                        self.__bars = self.rearrange_bars_list()

                        self.draw_screen()
                        #time.sleep(0.3)
                        swap_made = True

                    # returning the colour of the bars
                    if swap_made == True:
                        self.__bars[i+1].set_colour(temp_col1)
                        self.__bars[i].set_colour(temp_col2)
                    else:
                        self.__bars[i].set_colour(temp_col1)
                        self.__bars[i+1].set_colour(temp_col2)
                    swap_made = False
            limiter_index -= 1
        return True

    def rearrange_bars_list(self):
        new_list = []
        lowest = self.__screen_size[0]
        # every iteration, check for lowest x:
        # add the bar with lowest x to new_list and remove from old list
        # repeat until all bars added
        # set old list to be new list
        while len(self.__bars) > 0:
            for bar in self.__bars:
                if bar.get_x() < lowest:
                    lowest = bar.get_x()
            for bar in self.__bars:
                if bar.get_x() == lowest:
                    new_list.append(bar)
                    self.__bars.remove(bar)
            lowest = self.__screen_size[0]

        return new_list

class Bar:
    def __init__(self, screen, id, x, y, width, colour):
        self.__id = id
        self.__x = x
        self.__y = y
        self.__width = width
        self.__colour = colour
        self.__height = screen.get_height()
        self.__screen = screen

    def get_id(self):
        return self.__id

    def get_colour(self):
        return self.__colour

    def set_colour(self, new_colour):
        self.__colour = new_colour

    def get_x(self):
        return self.__x

    def set_x(self, new_x):
        self.__x = new_x

    def draw(self):
        pygame.draw.rect(self.__screen, self.__colour, (self.__x, self.__y, self.__width, self.__height))

if __name__ == "__main__":
    # Program(size(array or tuple), font_size(int), background_colour(array or tuple))
    program = Program((1280, 780), 30, (20, 20, 20))
    program.run()