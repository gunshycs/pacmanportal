import pygame
from pygame.sprite import Sprite

class BluePortal(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()
        # self.scoreboard = game.scoreboard
        self.level = game.board.level
        self.image = pygame.image.load('images/portals/blue.png')
        scaling_factor = 0.7  # 10% reduction
        new_width = int(self.image.get_width() * scaling_factor)
        new_height = int(self.image.get_height() * scaling_factor)
        self.image = pygame.transform.scale(self.image, (new_width, new_height))
        self.rect = self.image.get_rect()
        self.spawned = False  # Flag to check if the portal has been spawned
        self.portal_x = 0
        self.portal_y = 0

    def draw(self):
        if self.spawned:
            #print(f"Drawing at {self.portal_x}, {self.portal_y}")
            self.rect.topleft = (self.portal_x, self.portal_y)
            self.screen.blit(self.image, self.rect)

    def spawnportal(self, pacman_x, pacman_y, pacman_direction):
        print('spawnnign\n')
        if self.spawned:
            # Delete the existing portal
            self.deleteportal()

        # Create a new portal
        self.portal_x = pacman_x + self.rect.width // 3 + 2  # Adjusted for the width of the portal image
        self.portal_y = pacman_y + 5
        self.pacman_direction = pacman_direction
        self.spawned = True

    def deleteportal(self):
        self.spawned = False

    def updateportal(self):
        if self.spawned:
            if self.pacman_direction == 0:  # Up
                if self.check_movement_valid(2):
                    self.portal_x += 10
            elif self.pacman_direction == 1:  # Down
                if self.check_movement_valid(3):
                    self.portal_x -= 10
            elif self.pacman_direction == 2:  # Right
                if self.check_movement_valid(0):
                    self.portal_y -= 10
            elif self.pacman_direction == 3:  # Left
                if self.check_movement_valid(1):
                    self.portal_y += 10

    def is_moving(self):
        prev_x, prev_y = self.portal_x, self.portal_y
        self.updateportal()
        return (prev_x, prev_y) != (self.portal_x, self.portal_y)

    def checkcollisions(self):
        if self.spawned:
            if not self.check_movement_valid(self.pacman_direction):
                #print("Blue portal has hit a wall")
                return False
            return True

    def check_movement_valid(self, direction):
        pieceheight = ((self.settings.screen_height - 50) // 32)
        piecewidth = (self.settings.screen_width // 30)
        next_x = self.portal_x
        next_y = self.portal_y

        if direction == 0:  # Up
            # print(f"{direction}")
            next_x += 10
            if self.level[next_y // pieceheight][next_x // piecewidth] >= 3:
                return False
        elif direction == 1:  # Down
            next_x += 10
            next_y += round(self.rect.height * 0.7)
            if (
                next_x >= self.settings.screen_width
                or self.level[next_y // pieceheight][next_x // piecewidth] in (4, 7, 8)
            ):
                return False
        elif direction == 2:  # Right
            next_y += 10
            next_x += round(self.rect.width * 0.7)
            if (
                next_y >= self.settings.screen_height - 50
                or self.level[next_y // pieceheight][next_x // piecewidth] == 3
            ):
                return False
        elif direction == 3:  # Left
            # print(f"{direction}")
            next_y += 10
            if self.level[next_y // pieceheight][next_x // piecewidth] >= 3:
                return False

        return True











class OrangePortal(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()
        # self.scoreboard = game.scoreboard
        self.level = game.board.level
        self.image = pygame.image.load('images/portals/orange.png')
        scaling_factor = 0.7  # 10% reduction
        new_width = int(self.image.get_width() * scaling_factor)
        new_height = int(self.image.get_height() * scaling_factor)
        self.image = pygame.transform.scale(self.image, (new_width, new_height))
        self.rect = self.image.get_rect()
        self.spawned = False  # Flag to check if the portal has been spawned
        self.portal_x = 0
        self.portal_y = 0

    def draw(self):
        if self.spawned:
            #print(f"Drawing at {self.portal_x}, {self.portal_y}")
            self.rect.topleft = (self.portal_x, self.portal_y)
            self.screen.blit(self.image, self.rect)

    def spawnportal(self, pacman_x, pacman_y, pacman_direction):
        print('spawnnign\n')
        if self.spawned:
            # Delete the existing portal
            self.deleteportal()

        # Create a new portal
        self.portal_x = pacman_x + self.rect.width // 3 + 2  # Adjusted for the width of the portal image
        self.portal_y = pacman_y + 5
        self.pacman_direction = pacman_direction
        self.spawned = True

    def deleteportal(self):
        self.spawned = False

    def updateportal(self):
        if self.spawned:
            if self.pacman_direction == 0:  # Up
                if self.check_movement_valid(2):
                    self.portal_x += 10
            elif self.pacman_direction == 1:  # Down
                if self.check_movement_valid(3):
                    self.portal_x -= 10
            elif self.pacman_direction == 2:  # Right
                if self.check_movement_valid(0):
                    self.portal_y -= 10
            elif self.pacman_direction == 3:  # Left
                if self.check_movement_valid(1):
                    self.portal_y += 10

    def is_moving(self):
        prev_x, prev_y = self.portal_x, self.portal_y
        self.updateportal()
        return (prev_x, prev_y) != (self.portal_x, self.portal_y)

    def checkcollisions(self):
        if self.spawned:
            if not self.check_movement_valid(self.pacman_direction):
                #print("Orange portal has hit a wall")
                return False
            return True

    def check_movement_valid(self, direction):
        pieceheight = ((self.settings.screen_height - 50) // 32)
        piecewidth = (self.settings.screen_width // 30)
        next_x = self.portal_x
        next_y = self.portal_y

        if direction == 0:  # Up
            #print(f"{direction}")
            next_x += 10
            if self.level[next_y // pieceheight][next_x // piecewidth] >= 3:
                return False
        elif direction == 1:  # Down
            next_x += 10
            next_y += round(self.rect.height * 0.7)
            if (
                next_x >= self.settings.screen_width
                or self.level[next_y // pieceheight][next_x // piecewidth] in (4, 7, 8)
            ):
                return False
        elif direction == 2:  # Right
            next_y += 10
            next_x += round(self.rect.width * 0.7)
            if (
                next_y >= self.settings.screen_height - 50
                or self.level[next_y // pieceheight][next_x // piecewidth] == 3
            ):
                return False
        elif direction == 3:  # Left
            #print(f"{direction}")
            next_y += 10
            if self.level[next_y // pieceheight][next_x // piecewidth] >= 3:
                return False

        return True