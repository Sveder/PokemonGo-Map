import PIL.Image as Image
import PIL.ImageOps as ImageOps

ORIGINAL = r"C:\work\pokemon\PokemonGo-Map\static\icons\%s.png"
GREY = r"C:\work\pokemon\PokemonGo-Map\static\icons\grey_%s.png"

for i in xrange(1, 152):
    img = Image.open(ORIGINAL % i)
    img.copy().convert("LA").save(GREY % i)