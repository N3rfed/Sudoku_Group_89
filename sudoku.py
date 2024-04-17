import pygame
import sys

LINE_COLOR = (30, 227, 49)
WIDTH = 800
HEIGHT = 800


def draw_game_start(screen):
    start_title_font = pygame.font.Font(None, 100)
    button_font = pygame.font.Font(None, 70)

    screen.fill((255, 255, 255))

    title_surface = start_title_font.render("Sudoku", 0, (LINE_COLOR))
    title_rectangle = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 150))
    screen.blit(title_surface, title_rectangle)

    easy_text = button_font.render("Easy", 0, (255, 255, 255))
    medium_text = button_font.render("Medium", 0, (255, 255, 255))
    hard_text = button_font.render("Hard", 0, (255, 255, 255))

    easy_surface = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))
    easy_surface.fill(LINE_COLOR)
    easy_surface.blit(easy_text, (10, 10))
    medium_surface = pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))
    medium_surface.fill(LINE_COLOR)
    medium_surface.blit(medium_text, (10, 10))
    hard_surface = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
    hard_surface.fill(LINE_COLOR)
    hard_surface.blit(hard_text, (10, 10))

    easy_rectangle = easy_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    medium_rectangle = medium_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 150))
    hard_rectangle = hard_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 250))

    screen.blit(easy_surface, easy_rectangle)
    screen.blit(medium_surface, medium_rectangle)
    screen.blit(hard_surface, hard_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rectangle.collidepoint(event.pos):
                    return
                if medium_rectangle.collidepoint(event.pos):
                    return
                if hard_rectangle.collidepoint(event.pos):
                    return
        pygame.display.update()


def draw_game_over(winner):
    game_over_font = pygame.font.Font(None, 150)
    button_font = pygame.font.Font(None, 70)
    screen.fill((255, 255, 255))
    if winner == True:
        text = f"Game Won!"
        button_text = button_font.render(f"Exit", 0, (255, 255, 255))
    else:
        text = f"Game Over :("
        button_text = button_font.render(f"Restart", 0, (255, 255, 255))
    game_over_surface = game_over_font.render(text, 0, LINE_COLOR)
    game_over_rectangle = game_over_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 150))
    screen.blit(game_over_surface, game_over_rectangle)

    button_surface = pygame.Surface((button_text.get_size()[0] + 20, button_text.get_size()[1] + 20))
    button_surface.fill(LINE_COLOR)
    button_surface.blit(button_text, (10, 10))
    button_rectangle = button_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    screen.blit(button_surface, button_rectangle)

    while True:  # quit doesn't do anything yet
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rectangle.collidepoint(event.pos):
                    return
        pygame.display.update()


def draw_grid():
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 0), pygame.rect(15, 15, 720, 720), 10)
    i = 1
    while (i * 80) < 720:
        line_width = 5 if i % 3 > 0 else 10
        pygame.draw.rect(screen, pygame.Color("black"), pygame.Vector2((i * 80) + 15, 15),
                         pygame.Vector2((i * 80) + 15, 735), line_width)
        pygame.draw.rect(screen, pygame.Color("black"), pygame.Vector2(15, (i * 80) + 15),
                         pygame.Vector2(735, (i * 80) + 15), line_width)
        i += 1


if __name__ == "__main__":
    game_over = False
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")

    draw_game_start(screen)
    draw_game_over(game_over)
