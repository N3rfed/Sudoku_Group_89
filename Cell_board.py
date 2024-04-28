import pygame
class Board:
    pygame.init()
    def __init__(self, width, height, screen, difficulty, boards):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.board = boards[0]
        self.solution = boards[1]
        self.cells = [[None for i in range(9)] for j in range(9)]

        self.surface = pygame.Surface((720, 720))
        self.surface.fill((255,255,255))
        self.selected = None

        for i in range(9):
            for j in range(9):
                self.cells[i][j] = Cell(self.board[i][j], i, j, self.surface)

    def draw(self):
        for i in range(9):
            for j in range(9):
                self.cells[i][j].draw()
        self.screen.blit(self.surface, (140, 50))

        for a in range(3):
            for b in range(3):
                cell_rect = pygame.Rect((a * 240 + 140, b * 240 + 50), (240, 240))
                pygame.draw.rect(self.screen, (0,0,0), cell_rect, 5)

    def select(self, row, col):
        if row < 0 or col < 0:
            return -1
        for i in self.cells:
            for j in i:
                j.selected = False
        try:
            self.cells[row][col].selected = True
            self.selectedPos = (row, col)
            self.selected = self.cells[row][col]
        except:
            pass


    def click(self, x, y):
        return (int(x//(self.width/9)), int(y//(self.height/9)))

    def clear(self):
        if self.board[self.selectedPos[0]][self.selectedPos[1]] == 0:
            self.selected.value = 0
            self.selected.sketched = None
    def sketch(self, value):
        if self.board[self.selectedPos[0]][self.selectedPos[1]] == 0:
            try:
                value = int(value)
                if value > 9 or value < 1:
                    raise Exception

                self.selected.sketched = value
            except:
                pass
    def place_number(self):
        if self.selected.sketched is not None:
            self.selected.value = self.selected.sketched
            self.selected.sketched = None

    def reset(self):
        for i in range(9):
            for j in range(9):
                self.cells[i][j] = Cell(self.board[i][j], i, j, self.surface)

    def is_full(self):
        for i in self.cells:
            for j in i:
                if j.value == 0:
                    return False
        return True



    def update_board(self):
        pass

    def find_empty(self):
        for i in self.cells:
            for j in i:
                if j.value == 0:
                    return (i, j)

    def check_board(self):
        for i in range(len(self.cells)):
            for j in range(len(self.cells[i])):
                if self.cells[i][j].value != self.solution[i][j]:
                    return False
        return True
class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.selected = False
        self.sketched = None

    def draw(self):
        pygame.init()
        if self.selected:
            color = (255, 0, 0)
            width = 7
        else:
            color = (0, 0, 0)
            width = 1

        rect_fill = pygame.Rect((self.row * 80, self.col * 80), (80,80))
        pygame.draw.rect(self.screen, (255,255,255), rect_fill)

        cell_rect = pygame.Rect((self.row * 80, self.col * 80), (80, 80))
        pygame.draw.rect(self.screen, color, cell_rect, width)

        number_font = pygame.font.Font(None, 70)
        if self.value == 0:
            title_surface = number_font.render(" ", 0, (0, 0, 0))
        else:
            title_surface = number_font.render(str(self.value), 0, (0, 0, 0))

        self.screen.blit(title_surface, (cell_rect.centerx - 15, cell_rect.centery - 20))

        if self.sketched is not None:
            sketch_font = pygame.font.Font(None, 40)
            other_surface = sketch_font.render(str(self.sketched), 0, (0,0,255))
            self.screen.blit(other_surface, (cell_rect.left + 7, cell_rect.top + 5))