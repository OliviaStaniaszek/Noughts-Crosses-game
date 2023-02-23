from menu import *
import GUI
from main import *
from pygame.locals import *


# -----------------------------------------------------------------------------------------------------------
#                                             GAME CLASS
# -----------------------------------------------------------------------------------------------------------

class Game:
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY, self.DELETE_KEY, self.KEY_INPUT = [False, False,
                                                                                                      False, False,
                                                                                                      False, '']
        [self.ONE_KEY, self.TWO_KEY, self.THREE_KEY, self.FOUR_KEY, self.FIVE_KEY, self.SIX_KEY, self.SEVEN_KEY,
         self.EIGHT_KEY, self.NINE_KEY] = False, False, False, False, False, False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = GUI.SCREENWIDTH, GUI.SCREENHEIGHT
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))  # pass as tuple
        self.window = pygame.display.set_mode((self.DISPLAY_W, self.DISPLAY_H))
        # colours
        self.darkmode = True
        self.p1colour = GUI.FUZZY
        self.p2colour = GUI.TAN
        self.bkgcolour = GUI.PRUSSIAN
        self.textcolour = GUI.MAGENTA
        self.bkgimg = GUI.DARKBKG

        self.win = main.win
        self.isboardfull = False
        # mouse
        # self.offset = [0,0]
        self.lclick = False
        self.mx, self.my = pygame.mouse.get_pos()

        if player == 1:
            self.winner = 'X'
        else:
            self.winner = 'O'

        pygame.display.set_caption('Noughts and Crosses')

        self.main_menu = MainMenu(self)

        self.startgame = StartGame(self)

        self.howtoplay = HowtoPlay(self)

        # self.options = OptionsMenu(self)

        self.appearance = Appearance(self)  # now called options
        # self.symbols = Symbols(self)

        self.endscreen = EndScreen(self)

        self.curr_menu = self.main_menu

    def game_loop(self):
        # print('TEST - GAME LOOP')
        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing = True
            self.display.fill(self.bkgcolour)
            self.window.blit(self.display, (0, 0))  # align screen with display
            # pygame.display.update()  # moves image onto screen
            self.reset_keys()
            self.reset_key_input()
            self.mx, self.my = pygame.mouse.get_pos()
            # self.loc = [self.mx, self.my]

    def check_events(self):
        # print('TEST - CHECK EVENTS')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                # print('TEST - EVENT GET')
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
                if event.key == pygame.K_DELETE:
                    self.DELETE_KEY = True

                if event.unicode:
                    self.KEY_INPUT = event.unicode

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.lclick = True
                    print('TEST - mouse click')

            # print('\tTEST ',self.KEY_INPUT)

    def reset_keys(self):
        # print('TEST - RESET KEYS')
        [self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY, self.DELETE_KEY] = False, False, False, False, False
        [self.ONE_KEY, self.TWO_KEY, self.THREE_KEY, self.FOUR_KEY, self.FIVE_KEY, self.SIX_KEY, self.SEVEN_KEY,
         self.EIGHT_KEY, self.NINE_KEY] = False, False, False, False, False, False, False, False, False,
        self.lclick = False

    def reset_key_input(self):
        self.KEY_INPUT = ''

    def draw_text_title(self, text, x, y):
        text_surface = GUI.TITLEF.render(text, True, self.textcolour)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)

    def draw_text_subtitle(self, text, x, y):
        text_surface = GUI.SUBF.render(text, True, self.textcolour)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)

    def draw_text_reg(self, text, x, y):
        text_surface = GUI.TEXTF.render(text, True, self.textcolour)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)

    def draw_XO1(self, text, x, y):
        text_surface = GUI.XO.render(text, True, self.p1colour)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)

    def draw_XO2(self, text, x, y):
        text_surface = GUI.XO.render(text, True, self.p2colour)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)

    def change_appearance(self, darkmode):
        if darkmode:  # if currently dark mode - go light mode
            self.p1colour = GUI.ARTICHOKE
            self.p2colour = GUI.EBONY
            self.bkgcolour = GUI.CHAMPAGNE
            self.textcolour = GUI.BRASS
            self.bkgimg = GUI.LIGHTBKG
        else:
            self.p1colour = GUI.FUZZY
            self.p2colour = GUI.TAN
            self.bkgcolour = GUI.PRUSSIAN
            self.textcolour = GUI.MAGENTA
            self.bkgimg = GUI.DARKBKG

    def moduleAtMousePos(self, mx, my):
        module = 0
        if 0 < mx < 213 and 0 < my < 213:
            print('TEST - module 1')
            module = 1
        elif 213 < mx < 426.7 and 0 < my < 213:
            print('TEST - module 2')
            module = 2
        elif 426.7 < mx < 640 and 0 < my < 213:
            print('TEST - module 3')
            module = 3
        elif 0 < mx < 213 and 213 < my < 426.7:
            print('TEST - module 4')
            module = 4
        elif 213 < mx < 426.7 and 213 < my < 426.7:
            print('TEST - module 5')
            module = 5
        elif 426.7 < mx < 640 and 213 < my < 426.7:
            print('TEST - module 6')
            module = 6
        elif 0 < mx < 231 and 426.7 < my < 640:
            print('TEST - module 7')
            module = 7
        elif 213 < mx < 426.7 and 426.7 < my < 640:
            print('TEST - module 8')
            module = 8
        elif 426.7 < mx < 640 and 426.7 < my < 640:
            print('TEST - module 9')
            module = 9

        else:
            print('TEST - not module ')
        return module


'''
    def draw_grid_line(self, startx, starty, endx, endy):
        line = pygame.draw.line(GUI.SCREEN, linecolour, [startx, starty], [endx, endy], 10)
        pygame.display.flip()
'''

# -----------------------------------------------------------------------------------------------------------
#                                             CODE STARTS
# -----------------------------------------------------------------------------------------------------------

g = Game()
while g.running:
    g.curr_menu.display_menu()
    g.game_loop()
