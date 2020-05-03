from PIL import Image, ImageFilter
from random import randint


class My_PIL:
    def __init__(self, for_open=True, *args, **kwargs) -> Image:
        """"
        :param mode: for_open = True - Open else Create
        """
        if for_open:
            self.im = Image.open(*args, **kwargs)
        else:
            self.im = Image.new(*args, **kwargs)

        self.size_x, self.size_y = self.im.size
        self.pixels = self.im.load()
        self.mask = [[False] * self.size_y for i in range(self.size_x)]

    def reload_mask(self):
        self.mask = [[False] * self.size_y for i in range(self.size_x)]

    def reload(self, im):
        self.im = im
        self.size_x, self.size_y = self.im.size
        self.pixels = self.im.load()

    def show(self):
        self.im.show()

    def save(self, *args, **kwargs):
        self.im.save(*args, **kwargs)

    def vertical_reflection(self):
        for i in range(self.size_x):
            for j in range(self.size_y // 2):
                self.pixels[i, j], self.pixels[i, self.size_y - j - 1] =\
                    self.pixels[i, self.size_y - j - 1], self.pixels[i, j]

    def horizontal_reflection(self):
        for i in range(self.size_x // 2):
            for j in range(self.size_y):
                self.pixels[self.size_x - i - 1, j], self.pixels[i, j] =\
                    self.pixels[i, j], self.pixels[self.size_x - i - 1, j]

    def transpose(self):
        image = Image.new("RGB", (self.size_y, self.size_x))
        pixels = image.load()
        for i in range(self.size_x):
            for j in range(self.size_y):
                pixels[j, i] = self.pixels[i, j]
        self.reload(image)

    def mask_contour(self):
        image = My_PIL(False, "RGB", (self.size_x, self.size_y))
        image.reload(self.im)
        image.im = image.im.filter(ImageFilter.CONTOUR)
        pixels = image.im.load()
        for i in range(self.size_x):
            for j in range(self.size_y):
                if sum(pixels[i, j]) / 3 < 20:
                    pixels[i, j] = 0, 0, 0
                    self.mask[i][j] = True

    def random_color(self):
        for i in range(self.size_x):
            for j in range(self.size_y):
                if not self.mask[i][j]:
                    self.pixels[i, j] = tuple([randint(0, 255) for i in range(3)])

    def my_filter(self):
        lst_color = [[0, 0, 0], [255, 255, 255], [255, 0, 0], [255, 255, 0], [0, 255, 0], [0, 255, 255], [0, 0, 255]]
        for i in range(self.size_x):
            for j in range(self.size_y):
                if not self.mask[i][j]:
                    self.pixels[i, j] = tuple(lst_color[randint(0, 6)])

    def random_color_with_n(self, n):
        for i in range(n):
            x, y = randint(0, self.size_x - 1), randint(0, self.size_y - 1)
            if not self.mask[x][y]:
                self.pixels[x, y] = tuple([randint(0, 255) for i in range(3)])


pic = My_PIL(True, 'strashnyi-kot-foto-20.jpg')
pic.mask_contour()
pic.my_filter()
#  pic.random_color()
#  pic.random_color_with_n(100000)
#  pic.vertical_reflection()
#  pic.horizontal_reflection()
#  pic.transpose()
pic.show()
#  pic.save("strashnyi-kot-foto-20.jpg", "JPEG")

