まず、

アクセス、表示できるようにする。
次にデータを使って文字起こしできるようにする。既存のファイルを使う。
次にアップロードしたやつでできるようにする。

これで送ることはできる。
testの方は書き方がよくわかってないのでしばらくこれで様子をみたい。
curl -X POST "localhost:8000/uploadAudio" \
    -F "file=@test.wav"
https://weblabo.oscasierra.net/curl-post/
