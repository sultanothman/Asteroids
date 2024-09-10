import circleshape
import pygame

from constants import PLAYER_RADIUS, PLAYER_DRAW_LINE_WIDTH, PLAYER_TURN_SPEED

class Player(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(
            screen, 
            (255, 255, 255), 
            self.triangle(),
            PLAYER_DRAW_LINE_WIDTH
            )
    def update(self, dt):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        #if keys[pygame.K_w]:

        #if keys[pygame.K_s]:


    def rotate(self, dt):
        self.rotation += dt * PLAYER_TURN_SPEED