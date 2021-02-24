# http://tinyurl.com/hll6t3q

answer = input("あなたの好きな映画は何ですか。：")
with open("fav_movie.txt", "w", encoding="utf-8") as f :
    f.write(answer)
    
