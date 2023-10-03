import sys
import pygame as pg
import random


WIDTH, HEIGHT = 800, 600


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    bb = pg.Surface((20, 20))
    pg.draw.circle(bb, (255, 0, 0), (10, 10), 10)
    bb_rct=bb.get_rect()#surfaceからrect抽出
    x=random.randint(0,WIDTH)
    y=random.randint(0,HEIGHT)
    bb_rct.center=(x,y)#rectにランダムな座標を設定する
    bb.set_colorkey((0, 0, 0))

    clock = pg.time.Clock()
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return

        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, [400, 200])
        screen.blit(bb, bb_rct)
        pg.display.update()
        tmr += 1
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()