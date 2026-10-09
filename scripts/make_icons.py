from PIL import Image, ImageDraw
import math
S=4  # supersample
def ring(size, bg, transparent=False, scale=1.0, mono=None):
    W=size*S
    im=Image.new("RGBA",(W,W),(0,0,0,0) if transparent else bg)
    d=ImageDraw.Draw(im)
    c=W/2; R=W*0.30*scale; w=W*0.075*scale
    segs=[(0,5,"#E2668A"),(5,10,"#7CC2A3"),(10,16,"#E9B04F"),(16,23,"#9A9AE0"),(23,28,"#C08AD4")]
    gap=1.2
    for a,b,col in segs:
        start=a/28*360-90+gap; end=b/28*360-90-gap
        d.arc([c-R,c-R,c+R,c+R],start,end,fill=mono or col,width=int(w))
    ang=(9.5/28)*2*math.pi-math.pi/2
    mx,my=c+(R-w/2)*math.cos(ang),c+(R-w/2)*math.sin(ang)
    r=w*0.95
    d.ellipse([mx-r,my-r,mx+r,my+r],fill=mono or "#FFFFFF")
    if not mono:
        r2=r*0.55; d.ellipse([mx-r2,my-r2,mx+r2,my+r2],fill="#4F8A72")
    return im.resize((size,size),Image.LANCZOS)
plum=(74,26,52,255)
ring(1024,plum).convert("RGB").save("assets/icon-only.png")
ring(1024,plum,transparent=True,scale=0.8).save("assets/icon-foreground.png")
Image.new("RGB",(1024,1024),plum[:3]).save("assets/icon-background.png")
for name,bg in (("splash.png",(246,242,244)),("splash-dark.png",(23,17,22))):
    sp=Image.new("RGB",(2732,2732),bg); sp.paste(ring(800,plum,transparent=True),(966,966),ring(800,plum,transparent=True)); sp.save("assets/"+name)
# Android notification small icon: white silhouette on transparent
ring(96,plum,transparent=True,mono="#FFFFFF").save("assets/ic_stat_icon.png")
ring(512,plum).convert("RGB").save("docs/icon-512.png")
print("ok")
