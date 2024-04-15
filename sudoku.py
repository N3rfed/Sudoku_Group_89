import pygame
import sys


def draw_game_start(screen):
    start_title_font = pygame.font.Font(None,100)
    button_font = pygame.font.Font(None, 70)

    screen.fill(255,255,255)

    title_surface = start_title_font.render("Sudoku", 0 , (255,255,255))
    title_rectangle = title_surface.get_rect(center=(800 // 2, 800 // 2 - 150))
    screen.blit(title_surface, title_rectangle)

    easy_text = button_font.render("Easy", 0, (255,255,255))
    medium_text = button_font.render("Medium", 0, (255,255,255))
    hard_text = button_font.render("Hard", 0, (255,255,255))

    easy_surface = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size[1] +20))
    easy_surface.fill(LINE_COLOR)
    easy_surface.blit(easy_text,(10,10))
    medium_surface = pygame.Surface(((medium_text.get_size()[0] +20, medium_text.get_size()[1] +20))
    medium_surface.fill(LINE_COLOR)
    medium_surface.blit(medium_text, (10, 10))
    hard_surface = pygame.Surface(((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
    hard_surface.fill(LINE_COLOR)
    hard_surface.blit(medium_text, (10, 10))