import sys
import qdarkstyle
import os
import argparse
import glob
import cv2
from artist import Artist
from ui.draw import ui_edit_widget
from PyQt5 import QtWidgets

parser = argparse.ArgumentParser()
parser.add_argument("--img", type=str, default="./images/content/o7.png", help='input')
parser.add_argument("--img_folder", type=str, default=None, help='inputs')
parser.add_argument("--model", type=str, default="./models/seated_nude.pth.tar", help='model')
parser.add_argument("--out", type=str, default='./out/', help='output')
parser.add_argument("--auto_update", action='store_true', help='if you have a powerful GPU, lets activate it for the better experience')
args = parser.parse_args()

if __name__ == '__main__':

    args.out = os.path.join(args.out, os.path.basename(args.model).strip(".pth.tar"))
    if not os.path.isdir(args.out):
        os.mkdir(args.out)
    artist = Artist(args.model)

    if args.img_folder is None:
        artist.network.connect_weights = [0.0, 0.0, 0.0, 0.0, 0.0] # match UI config
        app = QtWidgets.QApplication(sys.argv)
        app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        edit_widget = QtWidgets.QWidget()
        ui = ui_edit_widget()
        ui.setupUi(edit_widget, args.img, artist, args.out, auto_update=args.auto_update)
        edit_widget.show()
        sys.exit(app.exec_())
    else:
        imgs = glob.glob(os.path.join(args.img_folder, "*.png")) + glob.glob(os.path.join(args.img_folder, "*.jpg"))
        assert imgs != [], "Img Folder should contain images in PNG or JPG"
        for img in imgs:
            print("Stylizing " + img)

            img_np = cv2.cvtColor(cv2.resize(cv2.imread(img), (512, 512)), cv2.COLOR_BGR2RGB)
            stylized_img = artist.stylize(img_np)
            cv2.imwrite(os.path.join(args.out, os.path.basename(img)), cv2.cvtColor(stylized_img, cv2.COLOR_RGB2BGR))
