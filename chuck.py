import pygame
import random

pygame.init()

def toss():
    """ toss controlls all the events which happens after the button press or space"""
    pygame.draw.rect(appWindow,  appColor, [coin_x + 50, coin_y - 30, 100, 40])
    toss_ = random.randint(0, 1)

    # play sound
    try:
        pygame.mixer.music.play()
    except:
        pass

    # Running animation
    for coin_frame in toss_animation:
        appWindow.blit(coin_frame, (coin_x, coin_y))
        pygame.display.update()
        clock.tick(15)

    # Showing the result
    if toss_:
        face = coin_heads_image
        text_face = "heads"

    else:
        face = coin_tails_image
        text_face = "  tails"

    appWindow.blit(face, (coin_x, coin_y))

    show_text = pygame.font.SysFont(None, 50).render(text_face, True, black)
    appWindow.blit(show_text, (coin_x + 50, coin_y - 30))
    pygame.display.update()

# Game Variables
screen_width = 700
screen_height = 500
game_exit = False
font = pygame.font.SysFont(None, 50)

    # Coin
coin_x = screen_width/2 - 120
coin_y = screen_height/2 - 120

    # Color
white = (225, 225, 225)
black = (0, 0, 0)
gray = (249, 83, 53)
green = (0, 204, 102)
appColor = (77, 208, 225)

    # button
button_x = screen_width/2 - 63
button_y = 3*(screen_height/4)

    # Clock
clock = pygame.time.Clock()
fps = 15

# toss sound
toss_sound = "toss_sound.mp3"
pygame.mixer.init()
try:
    pygame.mixer.music.load(toss_sound)
except:
    print("For sound, open cmd in current directory")

# Loading all images for Toss Animation
image_count = 26
toss_animation = []
for i in range(image_count):
    image = pygame.image.load(f"toss_animation\\frame_{i}_delay-0.1s.gif")
    toss_animation.append(image)

del image

coin_heads_image = toss_animation[25]
coin_tails_image = toss_animation[0]

# Making window
appWindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("CHUCK")
appWindow.fill(appColor)

    # Button in window to flip
text = pygame.font.SysFont(None, 30).render("FLIP AGAIN", True, white)
appWindow.blit(text, [button_x, button_y])

appWindow.blit(coin_heads_image, (coin_x, coin_y))
pygame.display.update()

# Creating an app loop
while not game_exit:
    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(event)
            game_exit = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_x <= mouse[0] <= button_x+120 and button_y <= mouse[1] <= button_y+40:
                toss()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                toss()
      
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()
