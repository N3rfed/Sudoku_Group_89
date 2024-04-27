import pygame, sys
import sudoku_generator
from sudoku_generator import Board

LINE_COLOR = (30, 227, 49)
HEIGHT = 1000
WIDTH = 1000

def draw_game_start(screen):
    start_title_font = pygame.font.Font(None,100)
    other_text_font = pygame.font.Font(None, 85)
    button_font = pygame.font.Font(None, 70)

    screen.fill((179, 255, 207))

    title_surface = start_title_font.render("Welcome to Sudoku", 0 , (LINE_COLOR))
    title_rectangle = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 250))
    screen.blit(title_surface, title_rectangle)

    other_text = other_text_font.render("Select Game Mode:", 0, (LINE_COLOR))
    other_rectangle = other_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    screen.blit(other_text, other_rectangle)

    easy_text = button_font.render("Easy", 0, (255,255,255))
    medium_text = button_font.render("Medium", 0, (255,255,255))
    hard_text = button_font.render("Hard", 0, (255,255,255))

    easy_surface = pygame.Surface((easy_text.get_size()[0] +20, easy_text.get_size()[1] +20))
    easy_surface.fill(LINE_COLOR)
    easy_surface.blit(easy_text,(10,10))
    medium_surface = pygame.Surface((medium_text.get_size()[0] +20, medium_text.get_size()[1] +20))
    medium_surface.fill(LINE_COLOR)
    medium_surface.blit(medium_text, (10, 10))
    hard_surface = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
    hard_surface.fill(LINE_COLOR)
    hard_surface.blit(hard_text, (10, 10))

    easy_rectangle = easy_surface.get_rect(center =(WIDTH//2, HEIGHT//2 + 50))
    medium_rectangle = medium_surface.get_rect(center =(WIDTH//2, HEIGHT//2 + 150))
    hard_rectangle = hard_surface.get_rect(center=(WIDTH//2, HEIGHT//2 + 250))

    screen.blit(easy_surface,easy_rectangle)
    screen.blit(medium_surface,medium_rectangle)
    screen.blit(hard_surface, hard_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rectangle.collidepoint(event.pos):
                    return 30
                if medium_rectangle.collidepoint(event.pos):
                    return 40
                if hard_rectangle.collidepoint(event.pos):
                    return 50
        pygame.display.update()
def won_game(screen):
    win_font = pygame.font.Font(None, 100)
    button_font = pygame.font.Font(None, 70)

    screen.fill((255, 255, 255))

    win_surface = win_font.render("Game Won!", 0, (0, 0, 0))
    win_rectangle = win_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 150))
    screen.blit(win_surface, win_rectangle)

    exit_text = button_font.render("Exit", 0, (255, 255, 255))

    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surface.fill(LINE_COLOR)
    exit_surface.blit(exit_text, (10, 10))

    exit_rectangle = exit_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    screen.blit(exit_surface, exit_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_rectangle.collidepoint(event.pos):
                    pygame.quit()


        pygame.display.update()

def lost_game(screen):

    lose_font = pygame.font.Font(None, 100)
    button_font = pygame.font.Font(None, 70)

    screen.fill((255, 255, 255))

    lose_surface = lose_font.render("Game Over :(", 0, (0, 0, 0))
    lose_rectangle = lose_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 150))
    screen.blit(lose_surface, lose_rectangle)

    restart_text = button_font.render("Restart", 0, (255, 255, 255))

    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart_surface.fill(LINE_COLOR)
    restart_surface.blit(restart_text, (10, 10))

    restart_rectangle = restart_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    screen.blit(restart_surface, restart_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_rectangle.collidepoint(event.pos):
                    return True

        pygame.display.update()
def draw_buttons(buttonList):
    button_font = pygame.font.Font(None, 70)

    reset_text = button_font.render("Reset", 0, (255, 255, 255))
    restart_text = button_font.render("Restart", 0, (255, 255, 255))
    exit_text = button_font.render("Exit", 0, (255, 255, 255))

    reset_surface = pygame.Surface((reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 20))
    reset_surface.fill(LINE_COLOR)
    reset_surface.blit(reset_text, (10, 10))

    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart_surface.fill(LINE_COLOR)
    restart_surface.blit(restart_text, (10, 10))

    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surface.fill(LINE_COLOR)
    exit_surface.blit(exit_text, (10, 10))

    reset_rectangle = reset_surface.get_rect(center=(WIDTH // 2 - 220, HEIGHT // 10 * 9))
    restart_rectangle = restart_surface.get_rect(center=(WIDTH // 2, HEIGHT // 10 * 9))
    exit_rectangle = exit_surface.get_rect(center=(WIDTH // 2 + 220, HEIGHT // 10 * 9))

    screen.blit(reset_surface, reset_rectangle)
    screen.blit(restart_surface, restart_rectangle)
    screen.blit(exit_surface, exit_rectangle)

    buttonList.append(reset_rectangle)
    buttonList.append(restart_rectangle)
    buttonList.append(exit_rectangle)

    return

if __name__ == "__main__":
    game_over = False
    restart = True
    buttons = []
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")

    while restart == True:
        restart = False
        diff = draw_game_start(screen)

        game_board = Board(720, 720, screen, diff, sudoku_generator.generate_sudoku(9, diff))
        draw_buttons(buttons)
        game_board.draw()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    game_board.select(game_board.click(event.pos[0] - 140, event.pos[1] - 50)[0], game_board.click(event.pos[0] - 140, event.pos[1] - 50)[1])

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if buttons[2].collidepoint(event.pos):
                        pygame.quit()
                    elif buttons[1].collidepoint(event.pos):
                        restart = True
                        break
                    elif buttons[0].collidepoint(event.pos):
                        for i in range(len(game_board.cellArray)):
                            for j in range(len(game_board.cellArray)):
                                game_board.cellArray[i][j].sketched = None
                                game_board.cellArray[i][j].value = game_board.boardArray[i][j]

                if event.type == pygame.KEYDOWN:
                    game_board.sketch(pygame.key.name(event.key))

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_board.place_number()
                    elif event.key == pygame.K_0:
                        game_board.clear()

                    elif event.key == pygame.K_LEFT:
                        if game_board.selectedPos[0] != 0:
                            game_board.select(game_board.selectedPos[0]-1, game_board.selectedPos[1])
                    elif event.key == pygame.K_RIGHT:
                        if game_board.selectedPos[0] != 8:
                            game_board.select(game_board.selectedPos[0]+1, game_board.selectedPos[1])
                    elif event.key == pygame.K_UP:
                        if game_board.selectedPos[1] != 0:
                            game_board.select(game_board.selectedPos[0], game_board.selectedPos[1]-1)
                    elif event.key == pygame.K_DOWN:
                        if game_board.selectedPos[1] != 8:
                            game_board.select(game_board.selectedPos[0], game_board.selectedPos[1]+1)

            game_board.draw()
            if game_board.is_full():
                if game_board.check_board():
                    restart = won_game(screen)
                else:
                    restart = lost_game(screen)
            pygame.display.update()

            if restart == True:
                break