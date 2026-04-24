
# Import libraries
import cv2
import glob
import os
import random

def main():

    # Read images from folder
    output_dir ="/impose/data/imposeimage"
    o_img = [cv2.imread(file) for file in glob.glob('/impose/data/Officeimages/*.jpg')]
    f_img= [cv2.imread(file) for file in glob.glob('/impose/data/fireimages/*.jpg')]
    if not os.path.exists(output_dir):
         os.makedirs(output_dir)
    count=0
    for img1,img2 in zip(o_img,f_img):
        bh, bw = img1.shape[:2]
        img2 = cv2.resize(img2, (bw // 4, bh // 4))  #resize image
        fh, fw = img2.shape[:2]

        y_offset = random.randint(0, bh - fh)
        x_offset = random.randint(0, bw - fw)
        img1[y_offset:y_offset+fh, x_offset:x_offset+fw]=img2
        

        # Save images in folder
        cv2.imwrite(f"{output_dir}/img{count}.jpg",img1)
        count+=1
        
if __name__== "__main__":
    main()
    print("done")
    
    
    
    
    




