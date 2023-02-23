def printGrid(grid):
    print('', grid.get("1"), '|', grid.get("2"), '|', grid.get("3"))
    print('---+---+---')
    print('', grid.get("4"), '|', grid.get("5"), '|', grid.get("6"))
    print('---+---+---')
    print('', grid.get("7"), '|', grid.get("8"), '|', grid.get("9"))

    validinp = False
    while validinp == False:
        try:
            userinp = int(input('\nPlayer ' + (str(player)) + ' enter a value from 1-9\n\t>'))
        except ValueError:
            validinp = False
            print("value entered was not a number - try again")
        else:
            if userinp > 0 and userinp < 10:
                validinp = True
            else:
                print('value out of bounds - try again')

        '''
         for event in pygame.event.get():
             if event.type == pygame.KEYDOWN:
                 print('TEST - KEYDOWN')
                 if event.unicode:
                     print('TEST - change module')
                     self.main.changeModule(self.main.grid, self.game.KEY_INPUT)
                     # print(self.main.grid)
                     self.game.reset_key_input()
                     self.output_grid()
                     self.switch_player()


         for event in pygame.event.get():
             print('TEST - EVENT')
             if event.type == pygame.KEYDOWN:
                 if event.unicode:
                     print('TEST - KEYDOWN')
                     try:
                         if 0 < int(self.game.KEY_INPUT) < 10:
                             print('TEST - number input', self.game.KEY_INPUT)
                             # self.check_input()  # takes input and puts on grid (supposed to)
                             validCheck(self.main.grid, self.game.KEY_INPUT)
                             changeModule(self.main.grid, self.game.Key_INPUT)
                             self.blit_screen()  # also resets keys

                             self.switch_player()
                             self.output_grid()
                     except:
                         print('not a number')
         '''

    '''
    def check_input(self):
        print('TEST - check input')
        input = str(self.game.KEY_INPUT)
        self.game.check_events()
        if self.game.START_KEY == True:
            if self.main.player == 1:
                grid.update({input: 'x'})
            else:
                grid.update({input: 'o'})
    '''


'''
        while not self.main.checkWin(grid)  and not self.main.boardFull(grid):
            for i in range(4):
                if player == 1:
                    player = 2
                else:
                    player = 1
                print('USER INPUT')
'''

'''
 # NUMBERS
 if event.key == pygame.K_1:
     self.ONE_KEY = True
 if event.key == pygame.K_2:
     self.TWO_KEY = True
 if event.key == pygame.K_3:
     self.THREE_KEY = True
 if event.key == pygame.K_4:
     self.FOUR_KEY = True
 if event.key == pygame.K_5:
     self.FIVE_KEY = True
 if event.key == pygame.K_6:
     self.SIX_KEY = True
 if event.key == pygame.K_7:
     self.SEVEN_KEY = True
 if event.key == pygame.K_8:
     self.EIGHT_KEY = True
 if event.key == pygame.K_9:
     self.NINE_KEY = True
 '''
'''

while checkWin(grid) == False and boardFull(grid) == False:
    if player == 1:
        player = 2
    else:
        player = 1

    # validate input

    # changeModule(grid, userinp)

# game over
print()
# printGrid(grid)
if boardFull(grid) == True:
    print('\n\nits a tie!\n\n')
else:
    print('\n\nplayer', str(player), 'wins!\n\n')
'''


# -----------------------------------------------------------------------------------------------------------
#                                             OPTIONS
# -----------------------------------------------------------------------------------------------------------

class OptionsMenu(Menu):
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
            self.game.draw_text_subtitle('Light mode/ Dark mode', self.option1x, self.option1y)
            self.game.draw_text_subtitle('Change symbols', self.option2x, self.option2y)

            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            # print('TEST - ENTER KEY')
            if self.state == 'a':
                self.game.curr_menu = self.game.appearance
            else:  # b - symbols
                self.game.curr_menu = self.game.symbols
            self.run_display = False

    def move_cursor(self):
        if self.game.DOWN_KEY or self.game.UP_KEY:
            # print('TEST - up or down key')
            if self.state == 'a':
                self.cursor_rect.midtop = (self.option2x + self.offset, self.option2y)
                self.state = 'b'
            else:
                self.cursor_rect.midtop = (self.option1x + self.offset, self.option1y)
                self.state = 'a'

# -----------------------------------------------------------------------------------------------------------
#                                             SYMBOLS
# -----------------------------------------------------------------------------------------------------------

class Symbols(Menu):
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
            self.game.draw_text_title('Symbols', self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 175)
            self.game.draw_text_subtitle('Light mode/ Dark mode', self.option1x, self.option1y)
            self.game.draw_text_subtitle('Change symbols', self.option2x, self.option2y)

            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'a':
                self.game.curr_menu = self.game.appearance
            else:  # b - symbols
                self.game.curr_menu = self.game.symbols
            self.run_display = False

    def move_cursor(self):
        if self.game.DOWN_KEY or self.game.UP_KEY:
            if self.state == 'a':
                self.cursor_rect.midtop = (self.option2x + self.offset, self.option2y)
                self.state = 'b'
            else:
                self.cursor_rect.midtop = (self.option1x + self.offset, self.option1y)
                self.state = 'a'

