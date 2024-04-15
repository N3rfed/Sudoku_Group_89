import pygame
import sys
LINE_COLOR = (30, 227, 49)
WIDTH = 800
HEIGHT = 600

def draw_game_start(screen):
    start_title_font = pygame.font.Font(None,100)
    button_font = pygame.font.Font(None, 70)

    screen.fill((255,255,255))

    title_surface = start_title_font.render("Sudoku", 0 , (255,255,255))
    title_rectangle = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 150))
    screen.blit(title_surface, title_rectangle)

    easy_text = button_font.render("Easy", 0, (255,255,255))
    medium_text = button_font.render("Medium", 0, (255,255,255))
    hard_text = button_font.render("Hard", 0, (255,255,255))

    easy_surface = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] +20))
    easy_surface.fill(LINE_COLOR)
    easy_surface.blit(easy_text,(10,10))
    medium_surface = pygame.Surface((medium_text.get_size()[0] +20, medium_text.get_size()[1] +20))
    medium_surface.fill(LINE_COLOR)
    medium_surface.blit(medium_text, (10, 10))
    hard_surface = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
    hard_surface.fill(LINE_COLOR)
    hard_surface.blit(medium_text, (10, 10))

    easy_rectangle = easy_surface.get_rect(center =(WIDTH//2, HEIGHT//2 + 50))
    medium_rectangle = medium_surface.get_rect(center =(WIDTH//2, HEIGHT//2 + 150))
    hard_rectangle = hard_surface.get_rect(center=(WIDTH//2, HEIGHT//2 + 200))

    screen.blit(easy_surface,easy_rectangle)
    screen.blit(medium_surface,medium_rectangle)
    screen.blit(hard_surface, hard_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rectangle.collidepoint(event.pos):
                    pass #unfinished
        pygame.display.update()


if __name__ == "__main__":
    game_over = False
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")

    draw_game_start(screen)