import pygame
import random

from dino_runner.utils.constants import CLOUD,BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, RUNNING
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacles_manager import ObstacleManager
from dino_runner.components import text_utils
from dino_runner.components.power_up.power_up_manager import PowerUpManager


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.cloud_x = SCREEN_WIDTH
        self.cloud_y = 140
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.points = 0
        self.running = True
        self.death_count = 0

    def run(self):
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups(self.points)
        self.game_speed = 20
        self.points = 0
        self.player.hammer = 0
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def execute(self):
        while self.running:
            if not self.playing:
                self.show_menu()

    def show_menu(self):
        self.running = True
        white_color = (255, 255, 255)
        self.screen.fill(white_color)
        
        self.print_menu_elements()
        pygame.display.update()
        self.handle_key_events_on_menu()
        
    def print_menu_elements(self):
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2
        
        if self.death_count == 0:
            text, text_rect = text_utils.get_centered_message("Press any key to Start")
            self.screen.blit(text, text_rect)
        elif self.death_count > 0:
            text,text_rect = text_utils.get_centered_message("Press any key to Restart")
            score, score_rect = text_utils.get_centered_message("Your score: " + str(self.points),
                                                                height = half_screen_height + 50)
            death, death_rect = text_utils.get_centered_message("Death count: " + str(self.death_count),
                                                                height= half_screen_height + 100)
            self.screen.blit(score, score_rect)
            self.screen.blit(text, text_rect)
            self.screen.blit(death, death_rect)
        
        self.screen.blit(RUNNING[0], (half_screen_width - 20, half_screen_height - 140))

    def handle_key_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
                pygame.display.quit()
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                self.run()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
        self.screen.fill((255, 255, 255))

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input, self.game_speed)
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self.points, self.game_speed, self.player)

    def draw(self):
        self.score()
        self.clock.tick(FPS)
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        self.screen.blit(CLOUD, (self.cloud_x, self.cloud_y))
        if self.cloud_x < 0:   
            self.cloud_x = SCREEN_WIDTH
            self.cloud_y = random.randint(30,200)
        self.cloud_x -= self.game_speed    
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
        

    def score(self):
        self.points += 1
        if self.points % 100 == 0:
            self.game_speed += 1
        text, text_rect = text_utils.get_score_element(str(self.points))
        self.player.chek_invincibility(self.screen)
        self.player.check_hammer(self.screen)
        self.screen.blit(text, text_rect)