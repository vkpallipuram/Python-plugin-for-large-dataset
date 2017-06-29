from PIL import Image
import numpy as np
import os

def main():

    images = []
    output = open("Image_sums.csv", 'w')

    #Read file names and confirm they are .tif files.
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for f in files:
        ext =  (f[-4:])
        if ext == '.tif':
            images.append(f)
    #Iterate through images and calculate sums
    output.write("Sum of all Images\n")
    for imgName in images:
        try:
            img = Image.open(imgName, 'r')
        except:
            print ("Unable to load" + imgName)

        array = np.asarray(img)
        total = array.sum(0).sum(0)

        # output for txt file writ = imgName +  ": " + str(format(total, ",d"))
        writ = imgName + ", " + str(total)
        output.write(writ + "\n")
    output.close()

main()
