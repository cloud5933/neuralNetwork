from PIL import Image
import os
dataBaseMode = True
if dataBaseMode:
  path = "handwriting/"
  dir_list = os.listdir(path)
  print("Files and directories in '", path, "' :")
  # prints all files
  print(dir_list)
  pixOutput = []
  pixData = []
  for m in dir_list:
    im = Image.open(path+m) # Can be many different formats.
    pix = im.load()
    pixOutput.append([int(m[0])])
    pixelAll = []
    for i in range(0, im.height - 2):
      for n in range(0, im.width - 2):
        #print(i, n)
        #print(pix[n,i])  # Get the RGBA Value of the a pixel of an image
        if pix[n,i][0] - 0 < 255 - pix[n,i][0]:
          pixelAll.append(1)
        else:
          pixelAll.append(0)
    pixData.append(pixelAll)
  print(pixData)
  f = open("handwriting.txt", "w")
  f.write(str(pixData))
  f.close

  f = open("handwritingOutput.txt", "w")
  f.write(str(pixOutput))
  f.close
else:
    path = ""
    m = "userInput.jpg"
    im = Image.open(path+m) # Can be many different formats.
    pix = im.load()
    print(im.size)  # Get the width and hight of the image for iterating over
    pixelAll = []
    pixData = []
    print(im.width)
    print(im.height)
    for i in range(0, im.height - 2):
      for n in range(0, im.width - 2):
        #print(i, n)
        #print(pix[n,i])  # Get the RGBA Value of the a pixel of an image
        if pix[n,i][0] - 0 < 255 - pix[n,i][0]:
          pixelAll.append(1)
        else:
          pixelAll.append(0)
    """
    for i in range(len(pixelAll)):
      print(pixelAll[i], end="")
    """
    pixData.append(pixelAll)
    print(pixData)
    f = open("userInput bitmap.txt", "w")
    f.write(str(pixData))
    f.close