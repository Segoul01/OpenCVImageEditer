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


def main():
    menu = '''Options:
    1\tCreate New Image
    2\tShow Image
    3\tSave Image
    4\tLoad Image
    5\tExit'''

    while True:
        print(menu)
        try:
            user_input = int(input("-> "))
            match user_input:
                case 1: get_new_image()
                case 2: show_image()
                case 3: save_file()
                case 4: load_file()
                case 5: 
                    on_exit()
                    break
                case _: print("Command Not Recgonized...")
        except Exception as e:
            print(e)


def on_exit():
    cv2.destroyAllWindows()

main()