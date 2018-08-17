# encoding=utf-8
from Tkinter import *

def xinlabel():
    global root
    s = Label(root,text='我爱Python')
    s.pack()

def xinlabel2(event):
    global root
    print 'error'
    s = Label(root,text='python是啥')
    s.pack
    
if __name__=="__main__":
    root = Tk()
    root.wm_title("幸tkinter教程完全版")

    w1 = Label(root,text='跟着新歌学tkinter')
    w2 = Label(root,text='python开发界面不是梦')
    w3 = Label(root,text='人生苦短 我用python')
    w1.pack()
    w2.pack()
    w3.pack()

    b1 = Button(root,text='星哥',command = xinlabel)
    b1.pack()
    
    b2 = Button(root,text='星哥2')
    b2.bind("<Button-1>",xinlabel2)
    b2.pack()
    
    root.mainloop()
