import math, random, pygame

"""
This was adapted from a GeeksforGeeks article "Program for Sudoku Generator" by Aarti_Rathi and Ankur Trisal
https://www.geeksforgeeks.org/program-sudoku-generator/

"""


class SudokuGenerator:
    '''
	create a sudoku board - initialize class variables and set up the 2D board
	This should initialize:
	self.row_length		- the length of each row
	self.removed_cells	- the total number of cells to be removed
	self.board			- a 2D list of ints to represent the board
	self.box_length		- the square root of row_length

	Parameters:
    row_length is the number of rows/columns of the board (always 9 for this project)
    removed_cells is an integer value - the number of cells to be removed

	Return:
	None
    '''

    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = [[0 for i in range(self.row_length)] for j in range(self.row_length)]
        self.box_length = int(math.sqrt(row_length))

    def get_board(self):
        return self.board

    '''
	Displays the board to the console
    This is not strictly required, but it may be useful for debugging purposes

	Parameters: None
	Return: None
    '''

    def print_board(self):
        for i in range(self.row_length):
            for j in range(self.row_length):
                print(self.board[i][j], end=' ')
            print()

    '''
	Determines if num is contained in the specified row (horizontal) of the board
    If num is already in the specified row, return False. Otherwise, return True

	Parameters:
	row is the index of the row we are checking
	num is the value we are looking for in the row

	Return: boolean
    '''

    def valid_in_row(self, row, num):
        for col in range(self.row_length):
            if num == self.board[row][col]:
                return False
        return True

    '''
	Determines if num is contained in the specified column (vertical) of the board
    If num is already in the specified col, return False. Otherwise, return True

	Parameters:
	col is the index of the column we are checking
	num is the value we are looking for in the column

	Return: boolean
    '''

    def valid_in_col(self, col, num):
        for row in range(self.row_length):
            if num == self.board[row][col]:
                return False
        return True

    '''
	Determines if num is contained in the 3x3 box specified on the board
    If num is in the specified box starting at (row_start, col_start), return False.
    Otherwise, return True

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)
	num is the value we are looking for in the box

	Return: boolean
    '''

    def valid_in_box(self, row_start, col_start, num):
        for row in range(row_start, row_start + 3):
            for col in range(col_start, col_start + 3):
                if self.board[row][col] == num:
                    return False
        return True

    '''
    Determines if it is valid to enter num at (row, col) in the board
    This is done by checking that num is unused in the appropriate, row, column, and box

	Parameters:
	row and col are the row index and col index of the cell to check in the board
	num is the value to test if it is safe to enter in this cell

	Return: boolean
    '''

    def is_valid(self, row, col, num):
        if self.valid_in_row(row, num) and self.valid_in_col(col, num) and self.valid_in_box(row // 3 * 3, col // 3 * 3,
                                                                                             num):
            return True
        else:
            return False

    '''
    Fills the specified 3x3 box with values
    For each position, generates a random digit which has not yet been used in the box

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)

	Return: None
    '''

    def fill_box(self, row_start, col_start):
        box_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                random_valid_number = random.choice(box_values)
                while not self.is_valid(i, j, random_valid_number):
                    random_valid_number = random.choice(box_values)
                self.board[i][j] = random_valid_number
                box_values.remove(random_valid_number)
        return self.board

    '''
    Fills the three boxes along the main diagonal of the board
    These are the boxes which start at (0,0), (3,3), and (6,6)

	Parameters: None
	Return: None
    '''

    def fill_diagonal(self):
        for i in range(0, 7, 3):
            self.fill_box(i, i)

    # '''
    # DO NOT CHANGE
    # Provided for students
    # Fills the remaining cells of the board
    # Should be called after the diagonal boxes have been filled
    #
    # Parameters:
    # row, col specify the coordinates of the first empty (0) cell
    #
    # Return:
    # boolean (whether or not we could solve the board)
    # '''

    def fill_remaining(self, row, col):
        if col >= self.row_length and row < self.row_length - 1:
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    # '''
    # DO NOT CHANGE
    # Provided for students
    # Constructs a solution by calling fill_diagonal and fill_remaining
    #
    # Parameters: None
    # Return: None
    # '''

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    '''
    Removes the appropriate number of cells from the board
    This is done by setting some values to 0
    Should be called after the entire solution has been constructed
    i.e. after fill_values has been called

    NOTE: Be careful not to 'remove' the same cell multiple times
    i.e. if a cell is already 0, it cannot be removed again

	Parameters: None
	Return: None
    '''

    def remove_cells(self):
        counter = self.removed_cells
        while counter > 0:
            row = random.randrange(9)
            col = random.randrange(9)
            self.board[row][col] = 0
            counter -= 1


# '''
# DO NOT CHANGE
# Provided for students
# Given a number of rows and number of cells to remove, this function:
# 1. creates a SudokuGenerator
# 2. fills its values and saves this as the solved state
# 3. removes the appropriate number of cells
# 4. returns the representative 2D Python Lists of the board and solution
#
# Parameters:
# size is the number of rows/columns of the board (9 for this project)
# removed is the number of cells to clear (set to 0)
#
# Return: list[list] (a 2D Python list to represent the board)
# '''


def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    deep_board = sudoku.get_board()
    deep_board = [nums[:] for nums in deep_board]
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board, deep_board


class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.default_sketch = 0
        self.selected_cell = False

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.value = value

    # Draws this cell, along with the value inside it.
    # If this cell has a nonzero value, that value is displayed.
    # Otherwise, no value is displayed in the cell.
    # The cell is outlined red if it is currently selected.
    def draw(self):
        if self.selected_cell:
            color = (255, 0, 0)  # Red
            width = 5

        cell_outline = pygame.Rect((self.row * 50, self.col * 50), (50, 50))
        pygame.draw.rect(self.screen, (255, 255, 255), cell_outline)

        inner_cell = pygame.Rect((self.row * 50, self.col * 50), (50, 50))
        pygame.draw.rect(self.screen, color, inner_cell, width)

        '''if self.value != 0 and self.default_sketch == 0:  # UNFINISHED
            num_font = pygame.font.Font(None, 15)
            num_font_surface = num_font.render(str(self.value), True, (0, 0, 0))
            num_text_rect = num_font_surface.get_rect(center=(cell_outline.centerx, cell_outline.centery))
            self.screen.blit(num_font_surface, num_text_rect)'''
        if self.value != 0:
            number_font = pygame.font.Font(None, 70)
            title_surface = number_font.render(str(self.value), True, (0, 0, 0))
            self.screen.blit(title_surface, (cell_rect.centerx - 15, cell_rect.centery - 20))

            # Render a sketched value if it exists
        if self.sketched is not None:
            sketch_font = pygame.font.Font(None, 40)
            other_surface = sketch_font.render(str(self.sketched), True, (0, 0, 255))
            self.screen.blit(other_surface, (cell_rect.left + 5, cell_rect.top + 5))


class Board:
    def __init__(self, width, height, screen, difficulty, board_data):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.board, self.solution = board_data
        self.cell_size = min(width, height) // 9
        self.offsetX = 140
        self.offsetY = 50
        self.cell = [[0 for i in range(9)] for j in range(9)]
        self.selected_cell = None

    def draw(self):
        pygame.draw.rect(self.screen, pygame.Color("black"), pygame.Rect(145, 15, 720, 720), 10)
        i = 1
        while (i * 80) < 720:
            line_width = 5 if i % 3 > 0 else 10
            pygame.draw.line(self.screen, pygame.Color("black"), pygame.Vector2((i * 80) + 145, 15),
                             pygame.Vector2((i * 80) + 145, 730), line_width)
            pygame.draw.line(self.screen, pygame.Color("black"), pygame.Vector2(145, (i * 80) + 15),
                             pygame.Vector2(860, (i * 80) + 15), line_width)
            i += 1
        pygame.display.update()

    def select(self, row, col):
        if row is None or col is None:
            return  # Invalid click
        if 0 <= row < 9 and 0 <= col < 9:
            # Clear previous selections if any
            if self.selected_cell:
                self.selected_cell = False
            # Select the new cell
            self.selected_cell = self.cell[row][col]
            self.selected_cell = True

    def click(self, x, y):
        if self.offsetX <= x <= self.offsetX + self.width and self.offsetY <= y <= self.offsetY + self.height:
            col = (x - self.offsetX) // self.cell_size
            row = (y - self.offsetY) // self.cell_size
            return row, col
        return None

    def clear(self):
        pass

    def sketch(self, value):
        pass

    def place_number(self, value):
        pass

    def reset_to_original(self):
        pass

    def is_full(self):
        pass

    def update_board(self):
        pass

    def find_empty(self):
        pass

    def check_board(self):
        if self.board == self.solution:
            return True
        return False
