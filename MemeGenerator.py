import cv2
import tkinter


class MemeGUI:
    def __init__(self, master):
        self.master = master
        master.title("Meme Generator")

        self.text = tkinter.Text(master)
        self.text.pack()

        self.button = tkinter.Button(master, text="Submit", command=self.submit)
        self.button.pack()

    def submit(self):
        text = self.text.get("1.0", "end-1c")
        print(text)
        img = cv2.imread('cole.jpg', cv2.IMREAD_COLOR)

        # Getting the original size of the image
        dimensions = img.shape
        height = dimensions[0]
        width = dimensions[1]
        # print("Height: {:d} Width: {:d}".format(dimensions[0],dimensions[1]))

        # Resizing image if too big
        if height > 1080 and width > 720:
            img = cv2.resize(img, (1080, 720))
            height = 720
            width = 1080

        # Getting the positions for the image text
        texttopH = int(height / 6)
        textbottomH = height - int(height / 6)
        textW = width - int(width / 1.5)

        # Math for text size
        def scaleText(text, width):
            for scale in reversed(range(0, 60, 1)):
                textSize = cv2.getTextSize(text, fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=scale / 10, thickness=2)
                new_width = textSize[0][0]
                # print(new_width)
                if (new_width <= width):
                    return scale / 10

        # print(textsize[0][0])
        print(width)
        print(scaleText("Bottom Text", width))

        # Putting the text onto the image
        cv2.putText(img, "Bottom Text", (textW, textbottomH), cv2.FONT_HERSHEY_PLAIN,
                    scaleText("Bottom Text", width), (255, 255, 255), 4)
        cv2.putText(img, text, (textW, texttopH), cv2.FONT_HERSHEY_PLAIN, scaleText(text, width), (255, 255, 255),
                    4)

        # Displaying image onscreen
        cv2.imshow("Image", img)

        filename = 'meme.png'
        cv2.imwrite(filename, img)

        cv2.waitKey(1000000)

root = tkinter.Tk()
memeGUI = MemeGUI(root)
root.mainloop()


