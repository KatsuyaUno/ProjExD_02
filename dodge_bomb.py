import sys
import time
import pygame as pg
import random


WIDTH, HEIGHT = 800, 600

def check_bound(obj_rct:pg.Rect):
    """
    引数:こうかとんRect or 爆弾rect
    戻り値:タプル(横方向判定結果、縦方向判定結果)
    画面内ならTrue,画面外ならFalse
    """
    yoko,tate=True,True
    if obj_rct.left<0 or WIDTH<obj_rct.right:
        yoko=False
    if obj_rct.top<0 or HEIGHT<obj_rct.bottom:
        tate=False
    return yoko,tate


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    end_img = pg.image.load("ex02/fig/1.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    end_img = pg.transform.rotozoom(end_img, 0, 2.5)
    bb = pg.Surface((20, 20))
    pg.draw.circle(bb, (255, 0, 0), (10, 10), 10)
    bb_rct=bb.get_rect()#surfaceからrect抽出
    kk_rct=kk_img.get_rect()#surfaceからrect抽出
    end_rct=end_img.get_rect()

    kk_rct.center=(450,200)
    end_rct.center=(450,250)
    x=random.randint(0,WIDTH)
    y=random.randint(0,HEIGHT)
    vx=+5
    vy=+5
    
    delta={#ren3移動量リスト
        pg.K_UP:(0,-5), 
        pg.K_DOWN:(0,+5),
        pg.K_LEFT:(-5,0),
        pg.K_RIGHT:(+5,0),
    }

    #ace=[a for a in range(1,11)]

    
    bb_rct.center=(x,y)#rectにランダムな座標を設定する
    bb.set_colorkey((0, 0, 0))

    clock = pg.time.Clock()
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
            
        if kk_rct.colliderect(bb_rct):#ren5爆弾と衝突したら

            screen.blit(bg_img, [0, 0])#追加機能3
            screen.blit(end_img,kk_rct)#追加機能3
            
            pg.display.update()
            time.sleep(2)
            print("game over")
            return

        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, kk_rct)#ren3移動量に応じて更新
        ########bomb###########
        bb_rct.move_ip(vx,vy)#ren2 爆弾を動かす
        yoko,tate=check_bound(bb_rct)
        if not yoko:#横方向にはみ出たら
            vx *= -1
        if not tate:#縦方向にはみ出たら
            vy *= -1
        
        #for r in range(1,11):
            #bb=pg.surface((20*r,20*r))
            #pg.draw.circle(bb,(255,0,0),(10*r,10*r),10*r)
            #bb.append(bb)
        screen.blit(bb, bb_rct)

        key_lst=pg.key.get_pressed()#key有効化
        sum_mv=[0,0]
        
        for key,mv in delta.items():#ren3key入力判断
            if key_lst[key]:
                sum_mv[0]+=mv[0]
                sum_mv[1]+=mv[1]
        kk_rct.move_ip(sum_mv)
        if check_bound(kk_rct) != (True ,True):
            kk_rct.move_ip(-sum_mv[0], -sum_mv[1])


        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()