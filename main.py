import pygame

WIDTH = 800
HEIGHT = 600

white = (255, 255, 255)

thuis = 0
thuisset = 0
uit = 0
uitset = 0

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
maaseik = pygame.image.load("maaseik.jpg")
maaseik = pygame.transform.smoothscale(maaseik,(200, 150))
Roeselare= pygame.image.load("roeselare.png")
Roeselare = pygame.transform.smoothscale(Roeselare,(200, 150))

font = pygame.font.SysFont("none", 40)

# Start de klok
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                running = False
            elif event.key == pygame.K_LEFT:
                thuis += 1
                if thuis >= 25:
                    if uit < thuis - 1:
                        thuis = 0
                        uit = 0
                        thuisset += 1
                if uitset == 2 and thuisset == 2:
                    if uit == 15:
                        if uit < thuis - 1:
                            thuisset += 1
            elif event.key == pygame.K_RIGHT:
                uit += 1
                if uit >= 25:
                    if thuis < uit - 1:
                        thuis = 0
                        uit = 0
                        uitset += 1
                if uitset == 2 and thuisset == 2:
                    if uit == 15:
                        if thuis < uit - 1:
                            uitset += 1
            elif event.key == pygame.K_r:
                thuis = 0
                thuisset = 0
                uit = 0
                uitset = 0
            elif event.key == pygame.K_s:
                print(text.get_width())
                print(text.get_height())

    if thuisset >= 4:
        if uitset < 2:
            print("De thuisploeg wint!")
    if thuisset == 3 and uitset == 2:
        print("De thuisploeg wint!")

    if uitset >= 4:
        if thuisset < 2:
            print("De uitploeg wint!")
    if uitset == 3 and thuisset == 2:
        print("De uitploeg wint!")

    screen.fill("white")


    screen.blit(maaseik, (100, 100))
    screen.blit(Roeselare, (500, 100))




    font = pygame.font.SysFont("comicsansms", 45)
    text = font.render(f"thuis: {thuis}", True, "black")
    h = text.get_height()
    w = text.get_width()
    screen.blit(text,(WIDTH/4-w/2 ,HEIGHT/1.5-h/2))

    font = pygame.font.SysFont("comicsansms", 45)
    text = font.render(f"uit: {uit}", True, "black")
    h = text.get_height()
    w = text.get_width()
    screen.blit(text, (WIDTH / 1.35 - w / 3, HEIGHT / 1.5 - h / 2))

    font = pygame.font.SysFont("comicsansms", 24)
    text = font.render(f"set {thuisset}", True, "black")
    h = text.get_height()
    w = text.get_width()
    screen.blit(text, (WIDTH / 4 - w / 3, HEIGHT / 1.25 - h / 2))

    font = pygame.font.SysFont("comicsansms", 24)
    text = font.render(f"set {uitset}", True, "black")
    h = text.get_height()
    w = text.get_width()
    screen.blit(text, (WIDTH / 1.35 - w / 3, HEIGHT / 1.25 - h / 2))



    pygame.display.flip()

    # Wacht zodanig dat we maximal 60 FPS halen
    clock.tick(60)
