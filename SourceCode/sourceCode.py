
import subprocess,os,shutil
os.system('title Openbullet MMO - hungsaki2003@gmail.com')
xanh = '\033[0;32m'
try:
    os.makedirs('HungHT1890')
    with open('HungHT1890\huongdan.url','w',encoding='utf-8') as huongdan:
        huongdan.write('[InternetShortcut]\nIDList=\nURL=https://www.youtube.com/watch?v=iJ42M9D1fvY&list=PLU3IakGjGV_0F1iFqfJRieiKigiEZhB-H')
    with open('HungHT1890\FreeTools.url','w',encoding='utf-8') as freeTools:
        freeTools.write('[InternetShortcut]\nIDList=\nURL=https://sites.google.com/view/openbulletconfigshop/freemmotools?')
    with open('HungHT1890\PaidTools.url','w',encoding='utf-8') as paiodTools:
        paiodTools.write('[InternetShortcut]\nIDList=\nURL=https://sites.google.com/view/openbulletconfigshop')
    with open('HungHT1890\Lienhe.url','w',encoding='utf-8') as lienhe:
        lienhe.write('[InternetShortcut]\nIDList=\nURL=https://t.me/hunght1890')
except:
    pass
# task1
def runOpenbullet():
    subprocess.Popen('openbullet.exe')
# task2
def tutorialTools():
    os.startfile('HungHT1890\huongdan.url')
# task3
def fixError():
    try:
        shutil.rmtree('DB')
    except:
        pass
# task4
def resetTools():
    try:
        shutil.rmtree('DB')
    except:
        pass
    try:
        shutil.rmtree('Hits')
    except:
        pass
    try:
        shutil.rmtree('Configs')
    except:
        pass
    try:
        shutil.rmtree('Wordlists')
    except:
        pass
    try:
        shutil.rmtree('Plugins')
    except:
        pass
    try:
        shutil.rmtree('Screenshots')
    except:
        pass
    try:
        shutil.rmtree('Captchas')
    except:
        pass
    try:
        shutil.rmtree('Sounds')
    except:
        pass
    try:
        shutil.rmtree('ChromeExtensions')
    except:
        pass
    try:
        os.remove('Log.txt')
    except:
        pass
# task5
def freeTool():
    os.startfile('HungHT1890\FreeTools.url')
# task6
def paidTools():
    os.startfile('HungHT1890\PaidTools.url')
# task7
def lienhe():
    os.startfile('HungHT1890\Lienhe.url')
logo = '''Openbullet MMO - hungsaki2003@gmail.com
M??nh ch??? tinh ch???nh tools m???t ch??t ????? cho anh em d??? s??? d???ng ?????ng th???i tool ch???y t???i ??u h??n !
Tools v???n ???????c gi??? nguy??n theo nh?? s???n xu???t !
C??c l???a ch???n:
1: Ch???y tools Openbullet
2: Xem h?????ng d???n s??? d???ng
3: Fix L???i Tools Openbullet (Ch?? ?? --> ??i???u n??y s??? x??a m???i d??? li???u!)
4: Reset Openbullet
5: Free Tools
6: Mua tools
7: Li??n h??? m??nh
8: Tho??t
\nT??i ch???n c??i n??y: '''
while True:
    userChoice = int(input(f'{xanh}{logo}'))
    if userChoice == 1:
        runOpenbullet()
    elif userChoice == 2:
        tutorialTools()
    elif userChoice == 3:
        fixError()
    elif userChoice == 4:
        resetTools()
    elif userChoice == 5:
        freeTool()
    elif userChoice == 6:
        paidTools()
    elif userChoice == 7:
        lienhe()
    elif userChoice == 8:
        exit()
    else:
        pass
    os.system('cls')