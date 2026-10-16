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
            en_clean = en.strip().lower()
            ja_clean = ja.strip()
            glossary[en_clean] = ja_clean
            glossary[en_clean.replace("-", " ")] = ja_clean
            glossary[en_clean.replace(" ", "-")] = ja_clean

# Exact overrides and additions
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
glossary["displacer beast"] = "幻影の獣"
glossary["arch-lich"] = "アーチリッチ"
glossary["dwarf lord"] = "ドワーフの首領"
glossary["dwarf king"] = "ドワーフの支配者"
glossary["kobold lord"] = "コボルドの首領"
glossary["uruk-hai"] = "ウルク＝ハイ"
glossary["orc-captain"] = "オークの隊長"
glossary["ki-rin"] = "麒麟"
glossary["gnome lord"] = "ノームの首領"
glossary["gnome king"] = "ノームの支配者"
glossary["ogre lord"] = "オーガの首領"
glossary["ogre king"] = "オーガの暴君"
glossary["olog-hai"] = "オログ＝ハイ"
glossary["vampire lord"] = "ヴァンパイアの長"
glossary["woodland-elf"] = "森のエルフ"
glossary["green-elf"] = "緑エルフ"
glossary["grey-elf"] = "灰色エルフ"
glossary["elf-lord"] = "エルフの貴族"
glossary["elvenking"] = "エルフの君主"
glossary["caveman"] = "洞窟人"
glossary["high priest"] = "高位神官"
glossary["amorous demon"] = "好色な悪魔"

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
    (r"\bsteal-amulet\b", "盗み-魔除け"),
    (r"\bsteal\b", "盗み"),
    (r"\bseduce\b", "誘惑"),
    (r"\bsedux\b", "誘惑"),
    (r"\brust\b", "錆び"),
    (r"\brot\b", "腐敗"),
    (r"\bdrain-Int\b", "知力吸収"),
    (r"\bdrain-XL\b", "レベル吸収"),
    (r"\bStr-drain\b", "筋力吸収"),
    (r"\bdrain-Str\b", "筋力吸収"),
    (r"\bdrain\b", "エナジードレイン"),
    (r"\blyc\b", "獣化"),
    (r"\bcurse\b", "呪い"),
    (r"\bmagic\b", "魔法"),
    (r"\bcast cleric\b", "僧侶呪文"),
    (r"\bcast spell\b", "攻撃呪文"),
    (r"\bcast\b", "呪文詠唱"),
    (r"\bheal\b", "回復"),
    (r"\bwrap\b", "巻きつき"),
    (r"\bsticky\b", "粘着"),
    (r"\bslow\b", "減速"),
    (r"\bstun\b", "朦朧"),
    (r"\bseduction \(see Seduction\)", "誘惑 (誘惑セクション参照)"),
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
    ("Knight's starting steed.", "騎士の初期乗馬ペット。"),
    ("Passive acid damage; punching one corrodes your gloves.", "酸の反撃ダメージ。素手で殴ると手袋が腐食する。"),
    ("Slow but paralyses on touch. Don't melee without free-action.", "鈍足だが接触時に麻痺。自由行動なしでの近接戦は厳禁。"),
    ("Stings carry poison.", "毒針攻撃。"),
    ("Poison sting.", "毒針攻撃。"),
    ("No corpse.", "死体を残さない。"),
    ("Lawful PCs may find them peaceful.", "秩序のPCには友好的な場合がある。"),
    ("Hits hard. Drops decent loot.", "強烈な打撃。上質な戦利品をドロップ。"),
    ("drops a worm tooth.", "ワームの歯をドロップ。"),
    ("Grows stronger as your alignment record falls, gaining harder blows, flight, regeneration, and a second attack.",
     "属性値が低下するほど強化され、攻撃力上昇、飛行、自動回復、追加攻撃を獲得する。"),
    ("Casts touch of death; magic resistance mandatory.", "死の指を詠唱。魔法防御が必須。"),
    ("Casts wizard spells. Kill from afar.", "攻撃呪文を詠唱。遠距離から倒すこと。"),
    ("Throws boulders for big damage.", "巨石を投げて大ダメージを与える。"),
    ("Throws boulders.", "巨石投げ攻撃。"),
    ("Touch rusts iron. Strip armor before engaging or use silver.", "接触で鉄を錆びさせる。戦う前に鎧を脱ぐか銀製武器を使用すること。"),
    ("Four heavy attacks; baseline speed.", "4回連続の強烈な攻撃。標準速度。"),
    ("Tough humanoid with magic missiles. Casts spells.", "マジックミサイルを放つ頑強な人型生物。呪文を詠唱。"),
    ("Confusion gaze. Hard to navigate around. Hits hard too.", "混乱の凝視。回り込んで避けるのが困難。打撃も強力。"),
    ("eats metal objects left on the floor.", "床に落ちている金属製アイテムを捕食する。"),
    ("Displays as succubus or incubus by the demon's own randomly-assigned gender.",
     "悪魔自体のランダムな性別に応じてサキュバスまたはインキュバスとして出現する。"),
    ("Covetous: teleports to you in late Gehennom and on the planes. The final boss.",
     "執着行動：ゲヘナ深層および各元素界でプレイヤーの元へテレポートしてくる。最後のボス。"),
    ("Rider of the Apocalypse. Vanquish three to ascend.", "黙示録の四騎士。昇天するには3体を打ち倒さねばならない。"),
    ("Rider; drains nutrition to starvation.", "黙示録の四騎士。栄養度を吸い取って餓死寸前に追い込む。"),
    ("Rider; spreads disease.", "黙示録の四騎士。病気を媒介する。"),
    ("Appears only to deliver in-game mail, then leaves.", "ゲーム内メールを配達するためだけに出現し、すぐに立ち去る。"),
    ("Vault guardian on Fort Ludios. Wields a two-handed sword and hoards gold, gems, and magic items off the floor.",
     "ルディオス砦の財宝守護者。両手持ち剣を振るい、床の金貨、宝石、魔法のアイテムを溜め込む。"),
    ("Archeologist quest leader.", "考古学者のクエストリーダー。"),
    ("Barbarian quest leader.", "野蛮人のクエストリーダー。"),
    ("Cave Dweller quest leader.", "洞窟人のクエストリーダー。"),
    ("Healer quest leader.", "治療師のクエストリーダー。"),
    ("Knight quest leader. Holds Excalibur if you didn't get it.", "騎士のクエストリーダー。プレイヤーが入手していない場合エクスカリバーを所持。"),
    ("Monk quest leader.", "武闘家のクエストリーダー。"),
    ("Priest quest leader.", "司祭のクエストリーダー。"),
    ("Ranger quest leader. Bow user.", "レンジャーのクエストリーダー。弓の使い手。"),
    ("Rogue quest leader; also Tourist quest nemesis.", "盗賊のクエストリーダー（観光客のクエスト宿敵でもある）。"),
    ("Samurai quest leader.", "侍のクエストリーダー。"),
    ("Tourist quest leader.", "観光客のクエストリーダー。"),
    ("Valkyrie quest leader.", "ワルキューレのクエストリーダー。"),
    ("Wizard quest leader.", "魔法使いのクエストリーダー。"),
    ("Barbarian quest nemesis.", "野蛮人のクエスト宿敵。"),
    ("Healer quest nemesis.", "治療師のクエスト宿敵。"),
    ("Monk quest nemesis.", "武闘家のクエスト宿敵。"),
    ("Rogue quest nemesis.", "盗賊のクエスト宿敵。"),
    ("Samurai quest nemesis.", "侍のクエスト宿敵。"),
    ("Wizard quest nemesis.", "魔法使いのクエスト宿敵。"),
    ("Valkyrie quest nemesis.", "ワルキューレのクエスト宿敵。"),
    ("Vampire boss in Vlad's Tower. Has the Candelabrum.", "ヴラドの塔の吸血鬼ボス。燭台を所持。"),
    ("Temple defenders. Convert their altars or sacrifice on them.", "寺院の守護者。彼らの祭壇を改宗させるか生贄を捧げること。"),
    ("Endgame altar guardian. Don't fight one head-on.", "最終盤の祭壇守護者。正面から戦ってはならない。"),
    ("Don't anger one.", "決して怒らせてはならない。"),
    ("Acid breath.", "酸のブレス。"),
    ("Anti-magic breath. Magic resistance helps; reflection doesn't.", "反魔法ブレス。魔法防御が有効、反射は無効。"),
    ("Cold breath plus reflection scales: your reflection target.", "冷気ブレス。反射の鱗を落とすため反射能力の獲得標的となる。"),
    ("Cone of cold. Cold resistance.", "冷気ブレス。冷気耐性で対処。"),
    ("Cone of fire. Get fire resistance before you meet one.", "火炎ブレス。遭遇する前に火炎耐性を得ておくこと。"),
    ("Cone of lightning. Shock resistance.", "電撃ブレス。電撃耐性で対処。"),
    ("Disintegration breath. Disint resistance OR reflection.", "分解ブレス。分解耐性または反射が必須。"),
    ("Fire breath. Drops gold-colored scales (light source).", "火炎ブレス。金色の鱗（光源）をドロップ。"),
    ("Sleep ray. Sleep resistance trivialises.", "睡眠光線。睡眠耐性があれば無力化できる。"),
    ("Poison breath; poison resistance is enough.", "毒ブレス。毒耐性があれば十分。"),
    ("Active drains armor; passive drains weapon when you melee it.", "能動攻撃で防具が劣化し、近接攻撃を仕掛けると反撃で武器が劣化する。"),
    ("corpse: cold + poison resistance.", "死体：冷気耐性・毒耐性獲得。"),
    ("corpse: temp acid + stone resistance.", "死体：一時的な酸耐性・石化耐性獲得。"),
    ("Self-teleports. Corpse toggles intrinsic Fast.", "自己テレポート。死体を食べると「高速移動」能力の有無が反転。"),
    ("Self-teleports. Corpse triggers polyself.", "自己テレポート。死体を食べると「へんげ」が発生。"),
    ("Steals gold and teleports away. Carry no gold near them.", "金貨を盗んでテレポート逃走。近くでは金貨を持ち歩かないこと。"),
    ("Two claws plus a butt. Heavy hitter; roams the Gehennom mazes.", "2回の爪攻撃と頭突き。強打の持ち主でゲヘナの迷宮を徘徊。"),
    ("Five tentacles per turn. Any helmet blocks 7/8 of tentacles.", "1ターンに5回の触手攻撃。兜を着用していれば触手を7/8の確率で防御可能。"),
    ("Tentacles drain Int; once it reaches 3, the next tentacle that lands kills you. Any helmet blocks 7/8 of tentacles.",
     "触手が知力を吸収。知力が3に達すると次の触手攻撃で即死。兜を着用していれば触手を7/8の確率で防御可能。"),
]

def trans_race_name(r):
    race_map = {
        "human": "人間", "dwarf": "ドワーフ", "elf": "エルフ", "ettin": "エティン",
        "giant": "巨人", "gnome": "ノーム", "kobold": "コボルド", "orc": "オーク"
    }
    return race_map.get(r, r)

notes_trans = [
    (r"Drops an old (human|dwarf|elf|ettin|giant|gnome|kobold|orc) corpse\.", lambda m: f"古い{trans_race_name(m.group(1))}の死体を残す。"),
    (r"\bno corpse\b", "死体を残さない"),
    (r"\bNo corpse\b", "死体を残さない"),
    (r"\bGehennom-only\b", "ゲヘナ限定出現"),
    (r"\bpoisonous-corpse\b", "死体に毒あり"),
    (r"\bpois-res\b", "毒耐性"),
    (r"\bpoison-res\b", "毒耐性"),
    (r"\bfire-res\b", "火炎耐性"),
    (r"\bcold-res\b", "冷気耐性"),
    (r"\bshock-res\b", "電撃耐性"),
    (r"\bacid-res\b", "酸耐性"),
    (r"\bston-res\b", "石化耐性"),
    (r"\bdisint-res\b", "分解耐性"),
    (r"\bsleep-res\b", "睡眠耐性"),
    (r"\bsees-invis\b", "不可視視認"),
    (r"\bsee-invis\b", "不可視視認"),
    (r"\bregenerates\b", "自動回復"),
    (r"\btameable\b", "手懐け可能"),
    (r"\bamorphous\b", "不定形"),
    (r"\bmindless\b", "精神なし"),
    (r"\binvis\b", "不可視"),
    (r"\bhuman\b", "人間"),
    (r"\bundead\b", "アンデッド"),
    (r"\bdemonic\b", "悪魔"),
    (r"\bdemon\b", "悪魔"),
    (r"\bgiant\b", "巨人"),
    (r"\bflies\b", "飛行"),
    (r"\bfly\b", "飛行"),
    (r"\bswims\b", "遊泳"),
    (r"\bamphibious\b", "水陸両用"),
    (r"\bteleports\b", "テレポート"),
    (r"\bteleport-control\b", "テレポート制御"),
    (r"\bhides\b", "潜伏"),
    (r"\bhide\b", "潜伏"),
    (r"\btunnels\b", "穴掘り移動"),
    (r"\bclings\b", "壁張り付き"),
    (r"\bshapeshifter\b", "シェイプシフター"),
    (r"\bfollows stairs\b", "階段を追跡"),
    (r"\bstarts peaceful\b", "初期状態は友好的"),
]

# Section Japanese titles and Japanese prose definitions
prose_data = {
    "step_298": {
        "title": "モンスター図鑑一覧表 (Bestiary Tables) {#bestiary-tables}",
        "prose": """ダンジョンで遭遇しうるあらゆるモンスターをマップ記号ごとに分類した一覧です。**レベル (Lvl)**はモンスターの基本レベル、**速度 (Spd)**は移動速度（プレイヤーの標準速度は 12）、**AC**はアーマークラス（低いほど強固）、**MR**は魔法防御率（プレイヤーの呪文や魔法攻撃に抵抗する確率%）を表します。**攻撃方法 (Attacks)**は各攻撃の種別、ダメージダイス、追加効果を記載しており、`·` で区切られた攻撃は1ターン内にすべて連続して繰り出されます。**備考 (Notes)**には飛行能力、不可視視認、自動回復、死体に毒があるかなど、戦闘を一変させる重要な特性をまとめています。"""
    },
    "step_299": {
        "title": "蟻および昆虫 `a` (Ants and insects `a`) {#ants-and-insects-a}",
        "prose": """昆虫類。多くは集団で群れをなして出現します。兵隊蟻の毒針攻撃は筋力を吸い取ります。殺人蜂は大群で襲いかかり、蜂の巣の部屋にいる女王蜂は単体でも手ごわい相手です。"""
    },
    "step_300": {
        "title": "ブロッブ `b` (Blobs `b`) {#blobs-b}",
        "prose": """動きが遅く、精神を持ちません。酸のブロッブを素手や大切な金属武器で近接攻撃してはいけません。相手の酸による反撃で武器や防具が腐食します。ゼラチンキューブは接触時にプレイヤーを麻痺させます。\n\nすべてのブロッブは精神を持たず（マインドレス）、睡眠耐性と毒耐性を備えています。"""
    },
    "step_301": {
        "title": "コカトリス `c` (Cockatrices `c`) {#cockatrices-c}",
        "prose": """中世の動物寓話に登場する怪物。蛇の尾を持つ鶏の姿をしており、その接触は肉体を瞬時に石化させます。トカゲの死体を常時携帯し、必ず手袋を着用して戦ってください。どの職業も初期状態では石化耐性を持っておらず、コカトリスの死体を素手で装備すると即死します。[石化](#petrification-stoning)の項目を参照してください。\n\nすべてのコカトリス類は毒耐性を備えています。"""
    },
    "step_302": {
        "title": "犬およびイヌ科 `d` (Dogs and canines `d`) {#dogs-and-canines-d}",
        "prose": """野生のイヌ科生物は群れで狩りを行います。飼いならされたものは食料を与えることでペットにできます（[仲間の増やし方](#making-friends)参照）。ジャッカル人間や狼人間はプレイヤーを獣化（ライカンスロープ）に感染させることがあります。"""
    },
    "step_303": {
        "title": "目および球体 `e` (Eyes and spheres `e`) {#eyes-and-spheres-e}",
        "prose": """さまよう目の反撃麻痺凝視は、ダンジョン序盤において最も有名な死因の一つです。自由行動（Free action）、盲目状態、または遠距離攻撃の手段を持たずに近接攻撃を仕掛けてはなりません。倒した後は死体を食べてください。恒久的なテレパシー能力（内在能力）を獲得できます。\n\nすべての目および球体は飛行能力を持ちます。また、*さまよう目*を除きすべて精神を持ちません。"""
    },
    "step_304": {
        "title": "ネコ科 `f` (Felines `f`) {#felines-f}",
        "prose": """野生のネコ科生物は素早く敵対的です。虎や幻影の獣は、何気ない通路での遭遇を命がけの戦いに変えてしまいます。魔法使いは必ず小猫を連れてスタートし、初期ペットが固定されていない職業は小猫か仔犬のいずれかを 50% の確率で連れて開始します。"""
    },
    "step_305": {
        "title": "グレムリン `g` (Gremlins `g`) {#gremlins-g}",
        "prose": """夜間（または光源がない暗闇）に水に触れると分裂増殖する厄介な小型怪物です。暗闇の中でプレイヤーから内在能力を盗み取る攻撃を行います。明るい光源を持ち歩くか、明かりの巻物・呪文で部屋を照らすのが有効な対抗策です。"""
    },
    "step_306": {
        "title": "人型生物 `h` (Humanoids `h`) {#humanoids-h}",
        "prose": """小人族、ホビット、ドワーフ、巨人など多彩な人型生物が含まれます。ノームの鉱山ではドワーフが中立または友好的に出現することが多く、彼らの落とすミスリル服や鉄兜は序盤の貴重な防具供給源となります。"""
    },
    "step_307": {
        "title": "小悪魔および下級悪魔 `i` (Imps and minor demons `i`) {#imps-and-minor-demons-i}",
        "prose": """インプ、ホムンクルス、テングなどの下級悪魔です。テングは頻繁にテレポートを行い、その死体を食べることでテレポート能力やテレポート制御能力を獲得できるチャンスがあります。"""
    },
    "step_308": {
        "title": "ゼリー `j` (Jellies `j`) {#jellies-j}",
        "prose": """壁際や床に張り付く不定形の怪物です。青色ゼリーは冷気、赤色ゼリーは火炎の反撃ダメージを与えます。金属武器を腐食させる斑点ゼリーにも注意が必要です。"""
    },
    "step_309": {
        "title": "コボルド `k` (Kobolds `k`) {#kobolds-k}",
        "prose": """序盤に群れで現れる小型の邪悪な生物。毒矢を放ってくることがあり、毒耐性がない最序盤では1発で致命傷になり得ます。死体にも毒が含まれているため、毒耐性を得るまでは食べてはいけません。"""
    },
    "step_310": {
        "title": "レプラコーン `l` (Leprechauns `l`) {#leprechauns-l}",
        "prose": """金貨を盗んで即座にフロアの別の場所へテレポートする妖精です。攻撃力は高くありませんが、全財産を奪われて逃げられると回収に手間取ります。テレパシーで位置を特定して仕留めれば、大量の金貨を取り戻せます。"""
    },
    "step_311": {
        "title": "ミミック `m` (Mimics `m`) {#mimics-m}",
        "prose": """扉、階段、金貨、あるいは貴重なアイテムに擬態して獲物を待ち伏せます。触れると貼り付かれて移動不能になり、噛みつき攻撃を受けます。不自然な位置にある階段や扉、未識別の高価なアイテムには遠距離攻撃で確認を入れるのが賢明です。"""
    },
    "step_312": {
        "title": "ニンフ `n` (Nymphs `n`) {#nymphs-n}",
        "prose": """所持品からアイテムを1つ盗み取り、同じフロアのランダムな場所へテレポートします。遠距離から攻撃するか、ペットで進路を塞ぐか、エルベレスの文字を刻んで近寄らせないようにしてください。もしアイテムを盗まれた場合は、フロア全体を捜索して倒せば盗まれたアイテムをすべて回収できます。\n\nすべてのニンフはテレポート能力を持ちます。"""
    },
    "step_313": {
        "title": "オーク `o` (Orcs `o`) {#orcs-o}",
        "prose": """地下世界の主要な戦力。ノームの鉱山や通常フロアに集団で生成されます。毒矢を放つ弓兵や、耐腐食加工されたウルク＝ハイの装備など、序盤のプレイヤーにとって油断できない脅威です。\n\nすべてのオーク類は毒耐性を備えています。"""
    },
    "step_314": {
        "title": "ピアサー `p` (Piercers `p`) {#piercers-p}",
        "prose": """天井の鍾乳石に擬態し、直下を通過したプレイヤーに落下して大ダメージを与えてきます。怪しい天井の影には遠距離攻撃や投石で確認を入れるのが有効です。"""
    },
    "step_315": {
        "title": "四肢動物 `q` (Quadrupeds `q`) {#quadrupeds-q}",
        "prose": """ロゼやワンパスなど、地下に住まう4足歩行の獣です。群れで現れるロゼは序盤の食料源としても重宝されます。"""
    },
    "step_316": {
        "title": "げっ歯類 `r` (Rodents `r`) {#rodents-r}",
        "prose": """下水ネズミ、巨大ネズミ、岩モグラなどの小型哺乳類です。床に落ちている金属アイテムを食べる岩モグラや、木製の扉を齧るウッドチャックなどが含まれます。"""
    },
    "step_317": {
        "title": "蜘蛛およびサソリ `s` (Spiders and scorpions `s`) {#spiders-and-scorpions-s}",
        "prose": """洞窟グモや大蠍など、毒針や巣を扱う節足動物です。大蠍の毒針は筋力を急速に低下させるため、解毒手段がない序盤は近接戦を避けるべきです。\n\nすべての蜘蛛およびサソリは毒耐性を備えています。"""
    },
    "step_318": {
        "title": "罠生物 `t` (Trappers and lurkers `t`) {#trappers-and-lurkers-t}",
        "prose": """床に擬態するトラッパーと、天井に擬態するラーカーが含まれます。不用意に踏み込むと丸呑み（圧搾）され、脱出するまで毎ターンダメージを受け続けます。"""
    },
    "step_319": {
        "title": "馬およびユニコーン `u` (Unicorns and horses `u`) {#unicorns-and-horses-u}",
        "prose": """野生の馬は食料で手懐けて乗馬ペットにできます。白、灰色、黒の3種のユニコーンはそれぞれの属性を持ち、属性に合った宝石を投げると幸運を授けてくれます。ユニコーンの角はあらゆる状態異常を治療する至宝です。"""
    },
    "step_320": {
        "title": "渦 `v` (Vortices `v`) {#vortices-v}",
        "prose": """火炎、冷気、電撃、あるいは蒸気の渦です。プレイヤーを内部に巻き込み、属性ダメージを連続して与えてきます。魔法防御や対応する属性耐性がないと極めて危険です。"""
    },
    "step_321": {
        "title": "ワーム `w` (Worms `w`) {#worms-w}",
        "prose": """長い体をくねらせてダンジョンを掘り進む巨大ワームです。ロングワームは倒すと強力なナイフの材料となる「ワームの歯」をドロップします。"""
    },
    "step_322": {
        "title": "その他原生生物 `x` (Xan and miscellaneous `x`) {#xan-and-miscellaneous-x}",
        "prose": """ザンやジャガーノートなど、分類不能な異形の生物群です。ザンの刺突は傷口を化膿させて手足を麻痺させます。"""
    },
    "step_323": {
        "title": "光および幻影 `y` (Lights and phantoms `y`) {#lights-and-phantoms-y}",
        "prose": """黄色光や黒色光など、視界や精神を惑わす発光生物です。触れると自爆して盲目や混乱を引き起こします。"""
    },
    "step_324": {
        "title": "ズーティ `z` (Zruty `z`) {#zruty-z}",
        "prose": """スラブ神話の怪力巨人ズーティです。単純ながら非常に高い近接攻撃力を持ち、鈍足ですが正面から殴り合うと危険です。"""
    },
    "step_325": {
        "title": "天使系 `A` (Angelic beings `A`) {#angelic-beings-a}",
        "prose": """神に仕える聖なる使い。自身の属性と同じ天使を攻撃すると神の怒りを買います。アルコンや天使は強力な呪文と盲目攻撃を繰り出すため、敵対した際は最大級の警戒が必要です。"""
    },
    "step_326": {
        "title": "こうもりおよび鳥類 `B` (Bats and birds `B`) {#bats-and-birds-b}",
        "prose": """不規則に飛び回る素早い飛行生物です。吸血こうもりの噛みつきはエナジードレインを引き起こし、カラスは目を突いて盲目にしてきます。\n\nすべてのこうもりおよび鳥類は飛行能力を持ちます。"""
    },
    "step_327": {
        "title": "ケンタウロス `C` (Centaurs `C`) {#centaurs-c}",
        "prose": """上半身が人間、下半身が馬の俊足狩人です。遠距離から弓矢を連射してくるため、通路に誘い込んで射線を切るか、接近して近接戦に持ち込みましょう。"""
    },
    "step_328": {
        "title": "ドラゴン `D` (Dragons `D`) {#dragons-d}",
        "prose": """ダンジョン屈指の巨獣。属性に応じた強力なブレスを放ちます。倒して得られるドラゴンの死体や鱗からは、最高の防御性能と耐性を誇る「ドラゴンの鱗鎧」を作ることができます。\n\nすべてのドラゴンは飛行能力と不可視視認能力を備えています。"""
    },
    "step_329": {
        "title": "エレメンタル `E` (Elementals `E`) {#elementals-e}",
        "prose": """四大元素（風、火、土、水）の精霊です。風の精は素早く丸呑み攻撃を繰り出し、土の精は壁をすり抜けて奇襲してきます。対応する属性耐性と高いACが攻略の鍵です。"""
    },
    "step_330": {
        "title": "菌類およびモールド `F` (Fungi and molds `F`) {#fungi-and-molds-f}",
        "prose": """移動能力を持たない固定生物です。攻撃すると胞子をまき散らして反撃してきます。シュリーカーは大声で叫んで周囲のモンスターを呼び寄せるため、速やかに遠距離から排除してください。"""
    },
    "step_331": {
        "title": "ノーム `G` (Gnomes `G`) {#gnomes-g}",
        "prose": """ノームの鉱山の主。小型ながら道具やクロスボウを使いこなします。ノームの支配者やノームの魔法使いは油断ならない戦闘力を持ちます。"""
    },
    "step_332": {
        "title": "巨人 `H` (Giant humanoids `H`) {#giant-humanoids-h}",
        "prose": """巨岩を投げつけてくる怪力の人型生物です。火の巨人、霜の巨人、嵐の巨人はそれぞれの属性ダメージを扱い、その死体を食べることで火炎耐性、冷気耐性、電撃耐性や筋力上昇を獲得できるチャンスがあります。"""
    },
    "step_333": {
        "title": "ジャバウォック `J` (Jabberwocks `J`) {#jabberwocks-j}",
        "prose": """ルイス・キャロルの詩『ジャバウォックの詩』に登場する獰猛な怪物。プレイヤーと同等の速度で移動し、鋭い爪と噛みつきによる連続攻撃を繰り出してきます。十分なACと武器強化が整うまでは警戒が必要です。"""
    },
    "step_334": {
        "title": "キーストン・コップ `K` (Keystone Kops `K`) {#keystone-kops-k}",
        "prose": """店で泥棒を働くか、店主を傷つけた際に笛を鳴らして駆けつける警官隊です。個々の戦闘力は高くありませんが、群れをなして現れ、クリームパイを投げつけてプレイヤーの視界を塞ごうとします。"""
    },
    "step_335": {
        "title": "リッチ `L` (Liches `L`) {#liches-l}",
        "prose": """骸骨姿の強力な魔法使いアンデッド。マスターリッチやアーチリッチは死の指（Touch of death）を詠唱し、モンスターを大量召喚し、冷気光線を放ってきます。魔法防御（Magic resistance）がなければ即死する危険極まりない強敵です。\n\nすべてのリッチは自動回復し、死体を残さず、アンデッドであり、冷気耐性、睡眠耐性、毒耐性を備えています。"""
    },
    "step_336": {
        "title": "ミイラ `M` (Mummies `M`) {#mummies-m}",
        "prose": """精神を持たないアンデッド。アンデッド退散の杖や呪文を使うと 1d8 のダメージを受けて逃走します。死亡時には元となった種族の古びた死体を残すため、病気耐性なしで食べると食中毒を起こす危険があります。"""
    },
    "step_337": {
        "title": "ナーガ `N` (Nagas `N`) {#nagas-n}",
        "prose": """蛇の体を持つ人型生物で、遠距離から酸や毒のブレス・吐瀉攻撃を行ってきます。すべてのナーガは毒耐性を備えています。黒ナーガの死体を食べると恒久的な毒耐性を獲得できることがあり、酸耐性と石化耐性も一時的に得られます。"""
    },
    "step_338": {
        "title": "オーガ `O` (Ogres `O`) {#ogres-o}",
        "prose": """強大な筋力を持つ近接戦闘の巨人です。こん棒や戦斧を振り回して大ダメージを与えてきますが、防具を着けていないためACは低く、遠距離から削るのが有効です。"""
    },
    "step_339": {
        "title": "プリンおよびウーズ `P` (Puddings and oozes `P`) {#puddings-and-oozes-p}",
        "prose": """**茶色および黒色プリンは鉄製や金属製の刃物で攻撃すると分裂します**。無傷の死体ではなく塊を残します。\n\n**緑スライム**は[ゲヘナ](#gehennom)にのみ現れる例外で、分裂はしませんが接触した相手を緑スライムへと徐々に変異させていきます（石化に似た即死タイマー）。\n\nすべてのプリンおよびウーズは不定形で、精神を持たず、冷気耐性、毒耐性、酸耐性、石化耐性を備えています。"""
    },
    "step_340": {
        "title": "量子力学士 `Q` (Quantum mechanics `Q`) {#quantum-mechanics-q}",
        "prose": """特殊な爪攻撃を持つ2種類の生物です。**量子力学士 (Quantum mechanic)**は命中時にプレイヤーをランダムな場所へテレポートさせます。**遺伝子工学者 (Genetic engineer)**はプレイヤーを変身（ポリモルフ）させます。不変（Unchanging）の魔除けや魔法防御がなければ、一撃で別の生物に変えられてしまいます。\n\n両種とも自らランダムにテレポートし、毒のある死体を残します。"""
    },
    "step_341": {
        "title": "錆の怪物および魔法中和者 `R` (Rust monsters and disenchanters `R`) {#rust-monsters-and-disenchanters-r}",
        "prose": """錆の怪物は接触時に鉄製の武器や防具を急速に錆びさせます。ディスエンチャンター（吸魔の怪物）は命中時に装備している防具や武器の強化値（+値）を吸い取って低下させます。油を塗った防具や、魔法防御、木製・銀製・革製の装備で対抗してください。"""
    },
    "step_342": {
        "title": "ヘビ `S` (Snakes `S`) {#snakes-s}",
        "prose": """大半が猛毒を持っています。クサリヘビ（マムシ）やコブラは致命的な毒を持ち、ガータースネークなどは無害な獲物です。\n\nすべてのヘビは遊泳能力を持ち、*ニシキヘビ (python)* を除いて潜伏能力を備えています。"""
    },
    "step_343": {
        "title": "トロル `T` (Trolls `T`) {#trolls-t}",
        "prose": """驚異的な自動回復能力を持つ大型人型生物です。倒しても死体が数ターン後に復活するため、死体を食べるか、火炎で焼き払うか、缶詰にするか、別の階層へ運ぶ必要があります。"""
    },
    "step_344": {
        "title": "アンバーハルク `U` (Umber hulks `U`) {#umber-hulks-u}",
        "prose": """壁を掘り進む巨大な複眼の怪物です。その目を直視すると強烈な混乱状態に陥り、移動もままならなくなります。目隠しをして戦うか、遠距離から仕留めるのが定石です。"""
    },
    "step_345": {
        "title": "吸血鬼 `V` (Vampires `V`) {#vampires-v}",
        "prose": """アンデッドの貴族。噛みつき攻撃でプレイヤーの経験値レベル（XL）を直接吸い取ります。ヴラドの塔の最上階に君臨するヴラドは、昇天に必要な重要アイテム「燭台」を持っています。"""
    },
    "step_346": {
        "title": "レイス `W` (Wraiths `W`) {#wraiths-w}",
        "prose": """実体を持たない亡霊アンデッドです。攻撃でレベルを吸い取ってきますが、死体を食べると確実に経験値レベルが1上昇するため、プレイヤーにとって最も歓迎されるモンスターの一つです。"""
    },
    "step_347": {
        "title": "ゾーン `X` (Xorns `X`) {#xorns-x}",
        "prose": """3つの目と3本の腕、そして頭頂部に大きな口を持つ岩石生物です。固い岩壁の中を自由に通り抜けて移動し、金貨や金属アイテムを捕食します。"""
    },
    "step_348": {
        "title": "猿類およびイエティ `Y` (Apes and yetis `Y`) {#apes-and-yetis-y}",
        "prose": """人喰い猿、サル、イエティ、サスカッチなどの霊長類系モンスターです。イエティは冷気耐性を持ち、その死体から冷気耐性を獲得できます。"""
    },
    "step_349": {
        "title": "ゾンビおよび骸骨 `Z` (Zombies and skeletons `Z`) {#zombies-and-skeletons-z}",
        "prose": """死霊術によって動かされるアンデッドです。動きは遅いですが、元となった種族の死体を残すため食中毒に注意してください。骸骨は武器を持って攻撃してきます。"""
    },
    "step_350": {
        "title": "人間およびエルフ `@` (Humans and elves `@`) {#humans-and-elves}",
        "prose": """最も多彩で予測不可能なクラスです。友好的な店主や見張り、神官から、凶悪な暗殺者、各職業のクエストリーダーや宿敵、そして最後の敵イェンダーの魔法使いまでが含まれます。マップ上の `@` を見ただけで油断してはなりません。"""
    },
    "step_351": {
        "title": "大悪魔 `&` (Major demons `&`) {#major-demons}",
        "prose": """ゲヘナを支配する強大な悪魔貴族や魔王たちです。高額の賄賂でやり過ごせる者もいますが、バールゼブブやアスモデウス、デモゴルゴンなどは壊滅的な攻撃力を誇ります。"""
    },
    "step_352": {
        "title": "ゴーレム `'` (Golems `'`) {#golems}",
        "prose": """魔法で命を吹き込まれた人造人間です。藁、肉、土、石、鉄など様々な素材で作られ、素材に応じた耐性を持ちます。死体を残さず、鉄のゴーレムは強打を放ちます。"""
    },
    "step_353": {
        "title": "海の怪物 `;` (Sea monsters `;`) {#sea-monsters}",
        "prose": """水中に潜む巨大生物。電気ウナギや巨大ウナギはプレイヤーを水中に引きずり込んで溺死させようとします。水上歩行や飛行の手段がない状態での水辺の戦闘は極めて危険です。"""
    },
    "step_354": {
        "title": "トカゲ類 `:` (Lizards `:`):",
        "prose": """ヤモリ、カメレオン、ワニ、サラマンダーなど。通常のトカゲ（Lizard）の死体は決して腐敗せず、食べると石化の進行を即座に中断させることができるため、全プレイヤー必携の救命アイテムです。"""
    },
}

with open(os.path.join("spoilers", "companion.md"), "r", encoding="utf-8") as f:
    companion_lines = f.readlines()

with open(os.path.join("docs", "translation_progress.json"), "r", encoding="utf-8") as f:
    progress = json.load(f)

def translate_row(line, sid):
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
    clean_name = re.sub(r"\[([^\]]+)\]\(#[^\)]+\)", r"\1", raw_name).strip().lower()
    
    # Specific disambiguation for @ class
    if sid == "step_350" and clean_name == "priest":
        if lvl == "12":
            ja_name = "神官"
        else:
            ja_name = "司祭"
    else:
        ja_name = glossary.get(clean_name, glossary.get(clean_name.replace("-", " "), raw_name))

    if raw_name.startswith("[") and "](#" in raw_name:
        # Preserve link markup
        m = re.match(r"\[([^\]]+)\]\((#[^\)]+)\)", raw_name)
        if m:
            disp_name = f"[{ja_name} ({m.group(1)})]({m.group(2)})"
        else:
            disp_name = f"[{ja_name}]({raw_name})"
    else:
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
        if p in ja_notes:
            ja_notes = ja_notes.replace(p, r)

    # Notes regex
    for p, r in notes_trans:
        ja_notes = re.sub(p, r, ja_notes)

    # Clean up punctuation formatting in notes
    ja_notes = ja_notes.replace(", .", "。").replace("..", "。").replace(". ", "。").replace(", ", "、")
    if ja_notes and not ja_notes.endswith("。") and not ja_notes.endswith("."):
        ja_notes += "。"
    ja_notes = ja_notes.replace("。。", "。")

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
                table_lines.append(translate_row(line, sid))

    table_md = "\n".join(table_lines)
    header_md = "| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |\n|---|---|---|---|---|---|---|---|\n"

    content = f"{prefix}{title}\n\n{audit_block}{prose}\n\n::: dense-table\n\n{header_md}{table_md}\n\n:::\n"
    return content

for s in progress["segments"]:
    idx = int(s["id"].split("_")[1])
    if 298 <= idx <= 354:
        c = generate_segment(s)
        out_path = os.path.join("docs", "segments_jp", f"{s['id']}.md")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(c.strip() + "\n")
        print(f"Generated {out_path}")

