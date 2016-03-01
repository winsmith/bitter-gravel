# coding: utf-8
from PIL import Image, ImageFont, ImageDraw
from subprocess import call


class WordGenerator:
    """
    Generates pithy statements for our visual content
    """

    source = None

    @staticmethod
    def get_content(length=100):
        return "I sat on a rug, biding my time, drinking her wine"


class ImageGenerator:
    """
    Steals pretty images for the content to sit on
    """

    @staticmethod
    def get_image():
        return "test:Boat"


class BitterGravelist:
    word_generator = None
    image_generator = None

    def __init__(self, word_generator=WordGenerator(), image_generator=ImageGenerator):
        self.word_generator = word_generator
        self.image_generator = image_generator

    def generate_gravel(self):
        image = Image.open(self.image_generator.get_image())
        draw = ImageDraw.Draw(image)

        color = '#ffc800'

        # create border
        padding = 10
        thickness = 5
        top = padding
        left = padding
        right = image.size[0] - padding
        bottom = image.size[1] - padding
        # turns out the method wants left, *then* top. switch.
        draw.rectangle((top, left, bottom, left+thickness), fill=color)
        draw.rectangle((top, left, top+thickness, right), fill=color)
        draw.rectangle((top, right, bottom, right-thickness), fill=color)
        draw.rectangle((bottom, left+thickness, bottom, right-thickness), fill=color)

        text = self.word_generator.get_content()
        font = ImageFont.truetype("Helvetica", 16)
        draw.text((10, 25), text, font=font)

        image_save_file_name = '/Users/danieljilg//Desktop/output.png'
        image.show()
        # image.save(image_save_file_name, 'PNG')
        # call(['open', image_save_file_name])


if __name__ == '__main__':
    BitterGravelist().generate_gravel()
