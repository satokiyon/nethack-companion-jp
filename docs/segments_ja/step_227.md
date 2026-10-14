---

### 設定のカスタマイズ {#options-worth-knowing-about}

<!-- audit
2026-07-30: audited with Advanced Controls vs NetHack-5.0 source (options.c); option names/effects/defaults verified. No corrections here.
-->

NetHack のデフォルト設定は堅実ですが、以下の5つのオプションを設定することで、よくある入力ミスを防止し、危険を直感的に察知できるようになります。ゲーム中に `mO` を入力して全設定メニューから切り替えるか、設定ファイル（macOS/Linux なら `~/.nethackrc`、Windows なら `%USERPROFILE%\NetHack\.nethackrc`、または環境変数 `NETHACKOPTIONS`）に記述して恒久化してください。

もし5つだけ変更するとしたら、以下の設定をおすすめします：

1. **HPと空腹度のカラー表示**：数値を確認する前に、色彩で直感的に危険を察知できるようにする。
2. **`paranoid_confirmation:+attack quit`**：致命的なタイプミスによる暴発や誤終了を防ぐ。
3. **`autopickup` と `pickup_types:$?!=/`**：無用な石や重い鎧を拾いすぎることなく、軽量で有用なアイテムだけを自動収集する。
4. **`pickup_burden:unencumbered`**：アイテムの拾得によって気付かぬうちに移動速度が低下（重荷）するのを防ぐ。
5. **呪われたアイテムをメニューで赤色表示**：危険な選択肢が一目で危険だとわかるようにする。

さらにもう1つ、インターフェースではなくキャラクター作成時に関わる設定があります。`OPTIONS=reroll` を設定すると、最初に振られた初期能力値と初期所持品を破棄して、別の組み合わせへと振り直すことができます。最初の手札にこだわりたいプレイヤーには快適な機能ですが、どのような初期値であっても、ゲーム開始後の決断ほど重要なものはありません。

