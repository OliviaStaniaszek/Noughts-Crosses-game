import pygame
import GUI
import main
from main import *
from pygame.locals import *

# -----------------------------------------------------------------------------------------------------------
#                                             MENU CLASS
# -----------------------------------------------------------------------------------------------------------

class Menu:
    def __init__(self, game):
        self.game = game  # allows you to use variables from game
        self.main = main
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = -150

    def draw_cursor(self):
        self.game.draw_text_reg('>', self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()
        self.game.reset_key_input()


# -----------------------------------------------------------------------------------------------------------
#                                             GAME CLASS
# -----------------------------------------------------------------------------------------------------------

class GameScreen:
    def __init__(self, game):
        self.game = game
        self.main = main
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.clock = pygame.time.Clock()

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        pygame.display.flip()
        self.game.reset_keys()

    def output_grid(self):
        # print('TEST - output grid start')
        first = 106.7
        middle = 320
        last = 533.3
        # self.game.draw_text_reg(self.game.KEY_INPUT, last, first - 85)
        if self.main.player == 1:
            playersymb = 'X'
        else:
            playersymb = 'O'
        self.game.draw_text_reg(playersymb, last + 80, first - 85)

        if self.main.grid.get('1') == 'X':
            self.game.draw_XO1(self.main.grid.get("1"), first, first)
        else:
            self.game.draw_XO2(self.main.grid.get("1"), first, first)
        if self.main.grid.get('2') == 'X':
            self.game.draw_XO1(self.main.grid.get("2"), middle, first)
        else:
            self.game.draw_XO2(self.main.grid.get("2"), middle, first)
        if self.main.grid.get('3') == 'X':
            self.game.draw_XO1(self.main.grid.get("3"), last, first)
        else:
            self.game.draw_XO2(self.main.grid.get("3"), last, first)
        if self.main.grid.get('4') == 'X':
            self.game.draw_XO1(self.main.grid.get("4"), first, middle)
        else:
            self.game.draw_XO2(self.main.grid.get("4"), first, middle)
        if self.main.grid.get('5') == 'X':
            self.game.draw_XO1(self.main.grid.get("5"), middle, middle)
        else:
            self.game.draw_XO2(self.main.grid.get("5"), middle, middle)
        if self.main.grid.get('6') == 'X':
            self.game.draw_XO1(self.main.grid.get("6"), last, middle)
        else:
            self.game.draw_XO2(self.main.grid.get("6"), last, middle)
        if self.main.grid.get('7') == 'X':
            self.game.draw_XO1(self.main.grid.get("7"), first, last)
        else:
            self.game.draw_XO2(self.main.grid.get("7"), first, last)
        if self.main.grid.get('8') == 'X':
            self.game.draw_XO1(self.main.grid.get("8"), middle, last)
        else:
            self.game.draw_XO2(self.main.grid.get("8"), middle, last)
        if self.main.grid.get('9') == 'X':
            self.game.draw_XO1(self.main.grid.get("9"), last, last)
        else:
            self.game.draw_XO2(self.main.grid.get("9"), last, last)


'''
    def draw_line(self):
        # pygame.draw.line(surface, color, start_pos, end_pos, width)
        self.game.draw_grid_line(0, 0, 640, 640)
        # pygame.draw.line(GUI.SCREEN, linecolour, [0, 0], [640, 640], 10)
'''


class StartGame(GameScreen):
    def __init__(self, game):
        GameScreen.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:

            self.game.check_events()  # checks for key input
            self.game.display.fill(self.game.bkgcolour)
            self.game.display.blit(self.game.bkgimg, (0, 0))
            self.output_grid()

            if self.game.KEY_INPUT != ' ' or self.game.lclick == True:
                if self.game.lclick == True:
                    self.mx, self.my = pygame.mouse.get_pos()
                    print(self.mx, self.my)
                    self.game.KEY_INPUT = self.game.moduleAtMousePos(self.mx, self.my)

                isvalid = self.main.validCheck(self.main.grid, self.game.KEY_INPUT)
                if isvalid:
                    self.main.changeModule(self.main.grid, self.game.KEY_INPUT)
                    # print('TEST - CHANGE MODULE')
                    # if self.game.START_KEY:
                    self.game.win = self.main.checkWin(self.main.grid)
                    if self.game.win:
                        # print('\tWIN')
                        self.game.win = True
                        self.switch_player()
                        self.game.winner = self.main.player

                        # if self.game.START_KEY:
                        # print('TEST - to end screen')
                        self.game.curr_menu = self.game.endscreen
                        self.run_display = False
                    else:  # not a win
                        self.game.isboardfull = self.main.boardFull(self.main.grid)
                        if self.game.isboardfull:
                            # print('\tboard full')
                            self.game.curr_menu = self.game.endscreen
                            self.run_display = False

                    # if not a win and board not full
                    self.switch_player()
                    # print('TEST - player', self.main.player)
                    # self.game.reset_keys()
                # print(self.main.grid)
                self.game.reset_key_input()
                self.output_grid()

            # self.draw_line()
            self.blit_screen()  # also resets keys
            self.clock.tick(10)

    def switch_player(self):
        # print('TEST - switching player', self.main.player)
        if self.main.player == 1:
            self.main.player = 2
        else:
            self.main.player = 1


# -----------------------------------------------------------------------------------------------------------
#                                             MAIN MENU
# -----------------------------------------------------------------------------------------------------------

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'a'
        self.option1x, self.option1y = self.mid_w, self.mid_h - 45
        self.option2x, self.option2y = self.mid_w, self.mid_h + 40
        self.option3x, self.option3y = self.mid_w, self.mid_h + 135
        self.cursor_rect.midtop = (self.option1x + self.offset, self.option1y)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.bkgcolour)
            self.game.draw_text_title('Noughts and Crosses', self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 175)
            self.game.draw_text_subtitle('Start Game', self.option1x, self.option1y)
            self.game.draw_text_subtitle('How to Play', self.option2x, self.option2y)
            self.game.draw_text_subtitle('Options', self.option3x, self.option3y)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            # print('TEST - DOWN')
            if self.state == 'a':
                self.cursor_rect.midtop = (self.option2x + self.offset, self.option2y)
                self.state = 'b'
            elif self.state == 'b':
                self.cursor_rect.midtop = (self.option3x + self.offset, self.option3y)
                self.state = 'c'
            elif self.state == 'c':
                self.cursor_rect.midtop = (self.option1x + self.offset, self.option1y)
                self.state = 'a'
        elif self.game.UP_KEY:
            if self.state == 'a':
                self.cursor_rect.midtop = (self.option3x + self.offset, self.option3y)
                self.state = 'c'
            elif self.state == 'b':
                self.cursor_rect.midtop = (self.option1x + self.offset, self.option1y)
                self.state = 'a'
            elif self.state == 'c':
                self.cursor_rect.midtop = (self.option2x + self.offset, self.option2y)
                self.state = 'b'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'a':
                self.game.curr_menu = self.game.startgame
            elif self.state == 'b':
                self.game.curr_menu = self.game.howtoplay
            elif self.state == 'c':
                self.game.curr_menu = self.game.appearance
            self.run_display = False


# -----------------------------------------------------------------------------------------------------------
#                                             OPTIONS/ APPEARANCE
# -----------------------------------------------------------------------------------------------------------

class Appearance(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'a'  # appearance
        self.option1x, self.option1y = self.mid_w, self.mid_h - 45
        self.option2x, self.option2y = self.mid_w, self.mid_h + 40
        self.cursor_rect.midtop = (self.option1x + self.offset, self.option1y)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            if self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.bkgcolour)
            self.game.draw_text_title('Options', self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 175)
            self.game.draw_text_subtitle('Light mode', self.option1x, self.option1y)
            self.game.draw_text_subtitle('Dark mode', self.option2x, self.option2y)
            self.game.draw_text_reg('Made by Olivia - August 2021', self.game.DISPLAY_W / 2, self.game.DISPLAY_H - 40)

            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'a':
                self.game.change_appearance(True)
            else:
                self.game.change_appearance(False)
            self.run_display = False

    def move_cursor(self):
        if self.game.DOWN_KEY or self.game.UP_KEY:
            if self.state == 'a':
                self.cursor_rect.midtop = (self.option2x + self.offset, self.option2y)
                self.state = 'b'
            else:
                self.cursor_rect.midtop = (self.option1x + self.offset, self.option1y)
                self.state = 'a'


# -----------------------------------------------------------------------------------------------------------
#                                             HOW TO PLAY
# -----------------------------------------------------------------------------------------------------------

class HowtoPlay(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.bkgcolour)

            topline = 230
            spacing = 35
            self.game.draw_text_title('How to Play', self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 175)
            self.game.draw_text_reg("Take turns placing your pieces ", self.game.DISPLAY_W / 2, topline)
            self.game.draw_text_reg("until someone gets a 3 in a row", self.game.DISPLAY_W / 2, topline + spacing)
            self.game.draw_text_reg("or the board is full - meaning its", self.game.DISPLAY_W / 2, topline + (spacing * 2))
            self.game.draw_text_reg("a tie.", self.game.DISPLAY_W / 2, topline + (spacing * 3))
            self.game.draw_text_reg("Use numbers 1-9 corresponding", self.game.DISPLAY_W / 2,
                                    topline + (spacing * 4))
            self.game.draw_text_reg("to each grid square (reading left", self.game.DISPLAY_W / 2, topline + (spacing * 5))
            self.game.draw_text_reg("to right), or click the squares", self.game.DISPLAY_W / 2, topline + (spacing * 6))
            self.game.draw_text_reg("with a mouse", self.game.DISPLAY_W / 2, topline + (spacing * 7))

            self.blit_screen()


# -----------------------------------------------------------------------------------------------------------
#                                             END SCREEN
# -----------------------------------------------------------------------------------------------------------

class EndScreen(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY:
                # reset grid and player
                self.main.grid = {
                    "1": " ",
                    "2": " ",
                    "3": " ",
                    "4": " ",
                    "5": " ",
                    "6": " ",
                    "7": " ",
                    "8": " ",
                    "9": " ",
                }
                self.main.player = 1

                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.bkgcolour)

            message = 'blank message'
            # print('test win?', self.game.win)
            if self.game.win == True:
                if self.main.player == 1:
                    message = 'X wins!'
                else:
                    message = 'O wins!'
                # print('TEST - message', message)
            elif self.game.isboardfull:
                message = "It's a tie!"

            topline = 230
            spacing = 35
            # print(message)
            self.game.draw_text_title('Game Over', self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 175)
            self.game.draw_text_subtitle(message, self.game.DISPLAY_W / 2, topline)
            self.game.draw_text_reg("Press enter to go back ", self.game.DISPLAY_W / 2,
                                    topline + spacing + 40)
            self.game.draw_text_reg("to the menu", self.game.DISPLAY_W / 2,
                                    topline + spacing + 80)

            self.blit_screen()

    def check_input(self):
        if self.game.START_KEY:
            self.game.curr_menu = self.game.main_menu
        self.run_display = False
