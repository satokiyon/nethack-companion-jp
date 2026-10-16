# -*- coding: utf-8 -*-
"""
Generate segments for step_365 to step_374 (Index and Acknowledgements).
"""
import os
import json

with open(os.path.join("spoilers", "companion.md"), "r", encoding="utf-8") as f:
    companion_lines = f.readlines()

with open(os.path.join("docs", "translation_progress.json"), "r", encoding="utf-8") as f:
    progress = json.load(f)

# step_365 to step_373: Index of Useful Knowledge (LaTeX print-only index blocks)
# We retain the LaTeX indexing structure while updating section titles if present
for s in progress["segments"]:
    idx = int(s["id"].split("_")[1])
    if 365 <= idx <= 373:
        start = s["start_line"] - 1
        end = s["end_line"]
        chunk = "".join(companion_lines[start:end])
        # Replace the header line if it starts with ## Index of Useful Knowledge
        chunk = chunk.replace("## Index of Useful Knowledge", "## 有用な知識の索引 (Index of Useful Knowledge) {#index-of-useful-knowledge}")
        out_path = os.path.join("docs", "segments_jp", f"{s['id']}.md")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(chunk.strip() + "\n")
        print(f"Generated {out_path}")

# step_374: Acknowledgements
ack_content = """### 謝辞 (Acknowledgements)
<!-- audit
2026-05-19:
- NetHack 1987, Fenlason -> Brouwer -> Stephenson lineage verified (Wikipedia, dat/history)
- DevTeam founders, Izchak Miller died 1994, Hack 1982 origin all verified
- WCST acronym is not expanded in the original Waterman file; Wheaton, IL distribution started 1991 (pdwaterman.com)
- Kevin Hugo is on the official 5.0 core team list (dat/history:314)
- nethackwiki.com returned 403, so wiki article counts and some spoiler-author attributions are unverified
-->

NetHack は 1987 年以来、世界中のプレイヤーによってプレイされ、罵倒され、愛され、そして詳細に記録され続けてきました。ゲーム本体は、現存する最長寿のオープンソースプロジェクトの一つを維持し続けてきた開発者の緩やかな集団である「NetHack DevTeam」の成果です。しかし、この迷宮で実際に生き延びるための攻略法や知恵、ドキュメントの数々は、プレイヤーたち自身の手によって築き上げられてきました。

草創期、知識は Usenet のニュースグループ **RGRN**（rec.games.roguelike.nethack）を通じて共有されました。何千人ものプレイヤーが質問を投稿し、戦略について議論し、自ら進んで秘密を明かそうとしないゲームの知識を少しずつ共有財産として蓄積していったのです。それは Wiki も Reddit も Discord も存在しなかった時代の話です。コカトリスの死体を武器として振り回せるかどうかを知りたければ、RGRN の過去ログを検索し、自分より先に誰かが試していることを祈るしかありませんでした。そして大抵の場合、先人がすでに試していたのです。

RGRN はコミュニティに多くの用語をもたらしました。**YASD**（*Yet Another Stupid Death* / またしてもくだらない死）は、「やってはならないと分かっていたはずのこと」で死亡した際に投稿される反省記事です。**YAFAP**（*Yet Another First Ascension Post* / またしても最初の昇天報告）は、ついにゲームをクリアした際の歓喜の報告です。どちらの伝統も、現在の Wiki、Reddit、Discord のコミュニティへと受け継がれています。

それらの対話から、最初の「スポイラー（解析・攻略情報）ファイル」が生まれました。あらゆるアイテム、あらゆるモンスター、あらゆる相互作用を網羅したプレーンテキストの目録です。それらは手作業で書き起こされ、ゲームのソースコードと照合され、惜しみなく無償で共有されました。

本ガイドは、彼らの偉大な先駆的成果の上に成り立っています。特に：

**Kevin Hugo 氏**は NetHack 3.2.2 向けの最初の包括的なスポイラーセットを編纂し、あらゆるアイテム分類、モンスターのステータス、呪文の計算式、スコア計算を極めて几帳面にまとめ上げました。**Dylan O'Donnell 氏**はその全セットを 3.4.3 向けに改訂・拡張し、数年間にわたって維持しました。両氏によるスポイラー群は、薬、巻物、杖、指輪、魔除け、道具、武器、防具、アーティファクト、食料、モンスター、呪文などを網羅する全38ファイルからなる不動の決定版リファレンスとなりました。本ガイドの第4部および第5部に掲載されているデータ一覧表は、彼らの作業と照合・検証されています（BSD風ライセンスの下で公開）。

**Paul Waterman 氏**は 1991 年にウィートン大学で「WCST NetHack Spoilers」を執筆しました。これはゲーム全体を軽妙で主観的な語り口で解説した長大な単一ドキュメントでした。Hugo 氏と O'Donnell 氏が参照マニュアルを著したのに対し、WCST はまるで「旅行ガイドブック」でした。単に事象を説明するだけでなく、それにどう対処すべきかを説いたのです。これは本ガイドのトーンと構成における原初の着想となりました（本文の直接の引用はありません）。

**Kate Nepveu 氏**は steelypips.org を運営し、Hugo/O'Donnell スポイラー、RGRN の名作記事、そして自身の優れたガイド群（本ガイドの罠の章で引用したエルベレス FAQ など）をウェブ上で保存し続けました。Kate 氏の根気強いアーカイブ作業がなければ、Usenet の衰退とともに多くの貴重な知見が失われていたはずです。

さらに、以下の **RGRN コミュニティの執筆者たち**が、本ガイドの各節に情報を提供してくれた記事、FAQ、ガイドを寄稿してくれました：

アイテム識別 FAQ を著した **David Damerell 氏**。杖の識別ガイドを著した **Kieron Dunbar 氏**。即死スポイラーを編纂した **Trevor Powell 氏**。メデューサ対策ガイドを著した **Arien Malec 氏**。祈りガイドを著した **Matthew Lahut 氏**。[倉庫番](#sokoban)全8パターンの解答マップを作成した **Boudewijn Waijers 氏**。魔法書読解成功率を計算した **Steven Bush 氏**。店主の価格計算式を記録した **Gregory Bond 氏**。コンダクトを分類目録化した **Dion Nicolaas 氏**。風の精 FAQ を著した **David Goldfarb 氏**。経験値計算を記録した **Hojita Discordia 氏**。

そして Ray Chason 氏、Pat Rankin 氏、Geoduck 氏、Topi Linkala 氏、Geoffrey Eadon 氏、Roger Broadbent 氏、Sebastian Haas 氏、Jukka Lahtinen 氏をはじめ、「誰かこれを試した人はいる？」と問いかけ、その結果を報告してくれたニュースグループの無数の名無しの冒険者たちに深く感謝します。

**[NetHack Wiki](https://nethackwiki.com/)** は本ガイドにとって不可欠のリファレンスでした。2005 年に Sgeo 氏によって「WikiHack」として設立され、2010 年に独自ドメインへ移行した同サイトには、現在 5,000 件以上の記事が蓄積されています。制作者および管理者には Pasi Kallinen 氏、Drew Streib 氏、Alex Smith 氏、Shawn Moore 氏、George Koehler 氏、Tjr 氏、ZeroOne 氏、Ray Chason 氏らが名を連ねています。Wiki の [NetHack 5.0.0 ページ](https://nethackwiki.com/wiki/NetHack_5.0.0) はコミュニティの生きた更新履歴であり、本ガイドの 5.0 改訂における主たる情報源となりました。

現在多くのプレイヤーが集う**公開サーバー**は、[nethack.alt.org](https://alt.org/nethack/)（NAO: M. Drew Streib 氏と Pasi Kallinen 氏が運営する最長寿サーバー）および [Hardfought](https://hardfought.org/)（K2 氏が運営し、主要バリアントもホスト）です。どちらも無料でプレイでき、すべての昇天記録を保存しています。本ガイドで引用されている死因統計や昇天記録は、これら公開サーバーのデータに基づいています（NAO の [主な死因一覧](https://alt.org/nethack/topdeaths.html) 参照）。

Reddit の **[r/nethack](https://www.reddit.com/r/nethack/) コミュニティ** は、新世代のプレイヤーたちに向けて議論の場を提供し続けています。歴代のモデレーターたちは、ベテランと初心者が助言を交わし、昇天体験を共有し、最適な「願い」の選択について熱く議論できる温かいコミュニティを維持してきました。数千のスレッドを通じて受け継がれてきた集合知は、本ガイドの実戦的アドバイスに大きく反映されています。

そして何よりも、このゲームそのものが存在したからこそ、本ガイドが生まれました。
**[NetHack](https://www.nethack.org/)** は、Mike Stephenson 氏、Izchak Miller 氏、Janet Walz 氏によって設立された NetHack DevTeam により、1987 年から開発が続けられています。Izchak Miller 氏は 1994 年に惜しまれつつ世を去りました。[ノームの鉱山](#the-gnomish-mines) で彼の名を冠した店主（イズチャク）は、彼の遺した功績の大きさを今に伝えています。ソースコードは [github.com/NetHack](https://github.com/NetHack/NetHack) で公開されています。

ゲーム自体はさらに初期のローグライクに遡ります。**Hack** は 1982 年、リンカーン・サドベリー地域高校の授業プロジェクトとして Jay Fenlason 氏によって書かれ（Toy 氏と Wichman 氏の『Rogue』(1980) を下敷きにしています）、1980 年代半ばにかけて Andries Brouwer 氏によって拡張されました。NetHack は 1987 年に Brouwer 氏の Hack からフォークしました。**グリッドバグ**（マス目の格子状に住み、「昆虫」と「プログラムのバグ」を掛け、1982 年の映画『トロン』への敬意を込めたとされる直角移動モンスター）をはじめとする NetHack 固有のモンスターの多くは、Fenlason 氏のオリジナル Hack から受け継がれたものです。このダンジョンは、NetHack というゲームよりもさらに古い歴史を持っています。

開発の道のりは常に平坦だったわけではありません。2003 年 12 月のバージョン 3.4.3 の後、DevTeam は 12 年間もの長きにわたり沈黙を守りました。公には一切の発言を断ち、水面下で作業を続けていたのです。その間、コミュニティでは「*DevTeam は思考中である（The DevTeam is THINKING）*」というジョークが定着しました。ダンジョンは凍りつきました。新たなプレイヤーたちは 2003 年以来変わらない回廊へと降り立ち、変化のないゲームについて新たなスポイラーを書き、新たに記録された同じ死因で命を落としていきました。沈黙の 12年間に蓄積されたコミュニティの知恵は色褪せることなく役立ち続け、ゲームはたった1行の新しいコードが追加されることもなく、丸10年におよぶ新たな分析に耐えうるほどの奥深さを証明したのです。2015 年 12 月にバージョン 3.6 が登場し、それ以来活発な開発が続いています。

現在のチーム（Michael Allison, Ken Arromdee, David Cohrs, Jessie Collet, Kevin Hugo, Pasi Kallinen, Ken Lorber, Dean Luick, Patric Mueller, Pat Rankin, Derek S. Ray, Alex Smith, Mike Stephenson, Janet Walz, Paul Winner, Bart House, Warwick Allison の各氏）は、40年近くにわたりこのゲームを維持し、拡張し続けてきました。本書のすべての記述は、彼らの献身的な仕事の恩恵によるものです。

本ガイドのすべてのデータは、現在の NetHack 5.0.0 のソースコードと照合・検証されています。万一誤りがあれば、それはすべて編著者の責に帰するものです。

---

*『恐怖の迷宮への旅人の手引き (A Traveler's Companion to the Mazes of Menace)』 NetHack 5.0 ローンチ記念版*<br>
*編纂: David Bau、事実照合・検証: Claude 4.8 Opus*<br>
*日本語版翻訳・監修: Antigravity AI & NetHackJP Project*

*本著作物は [クリエイティブ・コモンズ 表示 - 継承 4.0 国際 (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/deed.ja) ライセンスの下で許諾されています。*
"""

step_374_path = os.path.join("docs", "segments_jp", "step_374.md")
with open(step_374_path, "w", encoding="utf-8") as f:
    f.write(ack_content.strip() + "\n")
print(f"Generated {step_374_path}")

