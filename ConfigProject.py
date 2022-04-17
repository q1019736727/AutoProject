
import os
import re
from biplist import *

class ConfigProject:

    def __init__(self):
        self.plistName = "info.plist"

    def modifyNameVersion(self):
        try:
            plist = readPlist("./TestAuto/" + self.plistName)
            plist['CFBundleDisplayName'] = '我的测试名称'
            plist['CFBundleShortVersionString'] = '1.1'
            writePlist(plist, "./TestAuto/" + self.plistName, binary=False)
            return (200, "配置APP名称和版本成功")
        except Exception as error:
            print('配置APP名称和版本出错：')
            print(error)
            return (0, "配置APP名称和版本出错，请联系天马工场技术人员")

    def modefyAudio(self):
        try:
            infoPath = os.path.join('./TestAuto/', self.plistName)
            plist = readPlist(infoPath)
            plist['UIBackgroundModes'] = ['audio']
            writePlist(plist, infoPath, binary=False)
            return (200, "后台音频配置成功")
        except Exception as error:
            print('后台音频配置出错')
            print(error)
            return (0, "配置APP名称和版本出错，请联系天马工场技术人员")

    def modefyNet(self):
        try:
            plist = readPlist("./TestAuto/" + self.plistName)
            plist['NSLocalNetworkUsageDescription'] = '开启app投放哈哈'
            writePlist(plist, "./TestAuto/" + self.plistName, binary=False)
            return (200, "投屏权限配置成功")
        except Exception as error:
            print('投屏权限配置出错')
            print(error)
            return (0, "配置APP名称和版本出错，请联系天马工场技术人员")


if __name__ == "__main__":
    modif = ConfigProject()
    modif.modifyNameVersion()
    modif.modefyAudio()
    modif.modefyNet()
    pass