#### ステータス表示の強調 (Status display)

**`hilite_status`** は、最下行のステータスライン（HP、空腹度、ACなど）に閾値ごとのカラールールを適用して色付けします。ルールを定義することでハイライトが有効になります。各完全なルールは1行に記述してください：

```
OPTIONS=statushilites
OPTIONS=hilite_status:hitpoints/<66%/yellow/<50%/orange/<33%/red&bold/<15%/red&inverse
OPTIONS=hilite_status:hunger/Satiated/yellow/Hungry/orange/Weak/red&bold/Fainting/red&inverse/Fainted/red&inverse+blink
```

末尾にバックスラッシュを置いてルールを複数行に分割しないでください。パーサーが空白を挿入してしまい、後続のフィールドが不正なオプションとして拒絶されてしまいます。

**`menucolors`** は、メニュー項目を正規表現パターンで色付けします。最も有用なルールはBUCタグの色分けであり、呪われたアイテムが赤色で警告され、祝福されたアイテムがシアン色で表示されるようになります：

```
MENUCOLOR=" cursed "=red
MENUCOLOR=" blessed "=cyan
```

前後の半角スペースが重要です。スペースを置くことで、`"uncursed"`（無呪）の中間に含まれる `"cursed"` に誤ってマッチするのを防ぎます。

**`force_invmenu`** は、所持品から選択を求めるコマンド（読む、置く、構える等）を実行した際、デフォルトの1文字プロンプト（*「どれを読みますか？ [j-k または ?*]」*）の代わりに、該当アイテムの一覧ポップアップメニューを開くようにします。候補が一目で確認でき、1キーで選択できるため、事前に `?` を押したり英文字を記憶しておく必要がなくなります。

**`pile_limit:5`** はデフォルト値です。同じマスに5個以上のスタックがある場合、個別のリストではなく要約が表示されます。`pile_limit:0` に設定すると、常にすべてのアイテムを一覧表示します。

