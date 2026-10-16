#### メッセージ詳細度 (Verbosity)

**`verbose`** は、より詳細な解説メッセージを有効にします。メッセージログが騒がしく感じられる場合は無効（off）にしてください。

**スターター向け設定ファイル例 (.nethackrc)。** 上記の推奨設定をまとめた数行の構成例です：

```
OPTIONS=statushilites
OPTIONS=hilite_status:hitpoints/<66%/yellow/<50%/orange/<33%/red&bold/<15%/red&inverse
OPTIONS=hilite_status:hunger/Satiated/yellow/Hungry/orange/Weak/red&bold/Fainting/red&inverse/Fainted/red&inverse+blink
MENUCOLOR=" cursed "=red
MENUCOLOR=" blessed "=cyan
OPTIONS=force_invmenu,pile_limit:5
OPTIONS=paranoid_confirmation:+attack quit
OPTIONS=autopickup,pickup_types:$?!=/
OPTIONS=pickup_burden:unencumbered
```

**curses によるパネル分割 UI。** さらに大幅なインターフェースの進化を望む場合、**curses** ウィンドウインターフェースを有効にしてビルドされた NetHack バイナリが必要です（標準的な 5.0 端末ビルドには含まれていない場合があります）。利用可能な場合、curses は端末内に整然としたパネル分割 UI を描画します。設定ファイルに `windowtype:curses`、`align_message:right`、`align_status:bottom`、`perm_invent`、`windowborders` を指定し、120×40 の広めのターミナルを開けば、常時表示のインベントリカラム、複数行のメッセージパネル、そして枠線で区切られたステータスとマップ領域が手に入ります（通常の tty NetHack では、何を設定してもメッセージ行は常に最上行の行0に固定されます）。

