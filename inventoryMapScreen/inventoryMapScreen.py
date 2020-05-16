import os

def display(inventory, heroLocationName, heroLocationId, rooms):
    selection = -1

    while selection != ' ':
        os.system('clear')
        print()
        print(' ', end='      ')
        inventory.show_inventory_map_screen()
        print()
        print('       You are currently in the {}'.format(heroLocationName))

        if heroLocationId < 8 or heroLocationId == 20:
            printMap(1, rooms)
        elif heroLocationId >= 8 and heroLocationId < 13 or heroLocationId == 22:
            printMap(2, rooms)
        elif heroLocationId == 13:
            printMap(3, rooms)
        elif heroLocationId > 13 and heroLocationId < 18:
            printMap(4, rooms)
        elif heroLocationId > 17 and heroLocationId < 20:
            printMap(6, rooms)
        else:
            printMap(5, rooms)

        print('\n\n')

        selection = input('       press \'enter\' to return to the game... ')
        selection = ' ' + selection

    # Having reached this point, selection matches. Clear screen to get ready to return to the game
    os.system('clear')

def printMap(mapChoice, rooms):
    first_floor = """
       ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
       ▒                                                                                                             ▒
       ▒                                                  First Floor                                                ▒
       ▒                                                                                                             ▒
       ▒            ---------------                                   ^                                              ▒
       ▒          /                 \\                                / \\                                             ▒
       ▒         /                   \\                                |                                              ▒
       ▒        /      Solarium       \\                               |                                              ▒
       ▒       /                       \\                    To Gardens and Gazebo                                    ▒
       ▒      /__________|  |___________\\___________________________|  |______________________________________       ▒
       ▒     |                               |                                    |                           |      ▒
       ▒     |                               |                                    --                          |      ▒
       ▒     |          Game Room            |      __|        Kitchen                                        |      ▒
       ▒     |                               |   __|                              --                          |      ▒
       ▒     |                               |  |  Stairs (to cellar)             |                           |      ▒
       ▒     |                 ____________________________________________________            Dining         |      ▒
       ▒     |                --                    |                             |             Room          |      ▒
       ▒     |                        Bathroom      |                 __          |                           |      ▒
       ▒     |                --                    |              __|            |                           |      ▒
       ▒     |__________|   |__|______________|   |_|           __|               |                           |      ▒
       ▒     |                               |               __| Grand            |                           |      ▒
       ▒     |                               |              |   Staircase         |                           |      ▒
       ▒     |                               |                                    |____________|    |_________|      ▒
       ▒     |                               --                                   |                           |      ▒
       ▒     |           Library                                                  |                           |      ▒
       ▒     |                               --                                   --                          |      ▒
       ▒     |                               |                                                 Parlor         |      ▒
       ▒     |                               |              Foyer                 --                          |      ▒
       ▒     |                               |                                    |                           |      ▒
       ▒     |_______________________________|_____________|      |_______________|___________________________|      ▒
       ▒                    |                                                               |                        ▒
       ▒                    |                               Porch                           |                        ▒
       ▒                    |                                                               |                        ▒
       ▒                    |____________________________|          |_______________________|                        ▒
       ▒                                                To Front Lawns                                               ▒
       ▒                                                      |                                                      ▒
       ▒                                                      |                                                      ▒
       ▒                                                     \\ /                                                     ▒
       ▒                                                      v                                                      ▒
       ▒                                                                                                             ▒
       ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒"""

    attic_base_state = """
       ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
       ▒                                                                                                             ▒
       ▒                        Attic                                                                                ▒
       ▒                                                                                                             ▒
       ▒                     ___________________________________________________________________                     ▒
       ▒                     |                                                                 |                     ▒
       ▒                     |             __|                                                 |                     ▒
       ▒                     |          __|                                                    |                     ▒
       ▒                     |       __|  Stairs                                               |                     ▒
       ▒                     |      |    (to 2nd Floor)                                        |                     ▒
       ▒                     |                                                                 |                     ▒
       ▒                     |                                                                 |                     ▒
       ▒                     |                                                                 |                     ▒
       ▒                     |                                                                 |                     ▒
       ▒                     |                                                                 |                     ▒
       ▒                     |                                                                 |                     ▒
       ▒                     |                                                                 |                     ▒
       ▒                     |                                                                 |                     ▒
       ▒                     |                                                                 |                     ▒
       ▒                     |                                                                 |                     ▒
       ▒                     |                                                                 |                     ▒
       ▒                     |_________________________________________________________________|                     ▒
       ▒                                                                                                             ▒
       ▒                                                                                                             ▒
       ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒"""

    attic_revealed = """
       ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
       ▒                                                                                                             ▒
       ▒                        Attic                                                                                ▒
       ▒                                                                                                             ▒
       ▒                     ___________________________________________________________________                     ▒
       ▒                     |                                                                 |                     ▒
       ▒                     |             __|                                                 |                     ▒
       ▒                     |          __|                                                    |                     ▒
       ▒                     |       __|  Stairs                                               |                     ▒
       ▒                     |      |    (to 2nd Floor)                                        |                     ▒
       ▒                     |                                                                 |                     ▒
       ▒                     |                                                                 |                     ▒
       ▒                     |                                                                 |                     ▒
       ▒                     |                                                                 |                     ▒
       ▒                     |                                                                 |                     ▒
       ▒                     |                                                 ----------------|                     ▒
       ▒                     |                                                |                |                     ▒
       ▒                     |                                                |                |                     ▒
       ▒                     |                                                |      Hidden    |                     ▒
       ▒                     |                                                |       Room     |                     ▒
       ▒                     |                                                |                |                     ▒
       ▒                     |________________________________________________|________________|                     ▒
       ▒                                                                                                             ▒
       ▒                                                                                                             ▒
       ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒"""

    gardens_base_state = """
       ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
       ▒                                                                                                             ▒
       ▒                                                                                                             ▒
       ▒                                          Gardens and Gazebo                                                 ▒
       ▒                                                                                                             ▒
       ▒                                                                                                             ▒
       ▒                     __________________________                       ---------------                        ▒
       ▒                    |                          |                    /                 \                      ▒
       ▒                    |                          |                   /                   \                     ▒
       ▒                    |                          |                  /                     \                    ▒
       ▒                    |          Rose            |                 |                       |                   ▒
       ▒                    |         Gardens          |                 |        Gazebo         |                   ▒
       ▒                    |                          |                 |                       |                   ▒
       ▒                    |                          |                  \                     /                    ▒
       ▒                    |                          |                   \                   /                     ▒
       ▒                    |                          |                    \                 /                      ▒
       ▒                    |__________________________|                      ---------------                        ▒
       ▒                                                                                                             ▒
       ▒                                                                                                             ▒
       ▒                                             -----------                                                     ▒
       ▒                                            |           |                                                    ▒
       ▒                                            | Fountain  |                                                    ▒
       ▒                           To Rear          |           |                                                    ▒
       ▒                           of House         |           |                                                    ▒
       ▒                              |              -----------                                                     ▒
       ▒                              |                                                                              ▒
       ▒                              |                                                                              ▒
       ▒                            \\  /                                                                             ▒
       ▒                              v                                                                              ▒
       ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒"""

    gardens_revealed = """
       ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
       ▒                                                                                                             ▒
       ▒                                                                                                             ▒
       ▒                                          Gardens and Gazebo                                                 ▒
       ▒                                                                                                             ▒
       ▒                                                                                                             ▒
       ▒                     __________________________                       ---------------                        ▒
       ▒                    |                          |                    /                 \                      ▒
       ▒                    |                          |                   /                   \                     ▒
       ▒                    |                          |                  /                     \                    ▒
       ▒                    |          Rose            |                 |                       |                   ▒
       ▒                    |         Gardens          |                 |        Gazebo         |                   ▒
       ▒                    |                          |                 |                       |                   ▒
       ▒                    |                          |                  \                     /                    ▒
       ▒                    |                          |                   \                   /                     ▒
       ▒                    |                          |                    \                 /                      ▒
       ▒                    |__________________________|                      ---------------                        ▒
       ▒                                                                        |         |                          ▒
       ▒                                                                        |         |                          ▒
       ▒                                             -----------                |  Dark   |                          ▒
       ▒                                            |           |               | Tunnel  |                          ▒
       ▒                                            | Fountain  |               |         |                          ▒
       ▒                           To Rear          |           |               |         |                          ▒
       ▒                           of House         |           |               |         |                          ▒
       ▒                              |              -----------                |         |                          ▒
       ▒                              |                                         |         |                          ▒
       ▒                              |                                         |         |                          ▒
       ▒                             \\ /                                        |         |                          ▒
       ▒                              v                                         |         |                          ▒
       ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒"""

    cellar_base_state = """
       ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
       ▒                                                                                                             ▒
       ▒                                                                                                             ▒
       ▒                                           Cellar                                                            ▒
       ▒     ______________________________________________________________________________________                  ▒
       ▒    |                                                                                      |                 ▒
       ▒    |-------                                               -----------------------------   |                 ▒
       ▒    |       |                       __                    |                             |  |                 ▒
       ▒    | Work  |                    __|                      |                             |  |                 ▒
       ▒    | Bench |                 __| Stairs                  |          Shelves            |  |                 ▒
       ▒    |       |                | (To 1st Floor)             |                             |  |                 ▒
       ▒    |       |                                             |                             |  |                 ▒
       ▒    |-------                                               -----------------------------   |                 ▒
       ▒    |__________________        ____________________________________________________________|                 ▒
       ▒    |                  |      |    |                      |                                |                 ▒
       ▒    |                              |                      |                                |                 ▒
       ▒    |                              --                     |                                |                 ▒
       ▒    |       Servant's                      Servant's      |                                |                 ▒
       ▒    |       Quarters               --      Bathroom       |                                |                 ▒
       ▒    |                              |                      |                                |                 ▒
       ▒    |______________________________|______________________|________________________________|                 ▒
       ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒"""

    cellar_revealed = """
       ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
       ▒                                                                                                             ▒
       ▒                                                                                               |        |    ▒
       ▒                                           Cellar                                              |  Dark  |    ▒
       ▒     ______________________________________________________________________________________    | Tunnel |    ▒
       ▒    |                                                                                      |   |        |    ▒
       ▒    |-------                                               -----------------------------   |   |        |    ▒
       ▒    |       |                       __                    |                             |  |   |        |    ▒
       ▒    | Work  |                    __|                      |                             |  |   |        |    ▒
       ▒    | Bench |                 __| Stairs                  |          Shelves            |  |   |        |    ▒
       ▒    |       |                | (To 1st Floor)             |                             |  |   |        |    ▒
       ▒    |       |                                             |                             |  |   |        |    ▒
       ▒    |-------                                               -----------------------------   |  /         |    ▒
       ▒    |__________________        ____________________________________________________________|/           /    ▒
       ▒    |                  |      |    |                      |                                .          /      ▒
       ▒    |                              |                      |                                .        /        ▒
       ▒    |                              --                     |                                .      /          ▒
       ▒    |       Servant's                      Servant's      |             Crypt              ._ _ /            ▒
       ▒    |       Quarters               --      Bathroom       |                                |                 ▒
       ▒    |                              |                      |                                |                 ▒
       ▒    |______________________________|______________________|________________________________|                 ▒
       ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒"""

    front_lawn_base_state = """
       ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
       ▒                                                                                                             ▒
       ▒                                                                                                             ▒
       ▒                                                Front Lawns                  ^                               ▒
       ▒                                                                            / \\                              ▒
       ▒                                                                             | To Front                      ▒
       ▒                                                                             | Of House                      ▒
       ▒                                                                             |                               ▒
       ▒                                _______________                                                              ▒
       ▒                               |               |                                                             ▒
       ▒                               |    Purple     |                          ----                               ▒
       ▒                               |    Flower     |                         |    |  large                       ▒
       ▒                               |    Garden     |                         |    |  tree                        ▒
       ▒                               |               |                          ----                               ▒
       ▒                               |_______________|                                                             ▒
       ▒                                                                                                             ▒
       ▒                            ---                                           ---                                ▒
       ▒                           |   |  tree                                   |   |  tree                         ▒
       ▒                            ---               |            |              ---                                ▒
       ▒                                              |            |                                                 ▒
       ▒                            ---               |            |              ---                                ▒
       ▒                           |   |  tree        |            |             |   |  tree                         ▒
       ▒                            ---               |            |              ---                                ▒
       ▒                                              |            |                                                 ▒
       ▒                                              |            |                                                 ▒
       ▒                                            Front Gate(Locked)                                               ▒
       ▒                           __________________..................______________________                        ▒
       ▒                                                                                                             ▒
       ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒"""

    front_lawn_with_grave = """
       ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
       ▒                                                                                                             ▒
       ▒                                                                                                             ▒
       ▒                                                Front Lawns                  ^                               ▒
       ▒                                                                            / \\                              ▒
       ▒                                                                             | To Front                      ▒
       ▒                                                                             | Of House                      ▒
       ▒                                                                             |                               ▒
       ▒                                _______________                                                              ▒
       ▒                               |               |                                                             ▒
       ▒                               |    Purple     |                          ----                               ▒
       ▒                               |    Flower     |              xxxxxx     |    |  large                       ▒
       ▒                               |    Garden     |       grave  x    x     |    |  tree                        ▒
       ▒                               |               |              xxxxxx      ----                               ▒
       ▒                               |_______________|                                                             ▒
       ▒                                                                                                             ▒
       ▒                            ---                                           ---                                ▒
       ▒                           |   |  tree                                   |   |  tree                         ▒
       ▒                            ---               |            |              ---                                ▒
       ▒                                              |            |                                                 ▒
       ▒                            ---               |            |              ---                                ▒
       ▒                           |   |  tree        |            |             |   |  tree                         ▒
       ▒                            ---               |            |              ---                                ▒
       ▒                                              |            |                                                 ▒
       ▒                                              |            |                                                 ▒
       ▒                                            Front Gate(Locked)                                               ▒
       ▒                           __________________..................______________________                        ▒
       ▒                                                                                                             ▒
       ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒"""

    second_floor = """
       ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
       ▒                                                                                                             ▒
       ▒                                                                                                             ▒
       ▒                                                Second Floor                                                 ▒
       ▒              _________________________________________________________________________________              ▒
       ▒             |                |                              |                                 |             ▒
       ▒             |                |            Pink Room         |                                 |             ▒
       ▒             |               --                              --                                |             ▒
       ▒             |    Red Room            __|                                 Green Room           |             ▒
       ▒             |               --    __|                       --                                |             ▒
       ▒             |                |   |   Stairs (to attic)      |                                 |             ▒
       ▒             |                |______________________________|_______                          |             ▒
       ▒             |                |    2nd Floor Landing                 |                         |             ▒
       ▒             |               --                   ___                --                        |             ▒
       ▒             |                                ___|                                             |             ▒
       ▒             |               --           ___|Grand Staircase        --                        |             ▒
       ▒             |                |          | (To 1st Floor/Attic)      |                         |             ▒
       ▒             |________________|                                      --------------------------|             ▒
       ▒             |                |              _____________           |                         |             ▒
       ▒             |  Linen        --             |             |          --      Bathroom          |             ▒
       ▒             |  Closet       --             |    Piano    |          --                        |             ▒
       ▒             |________________|_____________|_____________|__________|_________________________|             ▒
       ▒                                                                                                             ▒
       ▒                                                                                                             ▒
       ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒"""

    # Determine which map should be displayed to the user based on location and on room descriptions to determine player's progress in the game
    if mapChoice == 1:
        print(first_floor)
    if mapChoice == 2:
        print(second_floor)
    if mapChoice == 3:
        if rooms[13].long_des == 'You are standing in the Attic. Everything remains as it was with one exception: the boards around the walled in area have fallen exposing the entrance to a hidden room to the southeast.':
            print(attic_revealed)
        else:
            print(attic_base_state)
    if mapChoice == 4:
        if rooms[18].long_des == 'You have uncovered a tunnel under the gazebo....':
            print(cellar_revealed)
        else:
            print(cellar_base_state)
    if mapChoice == 5:
        if rooms[21].long_des == 'You are on the front lawns of the mansion. A grave is dug at the base of a tree. There is a flower garden nearby bordered in strange stone. You see the mansion to the North.' or rooms[21].long_des == 'You are on the front lawns of the mansion. The freshly filled grave is here. There are some gardens nearby bordered in strange stone. You see the mansion to the North.' or rooms[21].long_des == 'You are on the front lawns of the mansion. The grave grave is here, with the crying girl above, holding out her hand. There are some gardens nearby bordered in strange stone. You see the mansion to the North.':
            print(front_lawn_with_grave)
        else:
            print(front_lawn_base_state)
    if mapChoice == 6:
        if rooms[18].long_des == 'You have uncovered a tunnel under the gazebo....':
            print(gardens_revealed)
        else:
            print(gardens_base_state)
