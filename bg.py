from PIL import Image, ImageFont, ImageDraw

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
        return "/Users/danieljilg/Downloads/pexels-photo-48840.jpeg"


class BitterGravelist:
    word_generator = None
    image_generator = None

    def __init__(self, word_generator=WordGenerator(), image_generator=ImageGenerator):
        self.word_generator = word_generator
        self.image_generator = image_generator

    def generate_gravel(self):
        print "gravelling..."
        image = Image.open(self.image_generator.get_image())
        draw = ImageDraw.Draw(image)

        font = ImageFont.truetype("/Users/danieljilg/Downloads/master_of_break/master_of_break.ttf", 15)
        draw.text((10, 25), "world", font=font)

        image.save('/Users/danieljilg//Desktop/output.png', 'PNG')

if __name__ == '__main__':
    BitterGravelist().generate_gravel()
