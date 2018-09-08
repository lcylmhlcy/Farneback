import matplotlib
matplotlib.use('Agg') 
import cv2  
import numpy as np  
from PIL import Image,ImageDraw
from skimage import filter
from skimage import io
#import cv2.cv as cv   
import matplotlib.pyplot as plt

# def getPixel(image,x,y,G,N):  
#     L = image.getpixel((x,y))  
#     if L > G:  
#         L = True  
#     else:  
#         L = False  
  
#     nearDots = 0  
#     if L == (image.getpixel((x - 1,y - 1)) > G):  
#         nearDots += 1  
#     if L == (image.getpixel((x - 1,y)) > G):  
#         nearDots += 1  
#     if L == (image.getpixel((x - 1,y + 1)) > G):  
#         nearDots += 1  
#     if L == (image.getpixel((x,y - 1)) > G):  
#         nearDots += 1  
#     if L == (image.getpixel((x,y + 1)) > G):  
#         nearDots += 1  
#     if L == (image.getpixel((x + 1,y - 1)) > G):  
#         nearDots += 1  
#     if L == (image.getpixel((x + 1,y)) > G):  
#         nearDots += 1  
#     if L == (image.getpixel((x + 1,y + 1)) > G):  
#         nearDots += 1  
  
#     if nearDots < N:  
#         return image.getpixel((x,y-1))  
#     else:  
#         return None  

# def clearNoise(image,G,N,Z):  
#     draw = ImageDraw.Draw(image)  
  
#     for i in xrange(0,Z):  
#         for x in xrange(1,image.size[0] - 1):  
#             for y in xrange(1,image.size[1] - 1):  
#                 color = getPixel(image,x,y,G,N)  
#                 if color != None:  
#                     draw.point((x,y),color)        
      
def image_joint(image_list,opt):#opt= vertical ,horizon  
    image_num=len(image_list)  
    image_size=image_list[0].size  
    height=image_size[1]  
    width=image_size[0]  
          
    if opt=='vertical':  
        new_img=Image.new('RGB',(width,image_num*height),255)  
    else:  
        new_img=Image.new('RGB',(image_num*width,height),255)  
    x=y=0  
    count=0  
    for img in image_list:  
        new_img.paste(img,(x,y))  
        count+=1  
        if opt=='horizontal':  
            x+=width  
        else : y+=height  
    return new_img  


def Farneback():     
    start_img = Image.open("/home/computer/lcy/guangliu/image_0001.jpg")  
    later_img = Image.open("/home/computer/lcy/guangliu/image_0004.jpg")  
 
    start_img=np.array(start_img)  
    later_img=np.array(later_img)  
  
    prvs = cv2.cvtColor(start_img,cv2.COLOR_BGR2GRAY)  
    next = cv2.cvtColor(later_img,cv2.COLOR_BGR2GRAY)  
  
    flow = cv2.calcOpticalFlowFarneback(prvs,next,None,0.5,3,15,3,5,1.2,0)
    # print flow  
      
    hsv = np.zeros_like(start_img)  
    hsv[...,1] =255  
    mag, ang = cv2.cartToPolar(flow[...,0], flow[...,1])  
    hsv[...,0] = ang*180/np.pi/2  
    hsv[...,2] = cv2.normalize(mag,None,0,255,cv2.NORM_MINMAX)  
    RGB= cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)  
    GRAY = cv2.cvtColor(RGB,cv2.COLOR_BGR2GRAY)   
      
    GRAY=Image.fromarray(GRAY) 

    # clearNoise(GRAY,50,5,5)
    
    #  setup a converting table with constant threshold
    threshold = 11
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)

    #  convert to binary image by the table
    BLACK = GRAY.point(table,'1')
    BLACK = np.array(BLACK)

    # kernel = np.ones((5,5), np.uint8)  
    # BLACK = cv2.erode(BLACK,kernel)
    print BLACK.shape
    print '#######################################'
    print BLACK

##############################################################################
    # plt.figure()
    # plt.imshow(GRAY,cmap='gray')
    # plt.axis('off')
    # plt.savefig("/home/computer/lcy/guangliu/3.jpg")

    plt.figure()
    plt.imshow(BLACK)
    plt.axis('off')
    plt.savefig("/home/computer/lcy/guangliu/5.jpg")
##############################################################################

    # joint_image.show()  
    #GRAY.show()  
    #cv2.imshow('frame2',RGB)  
      
    # cv.WaitKey()  


Farneback()