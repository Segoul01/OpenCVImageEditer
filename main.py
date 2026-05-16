import cv2


webcam = cv2.VideoCapture(0)
current_image = ''


def get_new_image():
    global current_image
    ret, frame = webcam.read()
    current_image = frame
    print('Image Taken!')


def show_image():
    global current_image
    cv2.imshow("Image", current_image)
    cv2.waitKey(0)
    on_exit()


def save_file():
    cv2.imwrite('image_output.jpeg', current_image)
    print('Image saved!')


def load_file():
    global current_image
    current_image = cv2.imread('image_output.jpeg')


def process_grayscale():
    global current_image
    # current_image *= 1./255
    current_image = cv2.cvtColor(current_image, cv2.COLOR_BGR2GRAY)
    print("Image Grayscaled!")


def process_invert():
    global current_image
    current_image = 255 - current_image
    print("Image Inverted!")


def process_scale(words: list):
    dimensions = words[1:]
    try:
        for i in range(len(dimensions)): dimensions[i] = int(dimensions[i])
    except Exception as e:
        print(e)
    
    dimensions = tuple(dimensions)
    global current_image
    current_image = cv2.resize(current_image, dimensions, interpolation=cv2.INTER_LINEAR)
    print(f"Resized Image to {dimensions[0]}:{dimensions[1]}")


def main():
    menu = '''Options:
    1\tCreate New Image
    2\tShow Image
    3\tSave Image
    4\tLoad Image
    5\tProcess - Grayscale
    6\tProcess - Invert
    7\tProcess - Scale [x][y]
    8\tExit'''

    while True:
        print(menu)
        try:
            user_input = input("-> ").strip()
            words = user_input.split()
            match int(words[0]):
                case 1: get_new_image()
                case 2: show_image()
                case 3: save_file()
                case 4: load_file()
                case 5: process_grayscale()
                case 6: process_invert()
                case 7: process_scale(words)
                case 8: 
                    on_exit()
                    break
                case _: print("Command Not Recgonized...")
        except Exception as e:
            print(e)


def on_exit():
    cv2.destroyAllWindows()


main()