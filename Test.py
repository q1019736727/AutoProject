
import os
from biplist import  *

def creatJson():
    with open('info.plist', 'w', encoding='utf-8') as file:
        file.write("hello world")

def changePlist():
    try:
        plist = readPlist('./TestAuto/info.plist')
        plist['UIAppFonts'] = "字体名称"
        plist['NSPhotoLibraryUsageDescription'] = 'App需要您的同意才能访问相机'
        plist['CFBundleDisplayName'] = '这是App名字'
        writePlist(plist, './TestAuto/info.plist')
    except Exception as error:
        print("读取plist文件失败")




if __name__ == "__main__":
    changePlist()