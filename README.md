まず、

アクセス、表示できるようにする。
次にデータを使って文字起こしできるようにする。既存のファイルを使う。
次にアップロードしたやつでできるようにする。

これで送ることはできる。
testの方は書き方がよくわかってないのでしばらくこれで様子をみたい。
curl -X POST "localhost:8000/uploadAudio" \
    -F "file=@test.wav"
https://weblabo.oscasierra.net/curl-post/


これ、turbo以上のモデルくらいから文字起こしがよくなる。
ただ、8GB以上のRAMを持っていないと使えないので注意。

https://github.com/openai/whisper
文字起こしの精度や基本的な使い方はこれに基づいてできる。


file: UploadFile = File(...)で引数にしてpostすればよさそう。
高速化するためには、受け取ったファイルをdbにぶちこんで直接読み込むか？
ある程度サイズのあるファイルは、メモリ確保したやつでやるか？
そもそもpythonの変数のメモリ確保って動的なのか？スタック領域とかあるのかな？
少なくとも今回でM2のMac 8GBではできなかったから、RAM16GB以上のこのPCかサーバーでやるしかない。

<<<<<<< HEAD
もっとオプションとか調べて高速化と精度向上したい。
=======


最終的にはこんな感じにdockerでDBのヘルスチェックとかしたい
https://docs.github.com/ja/enterprise-server@3.17/actions/tutorials/use-containerized-services/create-postgresql-service-containers


docker cp postgres:/var/lib/postgresql/data/postgresql.conf ./my_postgresql.conf
docker cp postgres:/var/lib/postgresql/data/pg_hba.conf ./my_pg_hba.conf

でとってくる

他のfastapiの記事とかいろいろ見た感じ、
api
├── __init__.py
├── main.py
├── schemas
├── routers
├── models
└── cruds
docker
├── api
└── db
大まかにはこういうディレクトリがいいと思う。

routers
   エンドポイントに届くリクエストにどんな処理するかと
schemas
   APIレスポンスのの型定義
models
   DBのテーブル定義。sqlalchemyとかで
cruds
   エンドポイントに届いたリクエスト、routerで処理するDBに対しての関数定義とか。  

やること順番
ディレクトリ変える
上にあげたディレクトリ順に処理書いてく。




fastapiに届いたバックエンドの処理フローを考える上で
ざっくりした流れ的には、

postでファイル届く、
1,ディレクトリに音声格納 && random_id 発行

2,格納した音声に対して文字起こし開始

3,文字起こしstr格納 && done_flag == true

4,いつかは消す


まず、1を考える。

やること
db に











>>>>>>> 6d5cce9 (Postgreさんを召喚、方針ちょびっと)
