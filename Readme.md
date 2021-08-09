# 採点斬り 2021バージョン(β版)

## 初めに
* 竹内俊彦氏作成の[採点革命](http://www.nurs.or.jp/~lionfan/freesoft_45.html)や島守睦美氏作成の[採点斬り](http://www.nurs.or.jp/~lionfan/freesoft_49.html)などの素晴らしいフリーソフトを参考に、現在の環境でも動く同様のソフトを作成しました。

* フリーソフトですが、著作権は放棄しません。
* 転載、再配布は自由ですが、バグ対応等もあるので、現在のページ(https://phys-ken.github.io/saitenGiri2021/)へのリンクを貼ってください。
* 無断で改造、商用利用は認めていません。
* なお、このソフトウェアの使用によって生じた一切の損害について責任を負わないものとし、フリー版・シェアウェア版を問わず、個別のバグ対応は一切行いませんのでご注意下さい。
* とは言っても、バグの報告をいただけた場合にはできる限り対応します。Githubのissueにあげてください。

## 使い方
1. [release](https://github.com/phys-ken/saitenGiri2021/releases)のページから、最新版をダウンロードしてください。`dist`フォルダの中身が、アプリになります。
1. `saitenGiriGiri.exe`と、`appfigs`を同じフォルダに保存してください。
1. 採点斬りを起動し、初期設定をしてください。同じ場所に、settingフォルダが展開されます。
1. 解答用紙を、`./setting/input`に保存してください。
1. 斬る範囲を決めてください。(1枚目の解答用紙がロードされます。)![gifアニメ](appfigs/1giri.gif)
    1. １箇所目は名前、２回目以降は設問になります。
    1. 範囲を決める際は、実寸で0.5cm程度余白があるように選択すると、スキャン時の微妙なブレにも対応できると思います。
    1. 決まったら、`入力終了`を押してください。
1. 斬ります。裏側で動作しています。進み具合が気になる場合は、こっそり起動しているターミナルをみると、進捗のログが表示されています。
    1. このタイミングで、裏では`saiten.xlsx`が作成されています。
1. いよいよ採点です。少しUIがわかりづらいのですが、ご容赦ください...!![gifアニメ](appfigs/2saiten.gif)
    1. 点数を数字キーで入力します。
    1. 矢印キーで、`次へ進む・前に戻る`ができます。
    1. shift を押すと、`skip` できます。`skip`とした項目は採点ボタンを押しても採点されず、次回選択時にまた出てきます。
    1. 採点実行を押すと、得点をつけた項目が採点され、`setting/output`の中にある`saiten.xlsx`も更新されます。
        1. `saiten.xlsx`を起動している状態で**採点実行**をすると、動作がクラッシュします。

## Q&A
* もし採点を間違えたら?
  * 採点の点検機能が実装できませんでした。`setting/output/Q_000X`の中に、配点ごとにフォルダが作成されています。お手数ですが、自分でフォルダ内を漁って、画像ファイルを`setting/output/Q_000X`の直下に保存して、再度採点をしてください。

## 今後の計画
* UIをもっとわかりやすくしたいと思っています。

## 謝辞
* 参考にしたサイトがありすぎて、まとめられていません。