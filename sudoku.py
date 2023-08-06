import pygame
import random

import sudoku_generator
from sudoku_elements import *
from sudoku_generator import SudokuGenerator

def main():
    pygame.init()
    screen = pygame.display.set_mode((500, 600))
    clock = pygame.time.Clock()

    game_mode_select = True
    game_active = False
    game_over = False
    selection = False
    game_won = None

    # The following block of code will be to construct the game_mode_select screen.
    # I have an idea of having the numbers from 1 to 9 fly around in the background.
    mode_background = pygame.Surface((500,600))
    mode_background.fill("grey")

    # Fonts
    mode_background_font = pygame.font.Font(None, 30)
    main_font = pygame.font.Font(None, 50)

    # Background Numbers
    mode_background_1_surf = mode_background_font.render("1", True, "black")
    mode_background_1_rect = mode_background_1_surf.get_rect(center=(random.randint(0, 500), random.randint(0, 500)))
    mode_background_2_surf = mode_background_font.render("2", True, "black")
    mode_background_2_rect = mode_background_2_surf.get_rect(center=(random.randint(0, 500), random.randint(0, 500)))
    mode_background_3_surf = mode_background_font.render("3", True, "black")
    mode_background_3_rect = mode_background_3_surf.get_rect(center=(random.randint(0, 500), random.randint(0, 500)))
    mode_background_4_surf = mode_background_font.render("4", True, "black")
    mode_background_4_rect = mode_background_4_surf.get_rect(center=(random.randint(0, 500), random.randint(0, 500)))
    mode_background_5_surf = mode_background_font.render("5", True, "black")
    mode_background_5_rect = mode_background_5_surf.get_rect(center=(random.randint(0, 500), random.randint(0, 500)))
    mode_background_6_surf = mode_background_font.render("6", True, "black")
    mode_background_6_rect = mode_background_6_surf.get_rect(center=(random.randint(0, 500), random.randint(0, 500)))
    mode_background_7_surf = mode_background_font.render("7", True, "black")
    mode_background_7_rect = mode_background_7_surf.get_rect(center=(random.randint(0, 500), random.randint(0, 500)))
    mode_background_8_surf = mode_background_font.render("8", True, "black")
    mode_background_8_rect = mode_background_8_surf.get_rect(center=(random.randint(0, 500), random.randint(0, 500)))
    mode_background_9_surf = mode_background_font.render("9", True, "black")
    mode_background_9_rect = mode_background_9_surf.get_rect(center=(random.randint(0, 500), random.randint(0, 500)))
    rand_dir_1_x = random.randint(1, 5) * random.choice([-1, 1])
    rand_dir_1_y = random.randint(1, 5) * random.choice([-1, 1])
    rand_dir_2_x = random.randint(1, 5) * random.choice([-1, 1])
    rand_dir_2_y = random.randint(1, 5) * random.choice([-1, 1])
    rand_dir_3_x = random.randint(1, 5) * random.choice([-1, 1])
    rand_dir_3_y = random.randint(1, 5) * random.choice([-1, 1])
    rand_dir_4_x = random.randint(1, 5) * random.choice([-1, 1])
    rand_dir_4_y = random.randint(1, 5) * random.choice([-1, 1])
    rand_dir_5_x = random.randint(1, 5) * random.choice([-1, 1])
    rand_dir_5_y = random.randint(1, 5) * random.choice([-1, 1])
    rand_dir_6_x = random.randint(1, 5) * random.choice([-1, 1])
    rand_dir_6_y = random.randint(1, 5) * random.choice([-1, 1])
    rand_dir_7_x = random.randint(1, 5) * random.choice([-1, 1])
    rand_dir_7_y = random.randint(1, 5) * random.choice([-1, 1])
    rand_dir_8_x = random.randint(1, 5) * random.choice([-1, 1])
    rand_dir_8_y = random.randint(1, 5) * random.choice([-1, 1])
    rand_dir_9_x = random.randint(1, 5) * random.choice([-1, 1])
    rand_dir_9_y = random.randint(1, 5) * random.choice([-1, 1])
    mode_background_list = [[mode_background_1_rect, [rand_dir_1_x, rand_dir_1_y]],
                            [mode_background_2_rect, [rand_dir_2_x, rand_dir_2_y]],
                            [mode_background_3_rect, [rand_dir_3_x, rand_dir_3_y]],
                            [mode_background_4_rect, [rand_dir_4_x, rand_dir_4_y]],
                            [mode_background_5_rect, [rand_dir_5_x, rand_dir_5_y]],
                            [mode_background_6_rect, [rand_dir_6_x, rand_dir_6_y]],
                            [mode_background_7_rect, [rand_dir_7_x, rand_dir_7_y]],
                            [mode_background_8_rect, [rand_dir_8_x, rand_dir_8_y]],
                            [mode_background_9_rect, [rand_dir_9_x, rand_dir_9_y]]]

    welcome_surf = main_font.render("Welcome to Sudoku!", True, "black")
    welcome_rect = welcome_surf.get_rect(midtop = (250, 100))

    select_diff_surf = main_font.render("Select Game Mode:", True, "black")
    select_diff_rect = select_diff_surf.get_rect(midtop = (250, 250))

    easy_surf = main_font.render("Easy", True, "black")
    easy_rect = easy_surf.get_rect(midbottom = (100, 400))

    medium_surf = main_font.render("Medium", True, "black")
    medium_rect = medium_surf.get_rect(midbottom = (250, 400))

    hard_surf = main_font.render("Hard", True, "black")
    hard_rect = hard_surf.get_rect(midbottom = (400, 400))

    # I want each cell to be 50 pixels, so a total of 450 pixels, so bordered by 25 pixels on each side.
    while True:

        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if game_active and event.type == pygame.KEYDOWN and selection:
                if event.key == pygame.K_ESCAPE:
                    selection = False
                elif pygame.K_1 <= event.key <= pygame.K_9:
                    number = event.key - pygame.K_0  # Convert key to integer
                    game_board.sketch(selection_pos_index, number)

                elif event.key == pygame.K_RETURN:
                    game_board.place_number(selection_pos_index, game_board.sketch_board_list[selection_pos_index])
                    game_board.clear_sketch(selection_pos_index)
                    selection = False
                    if game_board.is_full():
                        game_active = False
                        game_over = True
                        if game_board.check_board():
                            game_won = True
                        elif not game_board.check_board():
                            game_won = False


                # allow clearing of a sketched number:
                elif event.key == pygame.K_c:
                    game_board.clear_sketch(selection_pos_index)
                # move up
                elif event.key == pygame.K_UP or event.type == pygame.K_w:
                    selection_pos, selection_pos_index = game_board.move_selection("up", selection_pos_index, selection_pos)
                # move down
                elif event.key == pygame.K_DOWN or event.type == pygame.K_s:
                    selection_pos, selection_pos_index = game_board.move_selection("down", selection_pos_index, selection_pos)
                # move left
                elif event.key == pygame.K_LEFT or event.type == pygame.K_a:
                    selection_pos, selection_pos_index = game_board.move_selection("left", selection_pos_index, selection_pos)
                # move right
                elif event.key == pygame.K_RIGHT or event.type == pygame.K_d:
                    selection_pos, selection_pos_index = game_board.move_selection("right", selection_pos_index, selection_pos)

            if game_over and not game_won:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if game_restart_rect.collidepoint(mouse_pos):
                        game_over = False
                        game_won = None
                        game_mode_select = True
            if game_over and game_won:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if game_exit_rect.collidepoint(mouse_pos):
                        pygame.quit()
                        exit()

        if game_mode_select:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pressed = pygame.time.get_ticks()
                if easy_rect.collidepoint(mouse_pos):
                    difficulty = 30
                    game_board = Board(screen, difficulty)
                    game_mode_select = False
                    game_active = True
                if medium_rect.collidepoint(mouse_pos):
                    difficulty = 40
                    game_board = Board(screen, difficulty)
                    game_mode_select = False
                    game_active = True
                if hard_rect.collidepoint(mouse_pos):
                    difficulty = 50
                    game_board = Board(screen, difficulty)
                    game_mode_select = False
                    game_active = True

        if game_active:
            game_board.draw()

            if game_board.reset_button_bg_rect.collidepoint(mouse_pos):
                pygame.draw.rect(screen, "red", game_board.reset_button_bg_rect, 5)

            if game_board.restart_button_bg_rect.collidepoint(mouse_pos):
                pygame.draw.rect(screen, "red", game_board.restart_button_bg_rect, 5)

            if game_board.exit_button_bg_rect.collidepoint(mouse_pos):
                pygame.draw.rect(screen, "red", game_board.exit_button_bg_rect, 5)

            if event.type == pygame.MOUSEBUTTONDOWN:
                # This if statement prevents the mouse button down event from
                # engaging selection during phase transition
                if pygame.time.get_ticks() - mouse_pressed >= 500:
                    if not selection:
                        for index, cell_rect in enumerate(game_board.cell_bg_rect_list):
                            temp_selection_pos = pygame.mouse.get_pos()
                            if cell_rect.collidepoint(temp_selection_pos) and game_board.iterable_board[index] == 0:
                                selection_pos = pygame.mouse.get_pos()
                                selection_pos_index = index
                                selection = True
                    if game_board.reset_button_bg_rect.collidepoint(mouse_pos):
                        game_board.reset_to_original()
                    if game_board.restart_button_bg_rect.collidepoint(mouse_pos):
                        game_active = False
                        game_mode_select = True
                    if game_board.exit_button_bg_rect.collidepoint(mouse_pos):
                        pygame.quit()
                        exit()

            if selection:

                if event.type == pygame.MOUSEBUTTONDOWN:
                    temp_selection_pos = pygame.mouse.get_pos()
                    for index, cell_rect in enumerate(game_board.cell_bg_rect_list):
                        if cell_rect.collidepoint(temp_selection_pos) and game_board.iterable_board[index] == 0:
                            selection_pos = temp_selection_pos
                            selection_pos_index = index

                for cell_rect in game_board.cell_bg_rect_list:
                    if cell_rect.collidepoint(selection_pos):
                        pygame.draw.rect(screen, "red", cell_rect, 5)

            if not selection:
                for index, cell_rect in enumerate(game_board.cell_bg_rect_list):
                    if cell_rect.collidepoint(mouse_pos) and game_board.iterable_board[index] == 0:
                        pygame.draw.rect(screen, "red", cell_rect, 5)


        # Game Mode Select Screen:
        if game_mode_select:
            screen.blit(mode_background, (0, 0))

            # This for loop is for all the background numbers
            # to fly around in an independently random direction.

            for i in mode_background_list:
                i[0].x += i[1][0]
                i[0].y += i[1][1]
                if i[0].x <= 0 or i[0].x >= 600:
                    i[0].x = random.randint(-25, 625)
                    i[1][0] = random.randint(1, 5) * random.choice([-1, 1])
                    i[1][1] = random.randint(1, 5) * random.choice([-1, 1])
                if i[0].y <= 0 or i[0].y >= 500:
                    i[0].y = random.randint(-25, 525)
                    i[1][0] = random.randint(1, 5) * random.choice([-1, 1])
                    i[1][1] = random.randint(1, 5) * random.choice([-1, 1])

            screen.blit(mode_background_1_surf, mode_background_1_rect)
            screen.blit(mode_background_2_surf, mode_background_2_rect)
            screen.blit(mode_background_3_surf, mode_background_3_rect)
            screen.blit(mode_background_4_surf, mode_background_4_rect)
            screen.blit(mode_background_5_surf, mode_background_5_rect)
            screen.blit(mode_background_6_surf, mode_background_6_rect)
            screen.blit(mode_background_7_surf, mode_background_7_rect)
            screen.blit(mode_background_8_surf, mode_background_8_rect)
            screen.blit(mode_background_9_surf, mode_background_9_rect)

            pygame.draw.rect(screen, "white", welcome_rect.inflate(15, 15), border_radius=15)
            screen.blit(welcome_surf, welcome_rect)

            pygame.draw.rect(screen, "white", select_diff_rect.inflate(15, 15), border_radius=15)
            screen.blit(select_diff_surf, select_diff_rect)

            pygame.draw.rect(screen, "white", easy_rect.inflate(10, 10), border_radius=10)
            if easy_rect.collidepoint(mouse_pos):
                pygame.draw.rect(screen, "red", easy_rect.inflate(10, 10), border_radius=10)
            screen.blit(easy_surf, easy_rect)

            pygame.draw.rect(screen, "white", medium_rect.inflate(10, 10), border_radius=10)
            if medium_rect.collidepoint(mouse_pos):
                pygame.draw.rect(screen, "red", medium_rect.inflate(10, 10), border_radius=10)
            screen.blit(medium_surf, medium_rect)

            pygame.draw.rect(screen, "white", hard_rect.inflate(10, 10), border_radius=10)
            if hard_rect.collidepoint(mouse_pos):
                pygame.draw.rect(screen, "red", hard_rect.inflate(10, 10), border_radius=10)
            screen.blit(hard_surf, hard_rect)

        # End Screen
        if game_over:  #game over block here

            # Will use check_board function, returns True or False

            screen.blit(mode_background, (0, 0))

            # This for loop is for all the background numbers
            # to fly around in an independently random direction.

            for i in mode_background_list:
                i[0].x += i[1][0]
                i[0].y += i[1][1]
                if i[0].x <= 0 or i[0].x >= 600:
                    i[0].x = random.randint(-25, 625)
                    i[1][0] = random.randint(1, 5) * random.choice([-1, 1])
                    i[1][1] = random.randint(1, 5) * random.choice([-1, 1])
                if i[0].y <= 0 or i[0].y >= 500:
                    i[0].y = random.randint(-25, 525)
                    i[1][0] = random.randint(1, 5) * random.choice([-1, 1])
                    i[1][1] = random.randint(1, 5) * random.choice([-1, 1])

            screen.blit(mode_background_1_surf, mode_background_1_rect)
            screen.blit(mode_background_2_surf, mode_background_2_rect)
            screen.blit(mode_background_3_surf, mode_background_3_rect)
            screen.blit(mode_background_4_surf, mode_background_4_rect)
            screen.blit(mode_background_5_surf, mode_background_5_rect)
            screen.blit(mode_background_6_surf, mode_background_6_rect)
            screen.blit(mode_background_7_surf, mode_background_7_rect)
            screen.blit(mode_background_8_surf, mode_background_8_rect)
            screen.blit(mode_background_9_surf, mode_background_9_rect)

            # Game Won

            if game_won:
                game_over_won = main_font.render("Game Won!", True, "black")
                game_won_rect = game_over_won.get_rect(midtop=(250, 200))
                pygame.draw.rect(screen, "green", game_won_rect.inflate(15, 15), border_radius=15)
                screen.blit(game_over_won, game_won_rect)

                game_won_exit = main_font.render("Exit", True, "black")
                game_exit_rect = game_won_exit.get_rect(midbottom=(250, 350))
                pygame.draw.rect(screen, "white", game_exit_rect.inflate(10, 10), border_radius=10)
                if game_exit_rect.collidepoint(mouse_pos):
                    pygame.draw.rect(screen, "blue", game_exit_rect.inflate(10, 10), border_radius=10)
                screen.blit(game_won_exit, game_exit_rect)

            # Game Lose

            elif not game_won:
                game_over_lose = main_font.render("Game Over :(", True, "black")
                game_lose_rect = game_over_lose.get_rect(midtop=(250, 200))
                pygame.draw.rect(screen, "red", game_lose_rect.inflate(15, 15), border_radius=15)
                screen.blit(game_over_lose, game_lose_rect)

                game_over_restart = main_font.render("Restart", True, "black")
                game_restart_rect = game_over_restart.get_rect(midbottom=(250, 350))
                pygame.draw.rect(screen, "white", game_restart_rect.inflate(10, 10), border_radius=10)
                if game_restart_rect.collidepoint(mouse_pos):
                    pygame.draw.rect(screen, "orange", game_restart_rect.inflate(10, 10), border_radius=10)
                screen.blit(game_over_restart, game_restart_rect)

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()