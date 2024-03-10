import pygame

pygame.init()


# screen set up
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

logo = pygame.image.load("./assets/cross.png")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tic tac toe")
pygame.display.set_icon(logo)



# loading assets
cell_image = pygame.transform.scale(pygame.image.load("./assets/cell.png"), (200, 200))
cross_image = pygame.transform.scale(pygame.image.load("./assets/cross.png"), (100, 100))
circle_image = pygame.transform.scale(pygame.image.load("./assets/circle.png"), (100, 100))



# defining the grid
grid = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]



# functions
def handle_user_clicks(x, y, sign):
    for row_index, row in enumerate(grid):
        if y//200 == row_index:
            for cell_index, cell in enumerate(row):
                if x//200 == cell_index:
                    if(grid[row_index][cell_index] == " "):
                        grid[row_index][cell_index] = sign
                        break
            break



def draw_condition_checker(grid):
    for row in grid:
        for cell in row:
            if cell == " ":
                return False
    return True



def win_condition_checker(grid, sign):
    if grid[0][0] == sign and grid[0][1] == sign and grid[0][2] == sign:
        return True
    elif grid[1][0] == sign and grid[1][1] == sign and grid[1][2] == sign:
        return True
    elif grid[2][0] == sign and grid[2][1] == sign and grid[2][2] == sign:
        return True
    elif grid[0][0] == sign and grid[1][0] == sign and grid[2][0] == sign:
        return True
    elif grid[0][1] == sign and grid[1][1] == sign and grid[2][1] == sign:
        return True
    elif grid[0][2] == sign and grid[1][2] == sign and grid[2][2] == sign:
        return True
    elif grid[0][0] == sign and grid[1][1] == sign and grid[2][2] == sign:
        return True
    elif grid[0][2] == sign and grid[1][1] == sign and grid[2][0] == sign:
        return True
    else:
        return False



def draw_grid(grid):
    for row_index, row in enumerate(grid):
        for cell_index, cell in enumerate(row):
            screen.blit(cell_image, (cell_index*200, row_index*200))
            if cell == "X":
                screen.blit(cross_image, (cell_index*200+50, row_index*200+50))
            elif cell == "O":
                screen.blit(circle_image, (cell_index*200+50, row_index*200+50))


# gameloop
running = True
finish = False
clock = pygame.time.Clock()
fps = 60
sign = "X"
font = pygame.font.Font(None, 36)
message = font.render("", True, (255))

while running:
    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if finish == False:
                handle_user_clicks(event.pos[0], event.pos[1], sign)

                if win_condition_checker(grid, sign):
                    finish = True
                    if sign == "X":
                        message = font.render("Player1 has won", True, (255, 0, 0))
                    else:
                        message = font.render("Player2 has won", True, (00, 255, 0))
                elif draw_condition_checker(grid):
                    finish = True
                    message = font.render("Draw!", True, (0, 0, 255))

                # sign flipper
                if sign == "X":
                    sign = "O"
                else:
                    sign = "X"
    

    
    
    # draw
    draw_grid(grid)
    
    
    screen.blit(message, (SCREEN_WIDTH//2-message.get_width()//2, SCREEN_HEIGHT//2-message.get_height()//2))

    pygame.display.flip()
    clock.tick(fps)