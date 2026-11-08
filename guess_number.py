# 数当てゲーム
# コンピュータが 1〜100 の数をひとつ決めるので、それを当てるゲームです。
#
# このプログラムで練習できること:
#   1. import     … 他の人が作った便利な機能を読み込む
#   2. 変数       … 値に名前をつけて覚えておく
#   3. input/print … ユーザーから入力を受け取り、結果を表示する
#   4. if/elif/else … 条件によって処理を分ける
#   5. while      … 同じ処理をくり返す
#   6. 関数 (def) … 処理のかたまりに名前をつける
#   7. try/except … エラーが起きたときに落ちないようにする

import random  # 乱数（ランダムな数）を作るための機能


def ask_number():
    """ユーザーに数を入力してもらい、整数にして返す関数。"""
    while True:  # 正しい数が入力されるまでくり返す
        text = input("1〜100 の数を入力してください: ")
        try:
            number = int(text)  # 文字列を整数に変換（できなければエラーになる）
        except ValueError:
            print("数字を入力してね。")
            continue  # ループの最初に戻る

        if 1 <= number <= 100:
            return number  # 正しい数なので関数から返す
        print("1〜100 の範囲で入力してね。")


def play():
    """ゲームを1回遊ぶ関数。"""
    answer = random.randint(1, 100)  # 1〜100 のランダムな整数
    count = 0  # 何回目の挑戦かを数える変数

    print("=== 数当てゲーム ===")

    while True:
        guess = ask_number()
        count = count + 1  # 挑戦回数を1増やす（count += 1 とも書ける）

        if guess < answer:
            print("もっと大きいです。")
        elif guess > answer:
            print("もっと小さいです。")
        else:
            print(f"正解！ {count} 回で当たりました。")
            break  # ループを抜けてゲーム終了


# このファイルを直接実行したときだけ play() を呼ぶ、というお決まりの書き方
if __name__ == "__main__":
    play()
