"""
TicTacToe.py
A simple Pygame-based Tic Tac Toe game with arrow key navigation,
win detection, and a styled mobile-like interface.

Controls:
- Arrow Keys: Move cursor
- Space: Place X/O
- R: Restart game
- ESC: Quit
"""
import pygame
pygame.init()

W=360
screen=pygame.display.set_mode((W,W))
clock=pygame.time.Clock()
board=[0]*9; cur=4; turn=1; winner=0
font=pygame.font.Font(None,100)
small=pygame.font.Font(None,60)

def check_win():
    wins=[(0,1,2),(3,4,5),(6,7,8),
          (0,3,6),(1,4,7),(2,5,8),
          (0,4,8),(2,4,6)]
    for a,b,c in wins:
        if board[a]!=0 and board[a]==board[b]==board[c]:
            return board[a]
    if all(board): return 2  # draw
    return 0

def draw_shadow_rect(x,y,w,h,color,off=4):
    pygame.draw.rect(screen,(60,60,120),(x+off,y+off,w,h),border_radius=20)
    pygame.draw.rect(screen,color,(x,y,w,h),border_radius=20)

def draw():
    screen.fill((100,149,237))
    draw_shadow_rect(20,20,W-40,W-40,(255,255,255))
    cell=(W-40)//3
    # Grid
    for i in (1,2):
        pygame.draw.line(screen,(50,50,50),(20+i*cell,20),(20+i*cell,W-20),3)
        pygame.draw.line(screen,(50,50,50),(20,20+i*cell),(W-20,20+i*cell),3)
    # Marks
    for i,v in enumerate(board):
        if v:
            mark="X" if v==1 else "O"
            txt=font.render(mark,True,(30,30,30))
            r=i//3; c=i%3
            rect=txt.get_rect(center=(20+c*cell+cell//2,20+r*cell+cell//2))
            screen.blit(txt,rect)
    # Cursor
    if not winner:
        r,c=cur//3,cur%3
        pygame.draw.rect(screen,(200,60,60),(20+c*cell+5,20+r*cell+5,cell-10,cell-10),3,border_radius=10)
    # Win message
    if winner:
        # Draw a rounded rectangle backdrop for the header and message
        backdrop_rect = pygame.Rect(W//2-140, W//2-110, 280, 140)
        pygame.draw.rect(screen, (255,255,255), backdrop_rect, border_radius=15)
        pygame.draw.rect(screen, (60,60,120), backdrop_rect, 4, border_radius=15)
        # Render a large header "Game Over" above the result message
        header_font = pygame.font.Font(None, 80)
        header = header_font.render("Game Over", True, (20,20,20))
        hrect = header.get_rect(center=(W//2, W//2 - 60))
        screen.blit(header, hrect)
        if winner==2: msg="Draw!"
        else: msg=("X Wins!" if winner==1 else "O Wins!")
        txt=small.render(msg,True,(20,20,20))
        rect=txt.get_rect(center=(W//2,W//2))
        screen.blit(txt,rect)
    pygame.display.flip()

run=True
while run:
    for e in pygame.event.get():
        if e.type==pygame.QUIT: run=False
        if e.type==pygame.KEYDOWN:
            if e.key==pygame.K_ESCAPE: run=False
            if e.key==pygame.K_r: board=[0]*9;cur=4;turn=1;winner=0
            if not winner:
                if e.key==pygame.K_LEFT: cur=(cur-1)%9
                if e.key==pygame.K_RIGHT: cur=(cur+1)%9
                if e.key==pygame.K_UP: cur=(cur-3)%9
                if e.key==pygame.K_DOWN: cur=(cur+3)%9
                if e.key==pygame.K_SPACE and not board[cur]:
                    board[cur]=turn
                    winner=check_win()
                    turn*=-1
    draw(); clock.tick(30)

pygame.quit()