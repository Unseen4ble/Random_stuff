from PIL import Image

# a=[r"C:\Users\arinj\Desktop\hola\coding_jinis\folder_dot_exe\rodnome mult shit\rdom\1.jpeg",r"C:\Users\arinj\Desktop\hola\coding_jinis\folder_dot_exe\rodnome mult shit\rdom\2.jpg",r"C:\Users\arinj\Desktop\hola\coding_jinis\folder_dot_exe\rodnome mult shit\rdom\3.png"]

# im= [Image.open(i) for i in a]

# im[0].save("smg.pdf",append_images=im[1:])

class pdfconvert:
    def __init__(self,files):
        self.im = [Image.open(filename) for filename in files]

    def imgtopdf(self):
        self.im[0].save("image.pdf",append_images=self.im[1:])