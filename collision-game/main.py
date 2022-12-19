import pygame
from sys import exit

pygame.init()

widthscreen = 1440 #middle 720
heightscreen = 790 #middle 395
w_surface = 800
h_surface = 500
midalignX_lg = (widthscreen-w_surface)/2
midalignY_lg = (heightscreen-h_surface)/2

#blue = player
#yellow = barrier

#game variable
collision_number = 0
converted_num = str(collision_number)

screen = pygame.display.set_mode((widthscreen,heightscreen))

pygame.display.set_caption("Collision Game")
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 45)


surface = pygame.Surface((w_surface,h_surface))
surface.fill('Light Yellow')

blue_b = pygame.image.load('images/blue.png').convert_alpha()
blue_b = pygame.transform.scale(blue_b,(35,35))

yellow_b = pygame.image.load('images/yellow.png').convert_alpha()
yellow_b = pygame.transform.scale(yellow_b,(35,35))

option_surf = test_font.render('Ball Option:', True, 'White')


score_surf = test_font.render('Score: ' + converted_num, True, 'White')
score_rect = score_surf.get_rect(center = (720,100))

barrier_1_x = 0
barrier_1_surf = pygame.image.load('images/yellow.png').convert_alpha()
barrier_1_surf = pygame.transform.scale(barrier_1_surf,(35,35))
barrier_1_rect =  barrier_1_surf.get_rect(center = (100, 350))

player_surf = pygame.image.load('images/blue.png').convert_alpha()
player_surf = pygame.transform.scale(player_surf,(35,35))
player_rect = player_surf.get_rect(center = (0,350))

A = False

while True:
    #elements & update
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # print('mouse down')
            mouse_pos = pygame.mouse.get_pos()
            rel_x = mouse_pos[0] - midalignX_lg
            rel_y = mouse_pos[1] - midalignY_lg
            if player_rect.collidepoint(rel_x, rel_y): print('collision')

        '''if event.type == pygame.MOUSEBUTTONUP:
            # print('mouse up')'''
    
    screen.blit(surface, (midalignX_lg,midalignY_lg))
    screen.blit(blue_b,(150,250))
    screen.blit(yellow_b, (150,300))
    screen.blit(option_surf,(150, 200))
    screen.blit(score_surf, score_rect)

    '''barrier_1_x += 3
    if barrier_1_x > 800: barrier_1_x = 0

    barrier_1_rect.x += 3
    if barrier_1_rect.x > 800:  barrier_1_rect.x = 0'''


    if A == False:
        barrier_1_rect.x -= 4
        if barrier_1_rect.right >= 820: barrier_1_rect.left = -5
        player_rect.x += 5
        if player_rect.right >= 810: player_rect.left = -10
    else:
        barrier_1_rect.x += 4
        if barrier_1_rect.right <= -5: barrier_1_rect.left = 810
        player_rect.x -= 5
        if player_rect.right <= -10: player_rect.left = 820
    

    surface = pygame.Surface((w_surface,h_surface))
    surface.fill('Light Yellow')
    surface.blit(barrier_1_surf, barrier_1_rect)
    surface.blit(player_surf, player_rect)


    if player_rect.colliderect(barrier_1_rect):
        print('player collided with barrier')

        if (player_rect.x < barrier_1_rect.x): A = True
        if (player_rect.x > barrier_1_rect.x): A = False

        collision_number += 1
    
    

    #below code is the same as in the event loop
    '''mouse_pos = pygame.mouse.get_pos()
    rel_x = mouse_pos[0] - midalignX_lg
    rel_y = mouse_pos[1] - midalignY_lg
    if player_rect.collidepoint(rel_x, rel_y):
        print(pygame.mouse.get_pressed())'''

    
    pygame.display.update()

    clock.tick(60)





    
