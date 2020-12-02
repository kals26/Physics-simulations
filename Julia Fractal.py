# Julia Fractal
from PIL import Image 
# driver function 
if __name__ == "__main__": 
	
	# setting the width, height and zoom 
	
	w, h, zoom = 1920,1080,1

	# creating the image in RGB mode 
	bitmap = Image.new("RGB", (w, h), "white") 

	pix = bitmap.load() 
	
	# the equation to create the fractal 
	cX, cY = -0.7, 0.3  # Just mess around and get messy images. Though this particular value makes it look beau.
	dX, dY = 0.0, 0.0
	maxIter = 255

	for x in range(w): 
		for y in range(h): 
			zx = 1.5*(x - w/2)/(0.5*zoom*w) + dX 
			zy = 1.0*(y - h/2)/(0.5*zoom*h) + dY 
			i = maxIter 
			while zx*zx + zy*zy < 4 and i > 1: 
				tmp = zx*zx - zy*zy + cX 
				zy,zx = 2.0*zx*zy + cY, tmp 
				i -= 1
				pix[x,y] = (i << 21) + (i << 10) + i*8

	# to display the created fractal 
	bitmap.show() 
	bitmap.save("fractalImage.png", format= 'png')
