# http://tinyurl.com/hll6t3q

import csv

movies = [["トップ・ガン", "リスキー・ビジネス", "マイノリティ・レポート"],
          ["タイタニック", "ザ・レヴェナント", "インセプション"],
          ["トレーニング・デイ", "マン・オン・ファイア", "フライト"]]

with open("movies_JP.csv", "w", encoding="shift_jis", newline="") as f :
    w = csv.writer(f, delimiter=",")
    for movie_list in movies :
        w.writerow(movie_list)
