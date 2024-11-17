import pygame
from constants import *

def main():
	if __name__ == "__main__":
		print("Starting asteroids!")
		print(f"Screen width: {SCREEN_WIDTH}")
		print(f"Screen height: {SCREEN_HEIGHT}")
		screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
		while(1 == 1):
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return
			screen.fill(000000)
			

main()
