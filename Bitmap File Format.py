from PIL import Image

def save_otl_image(image: Image.Image, filename: str):
    pixels = image.load()
    width, height = image.size
    with open(filename, 'w') as file:
        file.write(f'{width} {height}\n')
        for y in range(0,height):
            for x in range(0,width):
                r,g,b = pixels[x,y]
                file.write(f'{r} {g} {b}\n')
        
    print(f'Image saved to OTL format.\nSize: {width}x{height}\nFilename: {filename}')


def load_otl_image(filename: str) -> Image.Image:
    with open(filename, 'r') as file:
        meta_data_str = file.readline().strip().split(' ')
        width = int(meta_data_str[0])
        height = int(meta_data_str[1])
        return_image = Image.new('RGB', (width,height))
        pixels = return_image.load()
        for y in range(0,height):
            for x in range(0,width):
                line_colour = file.readline().strip().split(' ')
                r, g, b = [int(c) for c in line_colour]
                pixels[x,y] = r,g,b
        ## Complete the code
        
    return return_image

loaded_image = load_otl_image('image.otl')
loaded_image.save('temp.png')
save_otl_image(loaded_image, 'temp2.otl')