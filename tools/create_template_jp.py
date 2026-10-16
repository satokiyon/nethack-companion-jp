#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
spoilers/template.html から日本語版 spoilers/template.jp.html を生成するスクリプト。
すべての置換が確実に適用されたことをアサート検証する。
"""
import os


def replace_exact(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        raise RuntimeError(f"置換対象が見つかりません [{label}]:\n{old}")
    return text.replace(old, new, 1)


def main():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    src_path = os.path.join(root_dir, 'spoilers', 'template.html')
    dst_path = os.path.join(root_dir, 'spoilers', 'template.jp.html')

    with open(src_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. 基本ヘッダ・メタ情報の日本語化 & 印刷時空インデックス見出し非表示CSS
    html = replace_exact(html, '<html lang="en">', '<html lang="ja">', 'html lang')
    html = replace_exact(
        html,
        "<title>NetHack Spoilers: A Traveler's Companion to the Mazes of Menace</title>",
        "<title>NetHack スポイラー: 脅威の迷宮への旅人の手引き (5.0対応版)</title>",
        'title'
    )
    html = replace_exact(
        html,
        'family=EB+Garamond',
        'family=Noto+Serif+JP:wght@400;600;700&family=Noto+Sans+JP:wght@400;500;700&family=EB+Garamond',
        'google fonts'
    )
    html = replace_exact(
        html,
        '  <link rel="stylesheet" href="style.css">\n</head>',
        '  <link rel="stylesheet" href="style.css">\n  <style>@media print { #index-of-useful-knowledge { display: none !important; } }</style>\n</head>',
        'print style for index-of-useful-knowledge'
    )

    # 2. サイドバー・リボン等のUI文言
    html = replace_exact(html, '<div class="sidebar-title">Contents</div>', '<div class="sidebar-title">目次</div>', 'sidebar toc title')
    html = replace_exact(html, '<div class="sidebar-title">Search</div>', '<div class="sidebar-title">検索</div>', 'sidebar search title')
    html = replace_exact(html, 'placeholder="Search the guide..."', 'placeholder="ガイド内を検索..."', 'search placeholder')
    html = replace_exact(html, '<span class="page-fold-text">New!<br>Updated for 5.0</span>', '<span class="page-fold-text">5.0対応<br>完全改訂</span>', 'page-fold-text')

    # 3. TOC アイコンマップのアンカーID修正 ('wands-and-staves' -> 'wands')
    html = replace_exact(
        html,
        "    'wands-and-staves':   glyph('/'),",
        "    'wands':              glyph('/'),",
        'sectionIcons wands'
    )

    # 4. 検索ロジックの日本語対応 (文境界判定・見出し一致ボーナス・1文字検索許可・結果UI文字列)
    html = replace_exact(
        html,
        "      if (c === 46 || c === 33 || c === 63) {  // .!?",
        "      if (c === 46 || c === 33 || c === 63 || c === 0x3002 || c === 0xFF01 || c === 0xFF1F) {  // .!?。！？",
        'sentenceContaining start'
    )
    html = replace_exact(
        html,
        "      if (cc === 46 || cc === 33 || cc === 63) { end = k; break; }",
        "      if (cc === 46 || cc === 33 || cc === 63 || cc === 0x3002 || cc === 0xFF01 || cc === 0xFF1F) { end = k; break; }",
        'sentenceContaining end'
    )

    old_title_bonus = """  function titleMatchBonus(title, word) {
    var contentWords = title.toLowerCase().split(/\\s+/).map(function(w) {
      return w.replace(/[^a-z0-9]/g, '');
    }).filter(function(w) { return w && !STOPWORDS[w]; });
    if (contentWords.length === 0) return 0;"""

    new_title_bonus = """  function titleMatchBonus(title, word) {
    var lowerTitle = title.toLowerCase();
    if (/[^\\x00-\\x7F]/.test(word)) {
      if (lowerTitle.indexOf(word) === -1) return 0;
      var jpTitle = lowerTitle.replace(/\\s*\\([^)]*\\)\\s*/g, '').trim() || lowerTitle;
      var ratio = Math.min(1.0, word.length / Math.max(1, jpTitle.length));
      return 50 * Math.max(0.5, ratio);
    }
    var contentWords = lowerTitle.split(/\\s+/).map(function(w) {
      return w.replace(/[^a-z0-9]/g, '');
    }).filter(function(w) { return w && !STOPWORDS[w]; });
    if (contentWords.length === 0) return 0;"""

    html = replace_exact(html, old_title_bonus, new_title_bonus, 'titleMatchBonus JP support')

    html = replace_exact(
        html,
        """  function doSearch() {
    var query = searchInput.value.trim().toLowerCase();
    if (query.length < 2) {""",
        """  function doSearch() {
    var query = searchInput.value.trim().toLowerCase();
    var minLen = /[^\\x00-\\x7F]/.test(query) ? 1 : 2;
    if (query.length < minLen) {""",
        'doSearch 1-char JP query'
    )

    html = replace_exact(
        html,
        """    if (matches.length === 0) {
      searchResults.innerHTML = '<div class="search-empty">No results found.<br><span class="search-hint">The dungeon keeps its secrets.</span></div>';
      return;
    }""",
        """    if (matches.length === 0) {
      searchResults.innerHTML = '<div class="search-empty">一致する項目が見つかりません。<br><span class="search-hint">迷宮は秘密を隠し通している。</span></div>';
      return;
    }""",
        'search-empty JP message'
    )

    html = replace_exact(
        html,
        """    if (matches.length > shown) {
      html += '<div class="search-more">' + (matches.length - shown) + ' more results...</div>';
    }""",
        """    if (matches.length > shown) {
      html += '<div class="search-more">他 ' + (matches.length - shown) + ' 件の結果...</div>';
    }""",
        'search-more JP message'
    )

    # 5. 右サイドバー初期表示「有用な知識の索引 (Index of Useful Knowledge)」全32項目の日本語化（五十音順）とリンク切れID修正
    old_index_block = """  // --- Humorous index (shown when search is empty) ---
  var indexEntries = [
    ['Amorous demon, expensive evening with', 'seduction'],
    ['Amulet of Yendor, retrieving', 'the-ascension-run'],
    ['Ascension, how to not die during', 'the-ascension-run'],
    ['Boulders, pushing (see: Sokoban)', 'sokoban-solutions'],
    ['BUC, avoiding curses by checking', 'blessed-uncursed-cursed-buc'],
    ['Castle, storming the', 'the-castle'],
    ['Cockatrice corpse, wielding', 'petrification-stoning'],
    ['Death, causes of (see: everything)', 'things-that-will-kill-you'],
    ['Disenchanter, mourning your former +5', 'enchantment-drain'],
    ['Displacer beast, taming', 'the-displacer-beast'],
    ['Drowning, preventable', 'drowning'],
    ['Elbereth, writing frantically', 'engravings'],
    ['Floating eye, do not hit', 'eyes-and-spheres-e'],
    ['Food, running out of', 'how-hunger-works'],
    ['Gehennom, why is it so hot', 'gehennom'],
    ['Gods, angering', 'altars-and-alignment'],
    ['Identify, never enough scrolls of', 'the-scroll-rack'],
    ['Luck, secretly ruining yours', 'gaining-and-losing-luck'],
    ['Lurker above, looking up too late', 'engulfment'],
    ['Mines, gnomish', 'the-gnomish-mines'],
    ['Pet, accidentally killing your', 'keeping-your-pet-alive'],
    ['Prayer, when to', 'prayer'],
    ['Shopkeeper, angering', 'shopping-and-shopkeeper-pricing'],
    ['Sokoban, solving without cheating', 'sokoban-solutions'],
    ['Stoning, avoiding', 'petrification-stoning'],
    ['Tourists, playing as', 'choosing-your-expedition'],
    ['Unicorn horn, no longer a cure-all', 'what-changed-since-last-time'],
    ['Vlad&rsquo;s throne, fourth sit&rsquo;s the charm', 'vlads-tower'],
    ['Wand, identifying by engraving', 'identification-by-engraving'],
    ['Wand of wishing, found with one charge', 'the-castle'],
    ['Wishes, optimal use of', 'what-to-wish-for'],
    ['YASD, inevitability of', 'your-first-descent'],
  ];

  var indexHtml = '<div class="humorous-index"><div class="index-title">Index of Useful Knowledge</div>';"""

    new_index_block = """  // --- Humorous index (shown when search is empty) ---
  var indexEntries = [
    ['イェンダーの魔除け（奪還作戦）', 'the-ascension-run'],
    ['祈り（いつ祈るべきか）', 'prayer'],
    ['岩押し（参照：倉庫番）', 'sokoban-solutions'],
    ['ヴラドの玉座（4度目の正直）', 'vlads-tower'],
    ['運（知らぬ間に自滅している理由）', 'gaining-and-losing-luck'],
    ['エルベレス（半狂乱で床に刻む）', 'engravings'],
    ['溺れ死に（防げたはずの）', 'drowning'],
    ['神々（怒らせてしまったら）', 'altars-and-alignment'],
    ['観光客（あえて選ぶなら）', 'choosing-your-expedition'],
    ['吸魔の怪物（かつて+5だった武器を悼む）', 'enchantment-drain'],
    ['ゲヘナ（なぜこれほど暑いのか）', 'gehennom'],
    ['幻影の獣（手懐ける）', 'felines-f'],
    ['コカトリスの死体（武器として振り回す）', 'petrification-stoning'],
    ['さまよう目（決して殴るな）', 'eyes-and-spheres-e'],
    ['死因（参照：すべて）', 'things-that-will-kill-you'],
    ['識別の巻物（いくらあっても足りない）', 'the-scroll-rack'],
    ['城（突入作戦）', 'the-castle'],
    ['昇天（その途中で死なない方法）', 'the-ascension-run'],
    ['食料（尽き果てたとき）', 'how-hunger-works'],
    ['好色な悪魔（高くつく一夜）', 'seduction'],
    ['石化（回避する方法）', 'petrification-stoning'],
    ['倉庫番（ズルせずに解く）', 'sokoban-solutions'],
    ['杖（床に刻んで識別する）', 'the-engrave-test-wands'],
    ['店主（怒らせてしまったら）', 'shopping-and-shopkeeper-pricing'],
    ['願い（最適な使い道）', 'what-to-wish-for'],
    ['願いの杖（残り1回で見つかる）', 'the-castle'],
    ['ノームの鉱山（攻略）', 'the-gnomish-mines'],
    ['BUC（確認して呪いを避ける）', 'blessed-uncursed-cursed-buc'],
    ['ペット（うっかり殺してしまったら）', 'keeping-your-pet-alive'],
    ['ユニコーンの角（もはや万能薬ではない）', 'what-changed-since-last-time'],
    ['ラーカー（見上げた時にはもう遅い）', 'engulfment'],
    ['YASD（避けられぬくだらない死）', 'your-first-descent'],
  ];

  var indexHtml = '<div class="humorous-index"><div class="index-title">有用な知識の索引</div>';"""

    html = replace_exact(html, old_index_block, new_index_block, 'indexEntries JP translation and target IDs')

    # 6. 倉庫番 (Sokoban) 反転ボタンの日本語化と日本語手順テキストの方向反転対応
    old_sokoban_words = """  // Direction-word mappings used for solution prose.
  var H_WORD = {'left':'right','right':'left'};
  var V_WORD = {'up':'down','down':'up'};"""

    new_sokoban_words = """  // Direction-word mappings used for solution prose.
  var H_WORD = {'left':'right','right':'left'};
  var V_WORD = {'up':'down','down':'up'};
  var H_WORD_JP = {'左へ':'右へ','右へ':'左へ'};
  var V_WORD_JP = {'上へ':'下へ','下へ':'上へ'};"""

    html = replace_exact(html, old_sokoban_words, new_sokoban_words, 'sokoban H_WORD_JP / V_WORD_JP')

    old_transform_prose = """  function transformProse(html, width, height) {
    if (state.h) {
      html = html.replace(/\\b(left|right)\\b/g, function(w) {
        return H_WORD[w];
      });
    }
    if (state.v) {
      html = html.replace(/\\b(up|down)\\b/g, function(w) {
        return V_WORD[w];
      });
    }"""

    new_transform_prose = """  function transformProse(html, width, height) {
    if (state.h) {
      html = html.replace(/\\b(left|right)\\b/g, function(w) {
        return H_WORD[w];
      }).replace(/(左へ|右へ)/g, function(w) {
        return H_WORD_JP[w];
      });
    }
    if (state.v) {
      html = html.replace(/\\b(up|down)\\b/g, function(w) {
        return V_WORD[w];
      }).replace(/(上へ|下へ)/g, function(w) {
        return V_WORD_JP[w];
      });
    }"""

    html = replace_exact(html, old_transform_prose, new_transform_prose, 'sokoban transformProse JP')

    old_flipbar = """    bar.innerHTML =
      '<button type="button" data-flip="h" title="Mirror left-right">' +
      'Flip ↔</button>' +
      '<button type="button" data-flip="v" title="Mirror top-bottom">' +
      'Flip ↕</button>';"""

    new_flipbar = """    bar.innerHTML =
      '<button type="button" data-flip="h" title="左右反転">' +
      '左右反転 ↔</button>' +
      '<button type="button" data-flip="v" title="上下反転">' +
      '上下反転 ↕</button>';"""

    html = replace_exact(html, old_flipbar, new_flipbar, 'sokoban flipbar buttons JP')

    with open(dst_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print("spoilers/template.jp.html generated successfully.")


if __name__ == '__main__':
    main()
