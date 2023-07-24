

from PIL import Image, ImageEnhance

#converting pdf into csv

#import tabula
# Read a PDF File
#df = tabula.read_pdf("PMYLS Merit List_Mehran-University-of-Engineering-Technology.pdf", pages='all')[0]

#converting
#tabula.convert_into("PMYLS Merit List_Mehran-University-of-Engineering-Technology.pdf", "PM.csv", output_format="csv", pages='all')






# opening image to work with it
my_image = Image.open('WhatsApp Image 2023-07-21 at 11.02.11 AM.jpeg')



# Changing image extension
my_image.save("id_card_.pdf") #->It will save a copy in pdf

# show image
# id.show()



# resizing image
# my_image.thumbnail((400, 400))
# my_image.save("picture.png")

# enhancer
# enhancer = ImageEnhance.Sharpness(my_image)
# enhancer.enhance(5).save("enhancedImage.jpeg")

# color
# enhancer = ImageEnhance.Color(my_image)
# enhancer.enhance(4).save("color_changed.jpg")

# brightness
# enhancer = ImageEnhance.Brightness(my_image)
# enhancer.enhance(1.3).save("brightenedImage.png")
