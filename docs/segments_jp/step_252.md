#### 赤貧 (Pauper: 5.0新要素)

<!-- audit
2026-05-19:
- Pauper is set_in_config: rcfile or NETHACKOPTIONS env only, not in-game O menu (optlist.h:559)
- ini_inv early-return suppresses starting items only, not the pet (u_init.c:1308-1309)
- Pauper does NOT suppress the starting pet (dog.c:219-229; only pettype:none does)
- dog.c:262-267 skips the pony saddle for Pauper
- Cleric, Knight, Monk start knowing SPE_PROTECTION (pauper_reinit, u_init.c:890-922)
- Cave Dweller starts knowing FLINT (pauper_reinit, u_init.c:890-922)
- Protection book is a load-bearing early-game pickup for those three roles
- nudist cascade triggers when pauper is set (options.c:5290-5293)
- end-of-game string at insight.c:2117-2119; xlogfile at topten.c:604
-->

完全に何もない無一文の状態でゲームを開始します：所持金ゼロ、所持品ゼロ、防具なし、初期武器なし。設定ファイルに `OPTIONS=pauper` を記述します（設定ファイルまたは環境変数 `NETHACKOPTIONS` からのみ設定可能であり、ゲーム内の `O` メニューでは切り替えられません）。赤貧を設定すると自動的に裸族（Nudist）も有効化されます。これは後から失われることのない恒久的コンダクトです：後からゴールドを拾ったり使ったりすることは禁じられておらず、「何もない状態でスタートしたこと」そのものが達成条件となります。

開幕が完全に不可能になるのを防ぐため、わずかな補償措置が与えられます：未消費の武器スキルスロットが2枠与えられ、さらに各職業ごとに象徴的な呪文またはアイテムを1つ最初から認知しています。魔法使いは「衝撃」を、治療師は「回復」を、司祭・騎士・武闘家は「防護」を（司祭は聖水も認知）、考古学者は「試金石」を、洞窟人は「火打石」を、盗賊と観光客は「麻袋」を、侍は「軍糧丸」の食料をあらかじめ認知しています。浅い階層に配置された [補給コンテナ](#supply-containers) が、あなたの最初の装備セットの多くを賄ってくれるはずです。

