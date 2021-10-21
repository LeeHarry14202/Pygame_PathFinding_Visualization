import pygame.display

from utils import *

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def init_gird(rows, cols, color):
      gird_ = np.empty((rows, cols), dtype = tuple)
      gird_.fill(color)
      return gird_ 

def draw_gird(screen):
    for i, row in enumerate(gird):
        for j, pixel in enumerate(row):
            pygame.draw.rect(screen, pixel, (j * PIXEL_SIZE, i * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))

    if DRAW_GIRD_LINES:
        # Add 1 to draw the last row
        for i in range(ROWS + 1):
            pygame.draw.line(screen, BLACK, start_pos=(0, i * PIXEL_SIZE),
                             end_pos=(SCREEN_WIDTH, i * PIXEL_SIZE))
        # Add 1 to draw the last col
        for j in range(COLS + 1):
            pygame.draw.line(screen, BLACK, start_pos=(j * PIXEL_SIZE, 0),
                             end_pos=(j * PIXEL_SIZE, SCREEN_HEIGHT - abs(SCREEN_HEIGHT - SCREEN_WIDTH)))



def draw(screen):
      screen.fill(BACKGROUND_COLOR)
      draw_gird(screen)
      pygame.display.update()


clock = pygame.time.Clock()
run = True
gird = init_gird(ROWS, COLS, GREEN)


def main():
      while run:
            for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

            draw(SCREEN)

            clock.tick(FPS)

if __name__ == "__main__":
      main()
