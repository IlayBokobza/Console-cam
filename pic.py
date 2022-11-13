from io import BytesIO
from PIL import Image
from yachalk import chalk
import cv2

def processImage(data):
    ySize = 75
    xSize = 150

    image = Image.open(data)
    image = image.resize((xSize,ySize))
    image = image.transpose(Image.FLIP_LEFT_RIGHT)
    pixels = image.load()
    image.close()

    output = ""
    for y in range(ySize):
        for x in range(xSize):
            pixel = pixels[x,y]
            output += chalk.rgb(pixel[0],pixel[1],pixel[2]).bold("#")

        output += "\n"
    
    print(output)

def main():
    camera = cv2.VideoCapture(0)
    _,frame = camera.read()
    frameData = cv2.imencode('.webp',frame)[1].tobytes()
    processImage(BytesIO(frameData))
        

main()