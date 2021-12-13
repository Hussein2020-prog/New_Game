import pygame
pygame.init()
pygame.display.set_caption("====( NewGame )====")
#===========Main Options================
screenW = 1360
screenH = 700
BLACK   = (0,0,0)
RED     = (255,0,0)
GREEN   = (0,255,0)
BLUE    = (0,0,255)
FONT    = pygame.font.SysFont("ubuntu",30,True)
SCORE   = 0
screen  = pygame.display.set_mode((screenW,screenH))
BGIMA   = pygame.image.load("images/bob.png")
PLAYIM  = pygame.image.load("images/plan1.png")
ARMYIM  = pygame.image.load("images/rocket.png")
SOUNDS  = pygame.mixer.Sound("sounds/111.wav")
BULLET  = pygame.mixer.Sound("sounds/Bullet1.wav")
# ===============Classes=======================================
class player:
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.hitbox = (self.x -15,self.y -2,self.h -10,self.w -30)
    #=======Draw Player Function===============================
    def DrawPlayer(self):
        self.hitbox = (self.x,self.y,self.h,self.w)
        screen.blit(PLAYIM,(self.x,self.y))
        pygame.draw.rect(screen,GREEN,(self.x -15,self.y -2,self.h -10,self.w -30),2)

class Army:
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.hitbox = (self.x -15,self.y -2,self.h -10,self.w -30)

    # =======Draw Army Function===============================
    def DrawArmy(self):
        self.hitbox = (self.x,self.y,self.h,self.w)
        screen.blit(ARMYIM,(self.x,self.y))
        pygame.draw.rect(screen,BLACK,(self.x -15,self.y -2,self.h -10,self.w -30),2)
#=========Objects============================================
player1 = player(10,10,64,64)
player2 = player(30,80,64,64)
player3 = player(50,150,64,64)
player4 = player(70,220,64,64)
player5 = player(90,290,64,64)

player6 = player(110,10,64,64)
player7 = player(130,80,64,64)
player8 = player(150,150,64,64)
player9 = player(170,220,64,64)
player10 = player(190,290,64,64)
player11 = player(200,290,64,64)
#-----------------------------
Army1   = Army(screenW // 2,650,64,64)
#===StartGame Function=======================================
def StartGame():
    TEXT = FONT.render("Score : " + str(SCORE),True,GREEN)
    screen.blit(BGIMA,(0,0))
    screen.blit(TEXT,(1200,40))
    player1.DrawPlayer()
    player2.DrawPlayer()
    player3.DrawPlayer()
    player4.DrawPlayer()
    player5.DrawPlayer()

    player6.DrawPlayer()
    player7.DrawPlayer()
    player8.DrawPlayer()
    player9.DrawPlayer()
    player10.DrawPlayer()
    player11.DrawPlayer()

    Army1.DrawArmy()
    pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    if player1.x + player1.x > screenW  and player1.x > 0:
        player1.x += 50




#===Main Loop==========================
    player1.x += 70
    player2.x += 66
    player3.x += 77
    player4.x += 18
    player5.x += 99
    player6.x += 199
    player7.x += 111
    player8.x += 121
    player9.x += 123
    player10.x += 14
    player11.x += 105
    #SOUNDS.play()
    SCORE += 1
    StartGame()
