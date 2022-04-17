import os
from PIL import Image
import json
import  shutil
from math import trunc

images_template = [
        {
            "size": 20,
            "idiom": "iphone",
            "scale": 2
        },
        {
            "size": 20,
            "idiom": "iphone",
            "scale": 3
        },
        {
            "size": 29,
            "idiom": "iphone",
            "scale": 2
        },
        {
            "size": 29,
            "idiom": "iphone",
            "scale": 3
        },
        {
            "size": 40,
            "idiom": "iphone",
            "scale": 2
        },
        {
            "size": 40,
            "idiom": "iphone",
            "scale": 3
        },
        {
            "size": 60,
            "idiom": "iphone",
            "scale": 2
        },
        {
            "size": 60,
            "idiom": "iphone",
            "scale": 3
        },
        {
            "size": 1024,
            "idiom": "iphone",
            "scale": 1
        }
    ]
sizes = [
    40,
    60,
    58,
    87,
    80,
    120,
    180,
    1024
]
class CYGenerateIcon:
    def __init__(self,size=(1024,1024)):
        self.size = size

    def generateIcon(self):

        for s in sizes:
            image_path = Image.open('test2.png')
            print(s)
            imageSize = image_path.resize((s,s))
            dir_name = 'images'
            if not os.path.isdir(dir_name):
                os.makedirs(dir_name)
            imageSize.save('images/#{s}x#{s}.png', 'png')

        icons_dir = './images'
        appicon_dir = os.path.join('./', 'TestAuto/Assets.xcassets/AppIcon.appiconset')
        images = []
        cleared = False

        print(1111)

        for image_temp in images_template:
            icon_name = '{0}x{0}.png'.format(trunc(image_temp['size'] * image_temp['scale']))
            icon_path = os.path.join(icons_dir, icon_name)
            if not os.path.exists(icon_path):
                continue
            if not cleared:
                for root, dirs, files in os.walk(appicon_dir):
                    for f in files:
                        os.unlink(os.path.join(root, f))
                    for d in dirs:
                        shutil.rmtree(os.path.join(root, d))
                cleared = True
            shutil.copy2(icon_path, appicon_dir)
            image = {'filename': icon_name, 'idiom': image_temp['idiom'],
                     'scale': '{0}x'.format(image_temp['scale']), 'size': '{0}x{0}'.format(image_temp['size'])}
            images.append(image)
        print(222)

        contents = {
            'images': images,
            'info': {
                'author': 'tm',
                'version': 1
            },
            'properties': {
                'pre-rendered': False
            }
        }
        contents_path = os.path.join('./',
                                     'TestAuto/Assets.xcassets/AppIcon.appiconset/Contents.json')
        with open(contents_path, 'w', encoding='utf-8') as openfile:
            json.dump(contents, openfile, indent=4, sort_keys=False, ensure_ascii=False)
        print(333)

    def imageResize(self):
        image_path = Image.open('test2.png')
        imageSize = image_path.resize(self.size)
        dir_name = 'images'
        if not os.path.isdir(dir_name):
            os.makedirs(dir_name)
        imageSize.save('images/chang.png','png')

if __name__ == '__main__':
    image = CYGenerateIcon()
    # image.imageResize()
    image.generateIcon()

# cd TMProject
#
# Python3 -c 'from TMAutoManager import TMAutoManager; TMAutoManager(app_id="'$app_id'",version_id="'$version_id'",compApi="'$compApi'",build_number="'$BUILD_NUMBER'",callbackApi="'$callbackApi'", pgyerApiKey="'$apikey'").auto_manager()'
# Python3 -c 'from GenerateIcon import CYGenerateIcon; CYGenerateIcon(size=(100,100)).imageResize()'
