HANDS = {1:'グー', 2:'チョキ', 3:'パー'}


def select_hand():
    """
    コンピュータの手をランダムに決める
    :return: HANDSの中のいずれか
    """
    import random
    pass

    chand = random.choice(1,3)

def judgement(player, computer):
    """
    じゃんけんの勝敗を判定する
    :param player: HANDSの中のどれか
    :param computer: HANDSの中のどれか
    :return: プレイヤーが勝ちの場合は1,あいこは0,負けは-1を返す
    """
    pass
    if computer == 1:
        if player == 1:
            print("0")
        elif player == 2:
            print("-1")
        elif player == 3:
            print("1")
    elif computer == 2:
        if player == 1:
            print("1")
        elif player == 2:
            print("0")
        elif player == 3:
            print("-1")
    elif computer == 3:
        if player == 1:
            print("-1")
        elif player == 2:
            print("1")
        elif player == 3:
            print ("0")





def save_score(result):
    """
    'score,txt'に戦績を保存
    win:x lose:y draw:zのディクショナリデータを保存する
    :param result:
    :return:
    """
    pass


if __name__ == '__main__':
    player = int (input('グー(1)/チョキ(2)/パー(3)を選んでください(数字): '))
    computer = select_hand()
    result = judgement(player, computer)
    # コンピュータの手と勝敗の結果を表示

    save_score(result)