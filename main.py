# import random
# import neat
# # import neat.config
# import os 
# import pygame
# pygame.init()
# pygame.font.init()

# FONT = pygame.font.SysFont("sanasarif",30)
# WIN_WIDTH = 500


# class MoonSurface:
#     LANDING_X1=  0
#     LANDING_Y1=  0
#     LANDING_X2=  0
#     LANDING_Y2=  0
#     def __init__(self,min,max,total_points): # considering the min to be the lowest part and the max to be top part
#         points = []
#         x = 0
#         num_points = (total_points - 2)//2
#         for i in range(num_points):
#             y = random.randint(min,max)
#             points.append((x,y))
#             x += WIN_WIDTH / total_points
        
#         y = random.randint(min,max)
#         points.append((x,y))
#         self.LANDING_X1 = x 
#         self.LANDING_Y1 = y


#         x += WIN_WIDTH / total_points + 8
#         points.append((x,y))
#         self.LANDING_X2 = x 
#         self.LANDING_Y2 = y

#         for i in range(num_points+2,total_points):
#             y = random.randint(min,max)
#             points.append((x,y))
#             x += WIN_WIDTH / total_points
        
#         points.append((WIN_WIDTH,WIN_WIDTH))
#         points.insert(0,(0,WIN_WIDTH))
        
#         self.points = points
    
#     def draw(self,win):
#         pygame.draw.polygon(win,(127, 127, 127),self.points)
#         pygame.draw.circle(win,"red",(self.LANDING_X1,self.LANDING_Y1),5)
#         pygame.draw.circle(win,"red",(self.LANDING_X2,self.LANDING_Y2),5)

#     def get_mask(self):
#         mask_surface = pygame.Surface((WIN_WIDTH, WIN_WIDTH), pygame.SRCALPHA)
#         pygame.draw.polygon(mask_surface, (255, 255, 255), self.points)
#         mask = pygame.mask.from_surface(mask_surface)
#         return mask

# class SpaceShip:
#     CURRENT_X = 0
#     CURRENT_Y = 0
#     LEFT_THRUST = 20 
#     RIGHT_THRUST = 20
#     UP_THRUST = 20

#     def __init__(self,Win,y,Heigh_Space_Ship,Width_Spcae_Ship):
#         self.CURRENT_X = random.randint(50,500-50) 
#         self.CURRENT_Y = y
#         self.height = Heigh_Space_Ship
#         self.width = Width_Spcae_Ship
#         self.Win = Win
        

#     def draw(self):
#         self.rect = pygame.Rect(self.CURRENT_X,self.CURRENT_Y,self.width,self.height)
#         pygame.draw.rect(self.Win,("red"),self.rect)

#     def gravity(self,g_value):
#         self.CURRENT_Y += g_value

#     def get_mask(self):
#         ship_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
#         pygame.draw.rect(ship_surface, (255, 255, 255), (0, 0, self.width, self.height))
#         mask = pygame.mask.from_surface(ship_surface)
#         return mask
        
#     def thrust(self):
#         self.CURRENT_Y -= self.UP_THRUST
    
#     def left_thrust(self):
#         self.CURRENT_X -= self.LEFT_THRUST

#     def right_thrust(self):
#         self.CURRENT_X += self.RIGHT_THRUST
# GEN = 0
# def main_Game(genomes,config):
#     SCORE = 0
#     screen = pygame.display.set_mode((WIN_WIDTH,WIN_WIDTH))
#     pygame.display.set_caption("Moon Lander Game")
    
#     clock = pygame.time.Clock()
#     surface_generator = MoonSurface(400,490,8)
#     # space_ship = SpaceShip(screen,40,60,50)
#     spcaeships = []
#     ge = []
#     nets = []

#     for genome_id, genome in genomes:
#         spcaeships.append(SpaceShip(screen,40,60,50))
#         ge.append(genome)
#         net = neat.nn.FeedForwardNetwork.create(genome,config)
#         nets.append(net)
#         genome.fitness = 0 


#     moon_mask = surface_generator.get_mask()

#     while True:
#         screen.fill((0, 0, 0))
        
#         # font = FONT.render(f"Score: {SCORE}",1,(255,255,255))
#         # screen.blit(font,(10,10))

#         font = FONT.render(f"Score: {GEN+1}",1,(255,255,255))
#         screen.blit(font,(10,10))
        
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 exit()
         

#         surface_generator.draw(screen)
        

#         #checking collisions
#         for i, space_ship in enumerate(spcaeships):
#             space_ship.draw()
#             spaceship_mask = space_ship.get_mask()
#             offset = (int(space_ship.CURRENT_X), int(space_ship.CURRENT_Y))
#             if moon_mask.overlap(spaceship_mask, offset):
#                 if space_ship.CURRENT_X > surface_generator.LANDING_X1 and space_ship.CURRENT_X < surface_generator.LANDING_X2:
#                     print("Successfull landing")
#                     space_ship.gravity(0)
#                     SCORE += 1
#                     #fitness increase
#                     ge[i].fitness += 30
#                 else:
#                     print("Crash Landing")
#                     #fitness decrease
#                     spcaeships.pop(i)
#                     ge.pop(i)
#                     nets.pop(i)
#             else: 
#                 space_ship.gravity(1)
               
#                 output = nets[i].activate((space_ship.CURRENT_X,space_ship.CURRENT_Y,surface_generator.LANDING_X1,surface_generator.LANDING_X2))
#                 if output[0] > 0.5:
#                     space_ship.left_thrust()
#                 else:
#                     space_ship.right_thrust()

        
#         # print(space_ship.CURRENT_X,surface_generator.LANDING_X1,surface_generator.LANDING_X2)
#         pygame.display.update()
#         clock.tick(60)


# # main_Game()

# def run(config_path):
#     config = neat.Config(
#         neat.DefaultGenome, 
#         neat.DefaultReproduction,
#         neat.DefaultSpeciesSet,
#         neat.DefaultStagnation,
#         config_path
#     )

#     pop = neat.Population(config)
#     pop.run(main_Game,50)

# if __name__ == "__main__":
#     path = os.path.dirname(__file__)
#     con_path = os.path.join(path,"config.txt")
#     run(config_path=con_path)

import random
import neat
import os 
import pygame

pygame.init()
pygame.font.init()

FONT = pygame.font.SysFont("sans-serif", 30)
WIN_WIDTH = 500
WIN_HEIGHT = 500

class MoonSurface:
    LANDING_X1 = 0
    LANDING_Y1 = 0
    LANDING_X2 = 0
    LANDING_Y2 = 0

    def __init__(self, min, max, total_points): # considering the min to be the lowest part and the max to be top part
        points = []
        x = 0
        num_points = (total_points - 2) // 2
        for i in range(num_points):
            y = random.randint(min, max)
            points.append((x, y))
            x += WIN_WIDTH / total_points
        
        y = random.randint(min, max)
        points.append((x, y))
        self.LANDING_X1 = x 
        self.LANDING_Y1 = y

        x += WIN_WIDTH / total_points + 8
        points.append((x, y))
        self.LANDING_X2 = x 
        self.LANDING_Y2 = y

        for i in range(num_points + 2, total_points):
            y = random.randint(min, max)
            points.append((x, y))
            x += WIN_WIDTH / total_points
        
        points.append((WIN_WIDTH, WIN_HEIGHT))
        points.insert(0, (0, WIN_HEIGHT))
        
        self.points = points
    
    def draw(self, win):
        pygame.draw.polygon(win, (127, 127, 127), self.points)
        pygame.draw.circle(win, "red", (self.LANDING_X1, self.LANDING_Y1), 5)
        pygame.draw.circle(win, "red", (self.LANDING_X2, self.LANDING_Y2), 5)

    def get_mask(self):
        mask_surface = pygame.Surface((WIN_WIDTH, WIN_HEIGHT), pygame.SRCALPHA)
        pygame.draw.polygon(mask_surface, (255, 255, 255), self.points)
        mask = pygame.mask.from_surface(mask_surface)
        return mask

class SpaceShip:
    LEFT_THRUST = 20 
    RIGHT_THRUST = 20
    UP_THRUST = 20

    def __init__(self, win, y, height, width):
        self.CURRENT_X = random.randint(50, WIN_WIDTH - 50) 
        self.CURRENT_Y = y
        self.height = height
        self.width = width
        self.win = win
        self.rect = pygame.Rect(self.CURRENT_X, self.CURRENT_Y, self.width, self.height)
        self.is_landed = False
        self.crashed = False

    def draw(self):
        self.rect = pygame.Rect(self.CURRENT_X, self.CURRENT_Y, self.width, self.height)
        pygame.draw.rect(self.win, "red", self.rect)

    def gravity(self, g_value):
        self.CURRENT_Y += g_value

    def get_mask(self):
        ship_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        pygame.draw.rect(ship_surface, (255, 255, 255), (0, 0, self.width, self.height))
        mask = pygame.mask.from_surface(ship_surface)
        return mask
        
    def thrust(self):
        self.CURRENT_Y -= self.UP_THRUST
    
    def left_thrust(self):
        self.CURRENT_X -= self.LEFT_THRUST

    def right_thrust(self):
        self.CURRENT_X += self.RIGHT_THRUST

def main_Game(genomes, config):
    SCORE = 0
    screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption("Moon Lander Game")
    
    clock = pygame.time.Clock()
    surface_generator = MoonSurface(400, 490, 8)
    spaceships = []
    ge = []
    nets = []

    for genome_id, genome in genomes:
        spaceships.append(SpaceShip(screen, 40, 60, 50))
        ge.append(genome)
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        genome.fitness = 0 

    moon_mask = surface_generator.get_mask()
    running = True

    while running and len(spaceships) > 0:
        screen.fill((0, 0, 0))
        
        font = FONT.render(f"Score: {SCORE}", 1, (255, 255, 255))
        screen.blit(font, (10, 10))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        surface_generator.draw(screen)

        for i in range(len(spaceships) - 1, -1, -1):
            space_ship = spaceships[i]
            space_ship.draw()
            spaceship_mask = space_ship.get_mask()
            offset = (int(space_ship.CURRENT_X), int(space_ship.CURRENT_Y))

            if moon_mask.overlap(spaceship_mask, offset):
                if not space_ship.is_landed and not space_ship.crashed:
                    if (space_ship.CURRENT_X > surface_generator.LANDING_X1 and 
                        space_ship.CURRENT_X < surface_generator.LANDING_X2):
                        print("Successful landing")
                        SCORE += 1
                        ge[i].fitness += 30
                        space_ship.is_landed = True
                    else:
                        print("Crash Landing")
                        ge[i].fitness -= 1
                        space_ship.crashed = True
                        spaceships.pop(i)
                        ge.pop(i)
                        nets.pop(i)
            else: 
                space_ship.gravity(1)
               
            if not space_ship.is_landed and not space_ship.crashed:
                output = nets[i].activate((space_ship.CURRENT_X, space_ship.CURRENT_Y, 
                                           surface_generator.LANDING_X1, surface_generator.LANDING_X2))
                if output[0] > 0.5:
                    space_ship.left_thrust()
                else:
                    space_ship.right_thrust()
        
        pygame.display.update()
        clock.tick(60)
        
        # Check if all spaceships have landed or crashed
        if all(space_ship.is_landed or space_ship.crashed for space_ship in spaceships):
            running = False

def run(config_path):
    config = neat.Config(
        neat.DefaultGenome, 
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        config_path
    )

    pop = neat.Population(config)
    pop.run(main_Game, 50)

if __name__ == "__main__":
    path = os.path.dirname(__file__)
    con_path = os.path.join(path, "config.txt")
    run(config_path=con_path)
