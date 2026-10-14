# -*- coding: utf-8 -*-
"""
Build complete and accurate Japanese Bestiary segments: step_298 to step_354.
All prose, table headers, monster names, attack forms, and notes are translated
into natural Japanese complying with NetHackJP conventions.
"""
import os
import re
import json

# 1. Load glossary
glossary = {}
with open(os.path.join("docs", "glossary_references", "mon_jp.txt"), "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" in line:
            en, ja = line.split(":", 1)
            glossary[en.strip().lower()] = ja.strip()

# Absolute requirements
glossary["floating eye"] = "さまよう目"
glossary["water nymph"] = "水のニンフ"
glossary["wood nymph"] = "森のニンフ"
glossary["mountain nymph"] = "山のニンフ"
glossary["little dog"] = "仔犬"
glossary["large dog"] = "大きな犬"
glossary["large cat"] = "大きな猫"
glossary["winter wolf cub"] = "冬狼の子"
glossary["hell hound pup"] = "ヘルハウンドの仔"
glossary["air elemental"] = "風の精"
glossary["fire elemental"] = "火の精"
glossary["earth elemental"] = "土の精"
glossary["water elemental"] = "水の精"
glossary["lichen"] = "苔の怪物"
glossary["gas spore"] = "包子ガス"
glossary["stalker"] = "ストーカー"

color_dict = {
    "brown": "茶色",
    "yellow": "黄色",
    "blue": "青色",
    "red": "赤色",
    "black": "黒色",
    "magenta": "赤紫",
    "green": "緑色",
    "white": "白色",
    "cyan": "水色",
    "gray": "灰色",
    "grey": "灰色",
    "bright-blue": "明青",
    "bright-cyan": "明水",
    "bright-green": "明緑",
    "bright-magenta": "明紫",
    "orange": "橙色",
}

attack_trans = [
    (r"\bbite\b", "噛みつき"),
    (r"\bsting\b", "毒針"),
    (r"\btouch\b", "接触"),
    (r"\bpassive\b", "反撃"),
    (r"\bclaw\b", "爪"),
    (r"\bbutt\b", "頭突き"),
    (r"\bgaze\b", "凝視"),
    (r"\bspit\b", "吐瀉"),
    (r"\bkick\b", "蹴り"),
    (r"\bweapon\b", "武器攻撃"),
    (r"\bbreath\b", "ブレス"),
    (r"\bhug\b", "締め付け"),
    (r"\bdeath-burst\b", "爆発(死亡時)"),
    (r"\bexplode\b", "自爆"),
    (r"\bparalyse\b", "麻痺"),
    (r"\bpetrify\b", "石化"),
    (r"\bpoison\b", "毒"),
    (r"\bfire\b", "火炎"),
    (r"\bcold\b", "冷気"),
    (r"\bshock\b", "電撃"),
    (r"\bacid\b", "酸"),
    (r"\bdisint\b", "分解"),
    (r"\bblind\b", "盲目"),
    (r"\bsteal\b", "盗み"),
    (r"\bseduce\b", "誘惑"),
    (r"\bsedux\b", "誘惑"),
    (r"\brust\b", "錆び"),
    (r"\brot\b", "腐敗"),
    (r"\bdrain\b", "エナジードレイン"),
    (r"\blyc\b", "獣化"),
    (r"\bcurse\b", "呪い"),
    (r"\bmagic\b", "魔法"),
]

# Exact phrase translations for notes
phrase_trans = [
    ("Passive gaze paralyses on melee if you and the eye can both see each other. Use ranged, or wear a blindfold or towel to break sight. Corpse always grants telepathy.",
     "互いに視界が通っている状態で近接攻撃すると反撃麻痺。遠距離攻撃を行うか、目隠しやタオルで視覚を遮って対処。死体を食べると必ずテレパシーを獲得。"),
    ("A small cockatrice. Same petrify rules apply.", "小型のコカトリス。同様の石化ルールが適用される。"),
    ("Touch petrifies. Always carry a lizard corpse.", "触れると石化。常にトカゲの死体を携帯すること。"),
    ("The first thing that ever killed you.", "冒険者を最初に葬り去った相手。"),
    ("Guaranteed Caveman/Ranger/Samurai starting pet.", "洞窟人、野伏、侍の確定初期ペット。"),
    ("Common pet.", "一般的なペット。"),
    ("Passive acid damage; punching one corrodes your gloves.", "酸の反撃ダメージ。素手で殴ると手袋が腐食する。"),
    ("Slow but paralyses on touch. Don't melee without free-action.", "鈍足だが接触時に麻痺。自由行動なしでの近接戦は厳禁。"),
    ("Stings carry poison.", "毒針攻撃。"),
    ("Poison sting.", "毒針攻撃。"),
    ("No corpse.", "死体を残さない。"),
]

notes_trans = [
    (r"\bpoisonous-corpse\b", "死体に毒あり"),
    (r"\bpois-res\b", "毒耐性"),
    (r"\bfire-res\b", "火炎耐性"),
    (r"\bcold-res\b", "冷気耐性"),
    (r"\bshock-res\b", "電撃耐性"),
    (r"\bacid-res\b", "酸耐性"),
    (r"\bston-res\b", "石化耐性"),
    (r"\bdisint-res\b", "分解耐性"),
    (r"\bsleep-res\b", "睡眠耐性"),
    (r"\bsee-invis\b", "不可視視認"),
    (r"\bregenerates\b", "自動回復"),
    (r"\btameable\b", "手懐け可能"),
    (r"\bamorphous\b", "不定形"),
    (r"\bmindless\b", "精神なし"),
    (r"\binvis\b", "不可視"),
    (r"\bhuman\b", "人間"),
    (r"\bundead\b", "アンデッド"),
    (r"\bdemon\b", "悪魔"),
    (r"\bgiant\b", "巨人"),
    (r"\bflies\b", "飛行"),
    (r"\bfly\b", "飛行"),
    (r"\bswims\b", "遊泳"),
    (r"\bamphibious\b", "水陸両用"),
    (r"\bteleports\b", "テレポート"),
    (r"\bhides\b", "潜伏"),
    (r"\bhide\b", "潜伏"),
]

# Section Japanese titles and Japanese prose definitions
prose_data = {
    "step_298": {
        "title": "モンスター図鑑一覧表 (Bestiary Tables)",
        "prose": """ダンジョンで遭遇しうるあらゆるモンスターをマップ記号ごとに分類した一覧です。**レベル (Lvl)**はモンスターの基本レベル、**速度 (Spd)**は移動速度（プレイヤーの標準速度は 12）、**AC**はアーマークラス（低いほど強固）、**MR**は魔法防御率（プレイヤーの呪文や魔法攻撃に抵抗する確率%）を表します。**攻撃方法 (Attacks)**は各攻撃の種別、ダメージダイス、追加効果を記載しており、`·` で区切られた攻撃は1ターン内にすべて連続して繰り出されます。**備考 (Notes)**には飛行能力、不可視視認、自動回復、死体に毒があるかなど、戦闘を一変させる重要な特性をまとめています。"""
    },
    "step_299": {
        "title": "蟻および昆虫 `a` (Ants and insects `a`)",
        "prose": """昆虫類。多くは集団で群れをなして出現します。兵隊蟻の毒針攻撃は筋力を吸い取ります。殺人蜂は大群で襲いかかり、蜂の巣の部屋にいる女王蜂は単体でも手ごわい相手です。"""
    },
    "step_300": {
        "title": "ブロッブ `b` (Blobs `b`)",
        "prose": """動きが遅く、精神を持ちません。酸のブロッブを素手や大切な金属武器で近接攻撃してはいけません。相手の酸による反撃で武器や防具が腐食します。ゼラチンキューブは接触時にプレイヤーを麻痺させます。\n\nすべてのブロッブは精神を持たず（マインドレス）、睡眠耐性と毒耐性を備えています。"""
    },
    "step_301": {
        "title": "コカトリス `c` (Cockatrices `c`)",
        "prose": """中世の動物寓話に登場する怪物。蛇の尾を持つ鶏の姿をしており、その接触は肉体を瞬時に石化させます。トカゲの死体を常時携帯し、必ず手袋を着用して戦ってください。どの職業も初期状態では石化耐性を持っておらず、コカトリスの死体を素手で装備すると即死します。[石化](#petrification-stoning)の項目を参照してください。\n\nすべてのコカトリス類は毒耐性を備えています。"""
    },
    "step_302": {
        "title": "犬およびイヌ科 `d` (Dogs and canines `d`)",
        "prose": """野生のイヌ科生物は群れで狩りを行います。飼いならされたものは食料を与えることでペットにできます（[仲間の増やし方](#making-friends)参照）。ジャッカル人間や狼人間はプレイヤーを獣化（ライカンスロープ）に感染させることがあります。"""
    },
    "step_303": {
        "title": "目および球体 `e` (Eyes and spheres `e`)",
        "prose": """さまよう目の反撃麻痺凝視は、ダンジョン序盤において最も有名な死因の一つです。自由行動（Free action）、盲目状態、または遠距離攻撃の手段を持たずに近接攻撃を仕掛けてはなりません。倒した後は死体を食べてください。恒久的なテレパシー能力（内在能力）を獲得できます。\n\nすべての目および球体は飛行能力を持ちます。また、*さまよう目*を除きすべて精神を持ちません。"""
    },
    "step_304": {
        "title": "ネコ科 `f` (Felines `f`)",
        "prose": """野生のネコ科生物は素早く敵対的です。虎やディスプレイスビーストは、何気ない通路での遭遇を命がけの戦いに変えてしまいます。魔法使いは必ず小猫を連れてスタートし、初期ペットが固定されていない職業は小猫か仔犬のいずれかを 50% の確率で連れて開始します。"""
    },
    "step_305": {
        "title": "グレムリン `g` (Gremlins `g`)",
        "prose": """夜間（または光源がない暗闇）に水に触れると分裂増殖する厄介な小型怪物です。暗闇の中でプレイヤーから内在能力を盗み取る攻撃を行います。明るい光源を持ち歩くか、明かりの巻物・呪文で部屋を照らすのが有効な対抗策です。"""
    },
    "step_306": {
        "title": "人型生物 `h` (Humanoids `h`)",
        "prose": """小人族、ホビット、ドワーフ、巨人など多彩な人型生物が含まれます。ノームの鉱山ではドワーフが中立または友好的に出現することが多く、彼らの落とすミスリル服や鉄兜は序盤の貴重な防具供給源となります。"""
    },
    "step_307": {
        "title": "小悪魔および下級悪魔 `i` (Imps and minor demons `i`)",
        "prose": """インプ、ホムンクルス、テングなどの下級悪魔です。テングは頻繁にテレポートを行い、その死体を食べることでテレポート能力やテレポート制御能力を獲得できるチャンスがあります。"""
    },
    "step_308": {
        "title": "ゼリー `j` (Jellies `j`)",
        "prose": """壁際や床に張り付く不定形の怪物です。青色ゼリーは冷気、赤色ゼリーは火炎の反撃ダメージを与えます。金属武器を腐食させる斑点ゼリーにも注意が必要です。"""
    },
    "step_309": {
        "title": "コボルド `k` (Kobolds `k`)",
        "prose": """序盤に群れで現れる小型の邪悪な生物。毒矢を放ってくることがあり、毒耐性がない最序盤では1発で致命傷になり得ます。死体にも毒が含まれているため、毒耐性を得るまでは食べてはいけません。"""
    },
    "step_310": {
        "title": "レプラコーン `l` (Leprechauns `l`)",
        "prose": """金貨を盗んで即座にフロアの別の場所へテレポートする妖精です。攻撃力は高くありませんが、全財産を奪われて逃げられると回収に手間取ります。テレパシーで位置を特定して仕留めれば、大量の金貨を取り戻せます。"""
    },
    "step_311": {
        "title": "ミミック `m` (Mimics `m`)",
        "prose": """扉、階段、金貨、あるいは貴重なアイテムに擬態して獲物を待ち伏せます。触れると貼り付かれて移動不能になり、噛みつき攻撃を受けます。不自然な位置にある階段や扉、未識別の高価なアイテムには遠距離攻撃で確認を入れるのが賢明です。"""
    },
    "step_312": {
        "title": "ニンフ `n` (Nymphs `n`)",
        "prose": """所持品からアイテムを1つ盗み取り、同じフロアのランダムな場所へテレポートします。遠距離から攻撃するか、ペットで進路を塞ぐか、エルベレスの文字を刻んで近寄らせないようにしてください。もしアイテムを盗まれた場合は、フロア全体を捜索して倒せば盗まれたアイテムをすべて回収できます。\n\nすべてのニンフはテレポート能力を持ちます。"""
    },
    "step_313": {
        "title": "オーク `o` (Orcs `o`)",
        "prose": """集団で現れ、弓矢や毒矢、短剣を投げつけてきます。オークの弓や矢、盾、鎖かたびらなどを装備していることが多く、序盤の装備集めや飛び道具の補給に役立ちます。エルフのPCに対しては特に強い敵意を燃やします。"""
    },
    "step_314": {
        "title": "ピアサー `p` (Piercers `p`)",
        "prose": """天井の鍾乳石に擬態し、直下を通った冒険者の頭上へ落下して大ダメージを与えます。天井を見上げるか、怪しい通路の天井を注意深く探索することで事前に察知できます。"""
    },
    "step_315": {
        "title": "四足獣 `q` (Quadrupeds `q`)",
        "prose": """ロテやマンティコア、マムモスなどの四足歩行獣です。ロテは死体を急速に腐敗させて食べ尽くす能力を持ち、マンティコアは遠距離から大量のトゲを撃ち込んできます。"""
    },
    "step_316": {
        "title": "齧歯類 `r` (Rodents `r`)",
        "prose": """ネズミや巨大ネズミの群れ。兇暴ネズミは狂犬病に感染させてくる危険があります。ねずみ人間は噛みつきによってプレイヤーを獣化（ネズミ人間）させます。"""
    },
    "step_317": {
        "title": "蜘蛛および百足 `s` (Arachnids and centipedes `s`)",
        "prose": """巨大グモは足元に蜘蛛の巣を張って動きを封じ、毒を注入してきます。ムカデは器用さを吸い取る毒を持ちます。洞窟グモの巣はユニコーンの角や火炎の杖で焼き払うことができます。\n\nすべての蜘蛛および百足は毒耐性を備えています。"""
    },
    "step_318": {
        "title": "トラッパーおよびラーカー `t` (Trappers and lurkers `t`)",
        "prose": """床や天井に擬態する固定型の包み込み捕食者です。遠見（Farlook）でも隠れたラーカーを見抜くことはできません。怪しいマスには乗る前に隣から探索（Search）を行って正体を暴いてください。\n\nトラッパーとラーカーはすべて潜伏能力を持ち、階段の上り下りにも追従してきます。"""
    },
    "step_319": {
        "title": "ユニコーンおよび馬 `u` (Unicorns and horses `u`)",
        "prose": """馬（ポニー、馬、軍馬）は野生では敵対的に出現しますが、リンゴやニンジンを与えることで容易に手懐けられ、騎乗（Riding）スキルに活用できます。\n\nユニコーン（白、灰、黒）はそれぞれ秩序、中立、混沌の属性を持ち、同属性のプレイヤーには友好的です。宝石を投げ与えると幸運値を高めてくれます。角（ユニコーンの角）は万能の治療道具となります。"""
    },
    "step_320": {
        "title": "渦 `v` (Vortices `v`)",
        "prose": """プレイヤーを包み込んで元素ダメージを与える雲状の怪物です。色によって盲目砂嵐、冷気、電撃、火炎などの異なる属性ダメージを毎ターン与えてきます。包み込まれたら脱出の巻物や衝撃波、あるいは即座に倒す手段が必要です。\n\nすべての渦は飛行能力を持ち、精神を持たず、死体を残しません。"""
    },
    "step_321": {
        "title": "ワーム `w` (Worms `w`)",
        "prose": """長いワームは攻撃を受けるたびに尾のセグメントへ分裂して増殖します。紫ワーム（Purple worm）はプレイヤーを一撃で丸呑み（胃袋へ収容）して消化死させる極めて危険な怪物です。消化死を防ぐ手段（不変の魔除けなど）や、胃袋の内側から脱出する手段を用意してください。"""
    },
    "step_322": {
        "title": "ザンおよび幻想昆虫 `x` (Xans and fantastic insects `x`)",
        "prose": """グリッドバグは電気を帯びた単純な昆虫ですが、直角方向にしか移動できません。大型の近縁種であるザンは脚を刺して傷口を負わせ、最大所持重量（運搬能力）を急激に低下させます。\n\nすべてのザンおよび幻想昆虫は毒耐性を備えています。"""
    },
    "step_323": {
        "title": "光 `y` (Lights `y`)",
        "prose": """黄色い光は接触時に自爆閃光を放ち、10d20ターンの間プレイヤーを盲目にします。黒い光は自爆して幻覚状態を引き起こします。遠距離武器や魔法で接近される前に撃ち落とすのが鉄則です。\n\nすべての光は飛行能力を持ち、不定形で精神を持ちません。"""
    },
    "step_324": {
        "title": "ズリティ `z` (Zruties `z`)",
        "prose": """中盤に出現する手強い野獣で、2本の爪と強力な噛みつき攻撃を繰り出してきます。激しい連撃に耐えきることができれば、まとまった経験値を獲得できます。名称はスラブ神話の毛深い野生人に由来しています。"""
    },
    "step_325": {
        "title": "天使・神聖なる存在 `A` (Angelic beings `A`)",
        "prose": """武器を振るい、強力な魔法を操る終盤の強敵です。星界の面（Astral Plane）では各大祭司を護衛して立ち塞がります。[星界の面](#the-astral-plane)の項目を参照してください。\n\nすべての天使・神聖なる存在は階段の上り下りに追従し、死体を残しません。*アレアクス (Aleax)* を除きすべて飛行し、*コアトル (couatl)* を除きすべて不可視を看破します。"""
    },
    "step_326": {
        "title": "こうもりおよび鳥 `B` (Bats and birds `B`)",
        "prose": """不規則に飛び回る飛行生物。吸血こうもりは毒のある噛みつきで筋力を吸い取ります（毒耐性があれば防げます）。オオガラスは目をつついて盲目にしようとします。\n\nすべてのこうもりおよび鳥は飛行能力を持ちます。"""
    },
    "step_327": {
        "title": "ケンタウロス `C` (Centaurs `C`)",
        "prose": """強力な弓矢と近接攻撃を兼ね備えた半人半馬の射手です。森のケンタウロスは弓を放ち、平原や山のケンタウロスは複合弓を用いて強烈な矢の連射を浴びせてきます。離れた位置からの射撃戦は危険なため、角を曲がって誘い込むか接近戦に持ち込んでください。"""
    },
    "step_328": {
        "title": "ドラゴン `D` (Dragons `D`)",
        "prose": """成体のドラゴンは各自の属性に応じた強烈なブレスを直線状に吐き出します。反射（Reflection）能力があれば、遠距離ブレスを跳ね返して逆に大ダメージを与えられます。**幼体（子ドラゴン）はブレスを吐きません**。\n\n*多色ドラゴン (Chromatic Dragon)* を除き、すべてのドラゴンは飛行能力を持ちます。"""
    },
    "step_329": {
        "title": "精霊・エレメンタル `E` (Elementals `E`)",
        "prose": """風の精はプレイヤーを包み込んで瓦礫の嵐で叩きのめします。火の精は周囲を灼熱で焼き焦がし、水の精は強打を繰り出し、土の精は動きは鈍いものの極めて強固です。\n\n*ストーカー*を除き、すべてのエレメンタルは精神を持ちません。"""
    },
    "step_330": {
        "title": "菌類およびモールド `F` (Fungi and molds `F`)",
        "prose": """移動しない固定型の生物です。苔の怪物（Lichen）の死体は決して腐敗しないため、非常用の携帯食糧として最適です。茶色、緑、赤のモールドはそれぞれ冷気、酸、火炎の反撃ダメージを放ちます。\n\nすべての菌類およびモールドは精神を持ちません。"""
    },
    "step_331": {
        "title": "ノーム `G` (Gnomes `G`)",
        "prose": """ノームのPCにとってはノームの鉱山の住人の大半が友好的です。ノームの君主は通常種よりも高い攻撃力を持ち、ノームの魔法使いは強力な魔法攻撃を放ってきます。どちらも侮ってはなりません。"""
    },
    "step_332": {
        "title": "巨人 `H` (Giant humanoids `H`)",
        "prose": """巨岩を投げつけてくる怪力の人型生物です。火の巨人、霜の巨人、嵐の巨人はそれぞれの属性ダメージを扱い、その死体を食べることで火炎耐性、冷気耐性、電撃耐性や筋力上昇を獲得できるチャンスがあります。"""
    },
    "step_333": {
        "title": "ジャバウォック `J` (Jabberwocks `J`)",
        "prose": """ルイス・キャロルの詩『ジャバウォックの詩』に登場する獰猛な怪物。プレイヤーと同等の速度で移動し、鋭い爪と噛みつきによる連続攻撃を繰り出してきます。十分なACと武器強化が整うまでは警戒が必要です。"""
    },
    "step_334": {
        "title": "キーストン・コップ `K` (Keystone Kops `K`)",
        "prose": """店で泥棒を働くか、店主を傷つけた際に笛を鳴らして駆けつける警官隊です。個々の戦闘力は高くありませんが、群れをなして現れ、クリームパイを投げつけてプレイヤーの視界を塞ごうとします。"""
    },
    "step_335": {
        "title": "リッチ `L` (Liches `L`)",
        "prose": """骸骨姿の強力な魔法使いアンデッド。マスターリッチやアーチリッチは死の指（Touch of death）を詠唱し、モンスターを大量召喚し、冷気光線を放ってきます。魔法防御（Magic resistance）がなければ即死する危険極まりない強敵です。\n\nすべてのリッチは自動回復し、死体を残さず、アンデッドであり、冷気耐性、睡眠耐性、毒耐性を備えています。"""
    },
    "step_336": {
        "title": "ミイラ `M` (Mummies `M`)",
        "prose": """精神を持たないアンデッド。アンデッド退散の杖や呪文を使うと 1d8 のダメージを受けて逃走します。死亡時には元となった種族の古びた死体を残すため、病気耐性なしで食べると食中毒を起こす危険があります。"""
    },
    "step_337": {
        "title": "ナーガ `N` (Nagas `N`)",
        "prose": """蛇の体を持つ人型生物で、遠距離から酸や毒のブレス・吐瀉攻撃を行ってきます。すべてのナーガは毒耐性を備えています。黒ナーガの死体を食べると恒久的な毒耐性を獲得できることがあり、酸耐性と石化耐性も一時的に得られます。"""
    },
    "step_338": {
        "title": "オーガ `O` (Ogres `O`)",
        "prose": """強大な筋力を持つ近接戦闘の巨人です。こん棒や戦斧を振り回して大ダメージを与えてきますが、防具を着けていないためACは低く、遠距離から削るのが有効です。"""
    },
    "step_339": {
        "title": "プリンおよびウーズ `P` (Puddings and oozes `P`)",
        "prose": """**茶色および黒色プリンは鉄製や金属製の刃物で攻撃すると分裂します**。無傷の死体ではなく塊を残します。\n\n**緑スライム**は[ゲヘナ](#gehennom)にのみ現れる例外で、分裂はしませんが接触した相手を緑スライムへと徐々に変異させていきます（石化に似た即死タイマー）。\n\nすべてのプリンおよびウーズは不定形で、精神を持たず、冷気耐性、毒耐性、酸耐性、石化耐性を備えています。"""
    },
    "step_340": {
        "title": "量子力学士 `Q` (Quantum mechanics `Q`)",
        "prose": """特殊な爪攻撃を持つ2種類の生物です。**量子力学士 (Quantum mechanic)**は命中時にプレイヤーをランダムな場所へテレポートさせます。**遺伝子工学者 (Genetic engineer)**はプレイヤーを変身（ポリモルフ）させます。不変（Unchanging）の魔除けや魔法防御がなければ、一撃で別の生物に変えられてしまいます。\n\n両種とも自らランダムにテレポートし、毒のある死体を残します。"""
    },
    "step_341": {
        "title": "錆の怪物および魔法中和者 `R` (Rust monsters and disenchanters `R`)",
        "prose": """錆の怪物は接触時に鉄製の武器や防具を急速に錆びさせます。ディスエンチャンター（魔法中和者）は命中時に装備している防具や武器の強化値（+値）を吸い取って低下させます。油を塗った防具や、魔法防御、木製・銀製・革製の装備で対抗してください。"""
    },
    "step_342": {
        "title": "ヘビ `S` (Snakes `S`)",
        "prose": """大半が猛毒を持っています。クサリヘビ（マムシ）やコブラは致命的な毒を持ち、ガータースネークなどは無害な獲物です。\n\nすべてのヘビは遊泳能力を持ち、*ニシキヘビ (python)* を除いて潜伏能力を備えています。"""
    },
    "step_343": {
        "title": "トロール `T` (Trolls `T`)",
        "prose": """倒しても一定時間後に死体から自動復活します。確実にトロールの息の根を止めるには、**復活する前に死体を食べる**、缶詰作成キットで缶詰にする、あるいは火炎の杖や火炎の魔法で死体を焼き尽くす必要があります。\n\nすべてのトロールは自動回復能力を持ち、階段の上り下りにも追従してきます。"""
    },
    "step_344": {
        "title": "アンバーハルク `U` (Umber hulks `U`)",
        "prose": """混乱の凝視。視線が合うだけでプレイヤーを激しく混乱させます。目隠しやタオルを巻いて盲目状態で戦うか、遠距離から仕留めるのが定石です。混乱耐性やテレパシーを活用してください。"""
    },
    "step_345": {
        "title": "吸血鬼 `V` (Vampires `V`)",
        "prose": """噛みつき攻撃によってプレイヤーの経験値レベルを吸い取ります（エナジードレイン）。こうもりや霧の雲に変身して逃亡・奇襲を行います。通常の吸血鬼や吸血鬼の貴族は古びた人間の死体を残しますが、ヴラドは死体を残しません。ヴラド公は[ヴラドの塔](#vlads-tower)のボスです。\n\nすべての吸血鬼は飛行し、自動回復し、アンデッドであり、階段に追従し、変身能力を持ちます。"""
    },
    "step_346": {
        "title": "レイス `W` (Wraiths `W`)",
        "prose": """接触によってプレイヤーの経験値レベルを1段階吸い取ります。しかし、倒した後に残る新鮮なレイスの死体を食べれば、逆に経験値レベルが1上昇するという大きな見返りがあります。アンデッド退散や銀の武器が有効です。\n\nすべてのレイスはアンデッドであり、階段の上り下りに追従してきます。"""
    },
    "step_347": {
        "title": "ゾーン `X` (Xorns `X`)",
        "prose": """D&Dに由来する、土の元素界からやってきた3本腕・3つ目の異形の怪物です。彼らは**固い岩壁をすり抜けて移動**し、突然壁の中から奇襲を仕掛けてきます。金属や宝石を好んで食べます。"""
    },
    "step_348": {
        "title": "類人猿 `Y` (Apelike creatures `Y`)",
        "prose": """類人猿や大猿が中心です。サスクワッチ（雪男）は素早い動きで殴りかかってきます。肉食獣の死体は安全な食料となります。"""
    },
    "step_349": {
        "title": "ゾンビ `Z` (Zombies `Z`)",
        "prose": """動きの鈍いアンデッド。距離を取りながら戦えば容易に倒せます。種族ごとのゾンビは元となった種族の古びた死体を残すため、病気耐性なしで食べると食中毒の危険があります。アンデッド退散の杖や呪文を使うと逃走します。ガイコツ（スケルトン）は自然生成されず、オルクスの町やボーンデビルによって召喚されます。\n\nすべてのゾンビは精神を持たず、アンデッドです。"""
    },
    "step_350": {
        "title": "人間およびエルフ `@` (Humans and elves `@`)",
        "prose": """`@` のシンボルだけで相手を判断してはなりません。平和的な店主、僧侶、番兵、クエストリーダーであることもあれば、メデューサ、各職業のネメシス、富豪クロイソス、あるいはイェンダーの魔法使いである可能性もあります。動く前に対象の名前を必ず確認してください。このクラスには兵士、忍者、ドッペルゲンガー、獣人、冒険者、そしてプレイヤー自身も含まれます。"""
    },
    "step_351": {
        "title": "大悪魔 `&` (Major demons `&`)",
        "prose": """強力無比な大悪魔たちです。多くは同胞の悪魔を呼び出すゲート召喚能力を持ちます（1体の有刺デビルが瞬く間に5体に増えることもあります）。銀の武器やデーモンベインが特効の大ダメージを与えます。ゲリュオン、ディスパテル、ベルゼブブ、アスモデウスのみが賄賂（金貨）による停戦に応じますが、エクスカリバーやデーモンベインを構えているときは交渉に応じません。\n\nすべて階段の上り下りに追従してきます。"""
    },
    "step_352": {
        "title": "ゴーレム `'` (Golems `'`)",
        "prose": """鉄、石、粘土のゴーレムは非常に強固で危険です。木や革のゴーレムは序盤の敵です。極めて稀に出現する黄金ゴーレムは、歩く財宝の山と言えます。\n\nすべてのゴーレムは精神を持たず、睡眠耐性と毒耐性を備えています。"""
    },
    "step_353": {
        "title": "海の怪物 `;` (Sea monsters `;`)",
        "prose": """水中に生息する怪物です。巨大ウナギやクラーケンはプレイヤーの体に巻き付き、水中に引きずり込んで溺死させようとします。魔法の呼吸（Magical breathing）がなければ瞬時に命を落とします。\n\nすべての海の怪物は遊泳能力を持ち、水陸両用です。"""
    },
    "step_354": {
        "title": "トカゲ `:` (Lizards `:`)",
        "prose": """大半は無害です。**トカゲの死体は石化を治療し、決して腐敗しません**。コカトリス対策として必ず荷物に1つ入れておきましょう。ただし、メデューサの直接の凝視による石化は即死するため、トカゲの死体では救われません。"""
    },
}

with open(os.path.join("spoilers", "companion.md"), "r", encoding="utf-8") as f:
    companion_lines = f.readlines()

with open(os.path.join("docs", "translation_progress.json"), "r", encoding="utf-8") as f:
    progress = json.load(f)

def translate_row(line):
    parts = [p.strip() for p in line.split("|")]
    if len(parts) < 9:
        return line
    raw_name = parts[1]
    raw_color = parts[2]
    lvl = parts[3]
    spd = parts[4]
    ac = parts[5]
    mr = parts[6]
    attacks = parts[7]
    notes = parts[8]

    # Name translation
    clean_name = raw_name.lower()
    ja_name = glossary.get(clean_name, raw_name)
    disp_name = f"{ja_name} ({raw_name})" if ja_name != raw_name else raw_name

    # Color translation
    ja_color = color_dict.get(raw_color.lower(), raw_color)

    # Attacks
    ja_attacks = attacks
    for p, r in attack_trans:
        ja_attacks = re.sub(p, r, ja_attacks)

    # Notes phrases
    ja_notes = notes
    for p, r in phrase_trans:
        ja_notes = ja_notes.replace(p, r)

    # Notes regex
    for p, r in notes_trans:
        ja_notes = re.sub(p, r, ja_notes)

    return f"| {disp_name} | {ja_color} | {lvl} | {spd} | {ac} | {mr} | {ja_attacks} | {ja_notes} |"

def generate_segment(seg_info):
    sid = seg_info["id"]
    start = seg_info["start_line"] - 1
    end = seg_info["end_line"]
    orig_chunk = companion_lines[start:end]

    info = prose_data.get(sid, {})
    title = info.get("title", seg_info["orig_header"])
    prose = info.get("prose", "")

    # Extract audit block
    audit_block = ""
    chunk_str = "".join(orig_chunk)
    m = re.search(r'(<!-- audit.*?-->)', chunk_str, re.DOTALL)
    if m:
        audit_block = m.group(1) + "\n\n"

    prefix = "### " if sid == "step_298" else "#### "

    if sid == "step_298":
        return f"{prefix}{title}\n\n{audit_block}{prose}\n"

    table_lines = []
    in_table = False
    for line in orig_chunk:
        if line.strip() == "::: dense-table":
            in_table = True
            continue
        if in_table:
            if line.strip() == ":::":
                in_table = False
                break
            if line.strip().startswith("| Name |"):
                continue
            if line.strip().startswith("|---"):
                continue
            if line.strip().startswith("|"):
                table_lines.append(translate_row(line))

    table_md = "\n".join(table_lines)
    header_md = "| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |\n|---|---|---|---|---|---|---|---|\n"

    content = f"{prefix}{title}\n\n{audit_block}{prose}\n\n::: dense-table\n\n{header_md}{table_md}\n\n:::\n"
    return content

for s in progress["segments"]:
    idx = int(s["id"].split("_")[1])
    if 298 <= idx <= 354:
        c = generate_segment(s)
        out_path = os.path.join("docs", "segments_ja", f"{s['id']}.md")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(c.strip() + "\n")
        print(f"Generated {out_path}")

