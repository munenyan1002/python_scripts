import pyautogui as pgui
import webbrowser
from time import sleep

#redmineのログイン画面を新しいタブで開く
url = "http://spcdev:83/redmine/login?back_url=http%3A%2F%2Fspcdev%3A83%2Fredmine%2Fmy%2Fpage"
webbrowser.open(url, 1)

'''
移動させたいマウスの座標を入れる
x→X座標
y→y座標
'''
x, y =923, 450

#redmineの[ログイン]ボタンへマウス移動
pgui.moveTo(x, y, duration=0.25)

#Webページが開いてからクリックしたいので、10秒待つ
sleep(5)

#[ログイン]ボタンをクリック
pgui.click(x, y)


