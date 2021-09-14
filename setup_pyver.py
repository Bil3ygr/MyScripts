# coding: utf-8

import sys
import traceback
import winreg
# make sure both python2 and python3 install pywin32, the newests version of python2's pywin32 is 228
import win32con
import win32gui

regpath = r'SYSTEM\CurrentControlSet\Control\Session Manager\Environment'

def get_reg():
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, regpath, 0, winreg.KEY_READ)
    value, _ = winreg.QueryValueEx(key, 'Path')
    winreg.CloseKey(key)
    return value


def set_reg(value):
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, regpath, 0, winreg.KEY_WRITE)
    winreg.SetValueEx(key, 'Path', 0, winreg.REG_EXPAND_SZ, value)
    winreg.CloseKey(key)


def main(ver):
    try:
        paths = get_reg().split(';')
    except:
        traceback.print_exc()
        return 1

    if ver == 27:
        version = 'Python27'
    elif ver == 36:
        version = 'Python36'
    elif ver == 37:
        version = 'Python37'
    else:
        return 1

    for idx, path in enumerate(paths[:]):
        if version in path:
            paths.pop(idx)
            paths.insert(0, path)
    try:
        set_reg(';'.join(paths))
    except:
        traceback.print_exc()
        return 1
    print('change python version to %s, start broadcast...' % ver)
    try:
        win32gui.SendMessageTimeout(win32con.HWND_BROADCAST, win32con.WM_SETTINGCHANGE, 0, 'Environment', win32con.SMTO_ABORTIFHUNG, 3000)
    except:
        traceback.print_exc()
        return 1
    print('broadcast finished.')
    return 0


if __name__ == '__main__':
    try:
        ret = main(int(sys.argv[1]))
        if ret:
            exit(ret)
    except:
        traceback.print_exc()
        exit(1)
