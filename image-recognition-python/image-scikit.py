from skimage import data,color
from skimage.filters import threshold_otsu,try_all_threshold
import numpy as np
import matplotlib.pyplot as plt
import PIL

#Ex 4
#try_all_threshhold
#Global uniform background Threshhold threshhold_otsu
#Local Uneven background threshold threshhold_local (Block Size) offset
chess_image = data.coffee()
plt.imshow(chess_image)
plt.show()
chess_image_gray = color.rgb2gray(chess_image)
thresh = threshold_otsu(chess_image_gray)
fig,ax = try_all_threshold(chess_image_gray,verbose=False) 
plt.show()

binary = chess_image_gray < thresh
plt.imshow(binary,cmap='gray')
plt.show()
#global thresh and local(Block size offset, image)
'''
tryall
grayscale = rgb2gray(fruits_image)

# Use the try all method on the grayscale image
fig, ax = try_all_threshold(grayscale, verbose=False)

# Show the resulting plots
plt.show()
'''
#Ex 3
# rocket_image = data.rocket() 
# rocket_image = np.flipud(rocket_image)
# plt.imshow(rocket_image)
# plt.show()

# rocket_image = data.rocket() 
# rocket_image = np.fliplr(rocket_image)
# plt.imshow(rocket_image)
# plt.show()

# chess_image = data.coffee()
# plt.imshow(chess_image)
# plt.show()
# coffee_image = data.coffee()
# red_channel = coffee_image[:,:,0]
# plt.hist(red_channel.ravel(),bins=256)
# plt.title("Red Histogram")
# plt.show() 

#Ex 2
# grey_rocket = color.rgb2gray(rocket_image)
# print(grey_rocket)
# plt.imshow(grey_rocket,cmap='gray')
# plt.show()

# img = data.astronaut()
# img_gray = color.rgb2gray(img)
# plt.imshow(img_gray,cmap='gray') #cmap='gray' for gray scale
# plt.show()
# plt.imshow(rocket_image,'Orignal RGB image')
# plt.imshow(grey_rocket,'GreyScaled image')

#Ex 1
# coffee_image = data.coffee()
# print(np.shape(coffee_image))
# coins_image = data.coins()
# print(np.shape(coins_image))