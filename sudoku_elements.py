import pygame

import sudoku_generator

class Board:

    def __init__(self, screen, difficulty):
        self.my_font = pygame.font.Font(None, 30)
        self.sketch_font = pygame.font.Font(None, 20)
        self.difficulty = difficulty
        self.screen = screen
        self.cell_bg_surf_list = []
        self.cell_bg_rect_list = []
        self.cell_surf_list = []
        self.cell_rect_list = []

        self.board_object = sudoku_generator.SudokuGenerator(9, difficulty)
        self.board = self.board_object.get_board()
        self.board_object.fill_values()
        self.solved_board = self.board_object.solved_board
        self.board_object.remove_cells()
        self.original_board = [row[:] for row in self.board]

        self.sketch_board_list = []
        self.sketch_board_surf_list = []
        self.sketch_board_rect_list = []
        self.iterable_board = []

        self.create_board()

        # Reset button:

        self.reset_button_bg_surf = pygame.Surface((100, 50))
        self.reset_button_bg_surf.fill("grey")
        self.reset_button_bg_rect = self.reset_button_bg_surf.get_rect(center = (100, 525))
        self.reset_button_surf = self.my_font.render("Reset", True, "black")
        self.reset_button_rect = self.reset_button_surf.get_rect(center = (100, 525))

        # Restart button:

        self.restart_button_bg_surf = pygame.Surface((100, 50))
        self.restart_button_bg_surf.fill("grey")
        self.restart_button_bg_rect = self.restart_button_bg_surf.get_rect(center = (250, 525))
        self.restart_button_surf = self.my_font.render("Restart", True, "black")
        self.restart_button_rect = self.restart_button_surf.get_rect(center= (250, 525))

        # Exit button:

        self.exit_button_bg_surf = pygame.Surface((100, 50))
        self.exit_button_bg_surf.fill("grey")
        self.exit_button_bg_rect = self.exit_button_bg_surf.get_rect(center = (400, 525))
        self.exit_button_surf = self.my_font.render("Exit", True, "black")
        self.exit_button_rect = self.exit_button_surf.get_rect(center = (400, 525))

    def create_board(self):
        # Sketched numbers:
        for i in range(81):
            self.sketch_board_list.append(0)
        for i in self.sketch_board_list:
            self.sketch_board_surf_list.append(self.sketch_font.render(str(i), True, "grey"))
        x_increment = 0
        y_increment = 0
        for surf in self.sketch_board_surf_list:
            self.sketch_board_rect_list.append(
                surf.get_rect(topleft=((35 + (50 * x_increment)), (35 + (50 * y_increment)))))
            x_increment += 1
            if x_increment >= 9:
                x_increment = 0
                y_increment += 1
            if y_increment >= 9:
                break

        # Makes list of cell number surfaces
        for i in self.board:
            for number in i:
                self.cell_surf_list.append(self.my_font.render(str(number), True, "black", ))
        for i in self.board:
            for j in i:
                self.iterable_board.append(j)

        x_increment = 0
        y_increment = 0

        # Makes background cell rectangles
        for i in range(81):
            self.cell_bg_surf_list.append(pygame.Surface((50, 50)))
            if x_increment >= 9:
                x_increment = 0
                y_increment += 1
            self.cell_bg_rect_list.append(
                self.cell_bg_surf_list[i].get_rect(center=(50 + (50 * x_increment), 50 + (50 * y_increment))))
            x_increment += 1
            if y_increment >= 9:
                break

        # Makes cell rectangles
        x_increment = 0
        y_increment = 0
        for index, surf in enumerate(self.cell_surf_list):
            if x_increment >= 9:
                x_increment = 0
                y_increment += 1
            self.cell_rect_list.append(
                self.cell_surf_list[index].get_rect(center=(50 + (50 * x_increment), 50 + (50 * y_increment))))
            x_increment += 1
            if y_increment >= 9:
                break

    def draw(self):
        self.screen.fill("dark grey")

        # makes cell backgrounds white
        for surf in self.cell_bg_surf_list:
            surf.fill("white")

        # prints cell backgrounds
        for index, surf in enumerate(self.cell_bg_surf_list):
            self.screen.blit(surf, self.cell_bg_rect_list[index])

        # draw lines for board
        increment = 0
        for i in range(9):
            pygame.draw.line(self.screen, "black", (25 + (50 * increment), 25), (25 + (50 * increment), 475), 1)
            pygame.draw.line(self.screen, "black", (25, 25 + (50 * increment)) , (475, 25 + (50 * increment)), 1)
            increment += 1
        pygame.draw.line(self.screen, "black", (25, 25), (25, 475), 5)
        pygame.draw.line(self.screen, "black", (175, 25), (175, 475), 5)
        pygame.draw.line(self.screen, "black", (325, 25), (325, 475), 5)
        pygame.draw.line(self.screen, "black", (475, 25), (475, 475), 5)
        pygame.draw.line(self.screen, "black", (25, 25), (475, 25), 5)
        pygame.draw.line(self.screen, "black", (25, 175), (475, 175), 5)
        pygame.draw.line(self.screen, "black", (25, 325), (475, 325), 5)
        pygame.draw.line(self.screen, "black", (25, 475), (475, 475), 5)

        # Draw numbers for board.
        for index, surf in enumerate(self.cell_surf_list):
            if self.iterable_board[index] != 0:
                self.screen.blit(surf, self.cell_rect_list[index])

        # Reset button.
        self.screen.blit(self.reset_button_bg_surf, self.reset_button_bg_rect)
        self.screen.blit(self.reset_button_surf, self.reset_button_rect)

        # Restart button.
        self.screen.blit(self.restart_button_bg_surf, self.restart_button_bg_rect)
        self.screen.blit(self.restart_button_surf, self.restart_button_rect)

        # Exit button.
        self.screen.blit(self.exit_button_bg_surf, self.exit_button_bg_rect)
        self.screen.blit(self.exit_button_surf, self.exit_button_rect)

        # Draw sketched numbers.
        for index, surf in enumerate(self.sketch_board_surf_list):
            if self.sketch_board_list[index] != 0:
                self.screen.blit(surf, self.sketch_board_rect_list[index])

    def move_selection(self, direction, index, pos):
        [row, col] = self.find_row_and_col(index)
        row -= 1
        col -=1
        (x, y) = pos
        if direction == "up":
            for i in range(8):
                y -= 50
                for index, value in enumerate(self.iterable_board):
                    if self.cell_bg_rect_list[index].collidepoint((x, y)) and value == 0:
                        pos = (x, y)
                        return pos, index
                if y <= 25:
                    y = 500
        elif direction == "down":
            for i in range(8):
                y += 50
                for index, value in enumerate(self.iterable_board):
                    if self.cell_bg_rect_list[index].collidepoint((x, y)) and value == 0:
                        pos = (x, y)
                        return pos, index
                if y >= 475:
                    y = 0
        elif direction == "left":
            for i in range(8):
                x -= 50
                for index, value in enumerate(self.iterable_board):
                    if self.cell_bg_rect_list[index].collidepoint((x, y)) and value == 0:
                        pos = (x, y)
                        return pos, index
                if x <= 25:
                    x = 500

        elif direction == "right":
            for i in range(8):
                x += 50
                for index, value in enumerate(self.iterable_board):
                    if self.cell_bg_rect_list[index].collidepoint((x, y)) and value == 0:
                        pos = (x, y)
                        return pos, index
                if x >= 475:
                    x = 0

    def click(self, x, y):
        pass

    def clear(self):
        pass

    def sketch(self, index, value):
        self.sketch_board_list[index] = value
        self.sketch_board_surf_list[index] = self.sketch_font.render(str(value), True, "grey")

    def clear_sketch(self, index):
        self.sketch_board_list[index] = 0
        self.sketch_board_surf_list[index] = self.sketch_font.render("0", True, "grey")
        pass

    def place_number(self, index, value):
        [row, col] = self.find_row_and_col(index)
        self.iterable_board[index] = value
        self.cell_surf_list = []
        self.board[row][col] = value
        for i in self.board:
            for number in i:
                self.cell_surf_list.append(self.my_font.render(str(number), True, "black", ))
        self.iterable_board = []
        for i in self.board:
            for j in i:
                self.iterable_board.append(j)

    @staticmethod
    def find_row_and_col(index):
        row = index // 9
        col = index % 9
        return row, col




    def reset_to_original(self):
        self.board = self.original_board
        self.cell_bg_surf_list = []
        self.cell_bg_rect_list = []
        self.cell_rect_list = []
        self.cell_surf_list = []
        self.sketch_board_list = []
        self.sketch_board_surf_list = []
        self.iterable_board = []
        self.create_board()

    def is_full(self):
        for value in self.iterable_board:
            if value == 0:
                return False
        return True

    def check_board(self):
        if self.board == self.solved_board:
            return True
        else:
            return False
