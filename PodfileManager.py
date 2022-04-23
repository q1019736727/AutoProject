import datetime
import os
import subprocess
import time

class PodfileManager:

    def __init__(self,fileName='Podfile'):
        self.fileName = fileName
        self.podFileStr = ''

    def readConfig(self,fileName):
        with open(fileName, 'r', encoding='utf-8') as file:
            return file.read()

    def modefiyPod(self):
        if os.path.exists('Podfile.lock'):
            os.remove('Podfile.lock')
        podValue = ''
        podValue += '\n' + "pod 'AFNetworking'"
        self.podFileStr = self.podFileStr.replace('modify_pod_value', podValue)

    def creatPodFile(self):
        with open('Podfile', 'w', encoding='utf-8') as fh:
            fh.write(self.podFileStr)
            fh.close()

    def update_podfile(self):
        print('*****************开始拉取组件***************')
        podStr = 'pod install'
        index = 0
        while True:
            podResult = self.executeCommand(comString=podStr, timeout=1800)
            if podResult != 200:
                index += 1
                if index == 4:
                    podStr = "pod install --repo-update"
                elif index == 5:
                    podStr = "pod update --no-repo-update"
                elif index > 5:
                    print('组件多次拉取失败，请重新打包')
                    return (0, '组件多次拉取失败')
                else:
                    print('********拉取组件失败，正在尝试重新拉取')
                    continue
            else:
                print('pod 拉取组件成功')
                return (200,'pod 成功')


    def executeCommand(self, comString='', timeout=None):
        if comString == '':
            return (0,'请输入执行命令')
        statrtTime = datetime.datetime.now()

        if timeout:
            end_time = datetime.datetime.now() + datetime.timedelta(seconds=timeout)

        sub = subprocess.Popen(comString, stdin=subprocess.PIPE, shell=True, bufsize=4096)
        while True:
            if sub.poll() is not None:
                break
            time.sleep(0.1)
            if timeout:
                if end_time <= datetime.datetime.now():
                    sub.kill()
                    return 0

        endtime = datetime.datetime.now()
        seconds = (endtime - statrtTime).seconds
        if sub.returncode == 0:
            print(f'pod花费时间{seconds}')
            return 200
        else:
            if seconds > timeout:
                return 2
            else:
                return 1


    def autoManager(self):
        self.podFileStr = self.readConfig(fileName=self.fileName + '1')
        self.modefiyPod()
        self.creatPodFile()
        self.update_podfile()



if __name__ == '__main__':
    manager = PodfileManager(fileName='Podfile')
    manager.autoManager()