import pygame

pygame.init()

display_width = 1800
display_height = 900

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
orange = (255, 165, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (255, 0, 255)

city_attr = {
    # Blue
    'San Francisco': ['Blue', (0, 0), ['Tokyo', 'Manila', 'Los Angeles', 'Chicago']],
    'Chicago': ['Blue', (0, 0), ['Los Angeles', 'Mexico City', 'Atlanta', 'Montreal']],
    'Montreal': ['Blue', (0, 0), ['Chicago', 'Washington', 'New York']],
    'Atlanta': ['Blue', (0, 0), ['Chicago', 'Washington', 'Miami']],
    'New York': ['Blue', (0, 0), ['Montreal', 'Washington', 'London', 'Madrid']],
    'Washington': ['Blue', (0, 0), ['New York', 'Montreal', 'Atlanta', 'Miami']],
    'Madrid': ['Blue', (0, 0), ['New York', 'London', 'Paris', 'Algiers', 'Sao Paulo']],
    'London': (320, 320),
    'Paris': (230, 230),
    'Essen': (310, 310),
    'Milan': (280, 280),
    'St. Petersburg': (300, 300),

    # Yellow
    'Los Angeles': (250, 250),
    'Mexico City': (330, 330),
    'Miami': (390, 390),
    'Bogota': (380, 380),
    'Lima': (10, 10),
    'Santiago': (10, 10),
    'Buenos Ares': (460, 460),
    'Sao Paulo': (410, 410),
    'Lagos': (440, 440),
    'Kinshasa': (450, 450),
    'Khartoum': (370, 370),
    'Johannesburg': (10, 10),

    # Black
    'Algiers': (210, 210),
    'Istanbul': (160, 160),
    'Moscow': (240, 240),
    'Tehran': (140, 140),
    'Baghdad': (110, 110),
    'Cairo': (170, 170),
    'Riyadh': (190, 190),
    'Karachi': (100, 100),
    'Delhi': (60, 60),
    'Kolkata': (50, 50),
    'Chennai': (40, 40),
    'Mumbai': (130, 130),

    # Red
    'Hong Kong': (20, 20),
    'Bangkok': (30, 30),
    'Ho Chi Minh City': (70, 70),
    'Manila': (80, 80),
    'Jakarta': (90, 90),
    'Taipei': (120, 120),
    'Shanghai': (150, 150),
    'Sydney': (180, 180),
    'Tokyo': (220, 220),
    'Seoul': (290, 290),
    'Osaka': (340, 340),
    'Beijing': (350, 350),
}

# medic_pawn_img = pygame.image.load('medic_pawn.png')

# pawn_info = ['Name', 'City', [city_cards]]
medic_info = ['Medic', 'Atlanta', []]
medic_info[2].append('string')
for item in medic_info:
    print(item)

gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Pandemic Simulator v1.0')
clock = pygame.time.Clock()


def draw_pawn(coords):
    pass
    # gameDisplay.blit(medic_pawn_img, coords)


def get_city_coords(city):
    return city_attr[city][2]


def game_loop():

    game_exit = False
    # lost = False

    while not game_exit:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('User exited')
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_LEFT:
                    # TODO
                    print('Left key press')
                if event.type == pygame.K_RIGHT:
                    # TODO
                    print('Right key press')

            print(event)

        # Update locations
        draw_pawn(get_city_coords(medic_info[1]))

        # Resolve logic

        # Update the display
        pygame.display.update()
        clock.tick(60)

game_loop()
