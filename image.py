from PIL import Image
import sys, os
def image_to_ascii(name,format,end,scale):
    im = Image.open(f"./photos/{name}.{format}")
    width,height = im.size
    im.resize((width//scale,height//scale)).save(f"new.{format}")

    im = Image.open(f"new.jpg")
    width,height = im.size
    pix_value =list(im.getdata())
    grid = []
    for z in range(height):
        grid.append(["X"] * width)
    pix = im.load()


    for y in range(height):
        for x in range(width):
            if sum(pix[x,y]) == 0:
                grid[y][x] = "#"
            elif sum(pix[x,y]) in range(1,100):
                grid[y][x] = "X"
            elif sum(pix[x,y]) in range(100,200):
                grid[y][x] = "?"
            elif sum(pix[x,y]) in range(200,300):
                grid[y][x] = "&"
            elif sum(pix[x,y]) in range(300,400):
                grid[y][x] = "+"
            elif sum(pix[x,y]) in range(400,500):
                grid[y][x] = "/"
            elif sum(pix[x,y]) in range(500,600):
                grid[y][x] = "-"
            elif sum(pix[x,y]) in range(600,700):
                grid[y][x] = "*"
            elif sum(pix[x,y]) in range(700,765):
                grid[y][x] = "$"
            else:
                grid[y][x] = " "

    file = open(f"./result/{end}.txt","w")

    for row in grid:
        file.write("".join(row)+ "\n")

    file.close()




name = input("Напишите название картинки которую вы хотите конвертировать в ascii: \n")
format = input("Формат фото: \n")
end = input("Под каким названием сохранить фото? ")

image_to_ascii(name,format,end,3)