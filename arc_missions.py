import sys
from other_objects import *
from arc_missionList import mission_list

def mission_screen(m, screen):                                                               #mission_goto initiates the level for the mission
    display_mission = Mission(screen, m[0], m[1],m[2], m[3], m[4], m[5])                     #Gives the displayed mission the properties it holds (screen, employer, building, difficulty, requirements, reward, mission_goto)
    exit = Click_Button(40, BLACK, LIGHT_GREY, (100, screen.get_rect().bottom - 100), "Missions", False)
    click_button_group = pygame.sprite.Group()
    click_button_group.add(exit)
    mission_screen_loop = True
    while mission_screen_loop:

        screen.fill(WHITE)
        for event in pygame.event.get():
            click_button_group.update(screen, event)
            display_mission.update(screen, event)
            mission_screen_loop = exit.stay
            if event.type == pygame.QUIT: sys.exit()

        display_mission.TextBlit(screen)
        exit.TextBlit(screen)

        pygame.display.update()


def missions(screen):



    exit = Click_Button(40, BLACK, LIGHT_GREY, (screen.get_rect().centerx, screen.get_rect().bottom - 100), "Main Menu", False)
    click_button_group = pygame.sprite.Group()
    click_button_group.add(exit)
    for m in range(len(mission_list)):                                                                           #The last argument here is the argument that needs to be passed into the button's next_screen method
        button = Click_Button(40, BLACK, LIGHT_GREY, (screen.get_rect().centerx, 50 + (50 * m)), "Mission " + str(m + 1), mission_screen, mission_list[m])
        click_button_group.add(button)

    mission_loop = True
    while mission_loop:

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            click_button_group.update(screen, event)
            mission_loop = exit.stay

        screen.fill(WHITE)
        for c in click_button_group:
            c.TextBlit(screen)

        pygame.display.update()
