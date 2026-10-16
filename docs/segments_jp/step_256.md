#### ボーンズなし (Bonesless: 5.0新要素) {#bonesless-new-in-5.0}

<!-- audit
2026-05-19:
- bonesless achievement requires !flags.bones; you must turn bones loading off (topten.c:605)
- not encountering bones is a separate Miscellaneous enlightenment line, NOT the conduct (insight.c:439)
- you cannot get bonesless by luck alone
- show_conduct never lists lifesaving uses; there is no amulet-of-life-saving tracking (insight.c:2089-2200 show_conduct enumerates rerolling/food/atheist/weaphit/pacifist/illiterate/pets/genocides/polypiles/polyselfs/wishes — no lifesaving counter; u.uconduct has no lifesave field)
- `bones` is set_in_config: config file or command line only, not in-game O menu (optlist.h:213-215)
- !flags.bones blocks both save (bones.c:360) and load (bones.c:642) — cuts both directions
- "never encountered any bones levels" enlightenment requires flags.bones true AND u.uroleplay.numbones==0 (insight.c:439-441)
-->

過去のプレイヤー（または自分自身）の亡骸や遺留品から一切の遺産を受け継ぐことなくプレイします。設定ファイルに `OPTIONS=!bones` を記述します（[セーブとボーンズ](#saving-and-bones) を参照）。単に偶然ボーンズ階層に遭遇しなかっただけのプレイは、この公式コンダクトの対象にはなりません（明示的にオプションでボーンズ生成を無効化しておく必要があります）。
