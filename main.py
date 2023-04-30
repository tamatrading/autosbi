# これはサンプルの Python スクリプトです。

# Shift+F10 を押して実行するか、ご自身のコードに置き換えてください。
# Shift を2回押す を押すと、クラス/ファイル/ツールウィンドウ/アクション/設定を検索します。

import  myform
import form

def print_hi(name):
    # スクリプトをデバッグするには以下のコード行でブレークポイントを使用してください。
    print(f'Hi, {name}')  # Ctrl+F8を押すとブレークポイントを切り替えます。


# ガター内の緑色のボタンを押すとスクリプトを実行します。
if __name__ == '__main__':

    #--- 入力フォームを表示する
    print_hi('PyCharm')
    myform.init("SBI 入力フォーム")
    print(f"{myform.g_name},{myform.g_pass},{myform.g_code},{myform.g_go}")

    if myform.g_go == 1:
        print(f"{myform.g_name},{myform.g_pass},{myform.g_code},{myform.g_go}")




# PyCharm のヘルプは https://www.jetbrains.com/help/pycharm/ を参照してください
