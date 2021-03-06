import pygame, sys
from other_objects import *

WIN_W = 1600
WIN_H = 900
def lose(cur_level, hero):
    pygame.mixer.music.stop()

    try:
        pygame.mixer.music.load("Sounds/losesound.wav")
        pygame.mixer.music.play(-1)
    except pygame.error:
        pass
    screen = pygame.display.set_mode((WIN_W, WIN_H), pygame.SRCALPHA)
    clock = pygame.time.Clock()

    lose = hub_go = True
    game_over = Regular_Text(100, BLACK, (screen.get_rect().centerx, screen.get_rect().centery/2), "GAME OVER")
    retry = Click_Button(40, BLACK, LIGHT_GREY, (screen.get_rect().centerx/2, screen.get_rect().centery), "Retry", False)
    apartment = Click_Button(40, BLACK, LIGHT_GREY, (screen.get_rect().centerx, screen.get_rect().centery), "Back to Apartment", False)
    exit_game = Click_Button(40, BLACK, LIGHT_GREY, (screen.get_rect().centerx * 1.5, screen.get_rect().centery), "Exit Game", sys.exit)
    
    regular_button_group = pygame.sprite.Group()
    regular_button_group.add(game_over)
    click_button_group = pygame.sprite.Group()
    click_button_group.add(retry, apartment, exit_game)
    
    fade_in_screen = pygame.Surface((WIN_W, WIN_H))
    fade_in_screen.set_alpha(255)

    while lose and hub_go:
        clock.tick(60)
        screen.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            for c in click_button_group:
                c.update(screen, event)

            lose = retry.stay
            hub_go = apartment.stay

        for c in click_button_group:
            c.TextBlit(screen)
        for r in regular_button_group:
            r.update(screen)

        screen.blit(fade_in_screen, (0, 0))
        if fade_in_screen.get_alpha() != 0:
            fade_in_screen.set_alpha(fade_in_screen.get_alpha() - 3)
        pygame.display.flip()

    if retry.stay == False:     #Retrys the mission
        cur_level(True)
        hero.dead = True
        hero.menu = True
    if hub_go == False:         #Returns to the Apartment
        hero.dead = True
        hero.menu = True


