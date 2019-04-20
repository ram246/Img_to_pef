import util
import sys
import glob
from fpdf import FPDF
from PIL import Image

USAGE_ERROR = "Usage: " + sys.argv[0] + " <image_location> <img_prefix> [-f filename] [-d dest]"
def usage_error():
    print(USAGE_ERROR, file=sys.stderr)
    sys.exit(2)

def parseArguments(argv):
    length = len(argv)
    filename = None
    dest = None
    args = []
    i = 0
    while (i < length):
        if (argv[i] == "-f"):
            if (i == length - 1):
                usage_error()
            filename = argv[i + 1]
            i += 1
        elif (argv[i] == "-d"):
            if (i == length - 1):
                usage_error()
            dest = argv[i + 1]
            i += 1
        else:
            args.append(argv[i])
        i += 1
    
    if len(args) != 3:
        usage_error()
    
    if (filename == None):
        filename = args[2] + ".pdf"
    if (dest == None):
        dest = args[1]
    return (args[1], args[2], filename, dest)

if __name__ == "__main__":
    image_location, img_prefix, filename, dest = parseArguments(sys.argv)

    all_images = glob.glob(image_location + "\\" + img_prefix + '*.png')

    print("Parse successful: " + image_location, img_prefix, filename, dest)
    #print(all_images)
    cover = Image.open(all_images[0])
    width, height = cover.size

    pdf = FPDF(unit = "pt", format = [width, height])
    for image in all_images:
        pdf.add_page()
        pdf.image(image, 0, 0)
    pdf.output(dest + "\\" + filename, "F")
