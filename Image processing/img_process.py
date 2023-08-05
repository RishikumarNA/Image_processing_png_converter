from PIL import Image, ImageFilter


img=Image.open('./Image processing/img1.jpg')
filtered_img=img.filter(ImageFilter.BLUR)
filtered_img.save("Image processing/blur_img.png","png")