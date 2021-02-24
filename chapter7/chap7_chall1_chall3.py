# http://tinyurl.com/z2m2115

shows = ["ウォーキング・デッド",
         "アントラージュ",
         "ザ・ソプラノズ",
         "ヴァンパイア・ダイアリーズ"]

#リストの要素をそれぞれ出力する。
for show in shows :
    print(show)

#リストの要素をそれぞれ。インデックス値と一緒に出力する。
for index, show in enumerate(shows) :
    print(index)
    print(show)
