from utils import *

SCREEN = pygame.display.set_mode((500, 500))


def main():
      while True:
            SCREEN.fill((255, 255, 255))
            for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
