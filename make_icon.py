import os
from PIL import Image, ImageDraw
S=1024;K=2
os.makedirs('assets',exist_ok=True)
def bg():
    im=Image.new('RGB',(S,S));px=im.load()
    a=(88,70,255);b=(24,190,255)
    for y in range(S):
        for x in range(S):
            t=(x+y)/(2*S-2);px[x,y]=tuple(int(a[i]+(b[i]-a[i])*t) for i in range(3))
    return im
def fg():
    W=S*K;im=Image.new('RGBA',(W,W),(0,0,0,0));d=ImageDraw.Draw(im)
    rows=[('#ff5a5a',3),('#ff9f43',2),('#ffd93d',3),('#4cd97b',2)]
    box=int(W*0.60);x0=(W-box)//2;y0=(W-box)//2;gap=int(box*0.045)
    rh=(box-gap*3)//4;lab=int(rh*1.0);sq=rh
    for r,(c,n) in enumerate(rows):
        y=y0+r*(rh+gap)
        d.rounded_rectangle([x0,y,x0+lab,y+rh],radius=int(rh*.2),fill=c)
        d.rounded_rectangle([x0+lab+gap,y,x0+box,y+rh],radius=int(rh*.2),fill=(255,255,255,60))
        tw=(box-lab-gap-gap*4)//3
        for k in range(n):
            sx=x0+lab+gap*2+k*(tw+gap)
            d.rounded_rectangle([sx,y+gap,sx+tw,y+rh-gap],radius=int(rh*.16),fill=(255,255,255,235))
    return im.resize((S,S),Image.LANCZOS)
B=bg();F=fg()
B.save('assets/icon-background.png');F.save('assets/icon-foreground.png')
O=B.convert('RGBA');O.alpha_composite(F);O.convert('RGB').save('assets/icon-only.png')
