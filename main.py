import pygame
from player import Player
from constants import *
from asteroids import *
from asteroidfield import *
from circleshape import * 
clockObject = pygame.time.Clock()
def main():
	dt = 0
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	allAsteroids = pygame.sprite.Group()
	Asteroid.containers = (allAsteroids, updatable, drawable)
	Player.containers = (updatable,drawable)
	AsteroidField.containers = (updatable)
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	asteroidFieldObject = AsteroidField()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
	while(True):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill("black")
		for i in updatable:
			i.update(dt)
		for i in drawable:
			i.draw(screen)
		for i in allAsteroids:
			if(player.collisionCheck(i) == True):
				print("Game over!")
				return
		pygame.display.flip()
		dt = (clockObject.tick(60) / 1000)

if __name__ == "__main__":
	main()

