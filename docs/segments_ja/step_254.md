#### 完全聾 (Permadeaf: 5.0新要素)

<!-- audit
2026-05-19:
- permadeaf is u.uroleplay.deaf, in xlogfile (topten.c:602) and show_conduct (insight.c:2113)
- Deaf macro at youprop.h:125
- rcfile option name is `permadeaf` (or `deaf`), NOT `!acoustics` (a different flavor flag, flags.acoustics) (optlist.h:267-269 declares `deaf` with alias "permadeaf" binding u.uroleplay.deaf; optlist.h:143-145 declares `acoustics` binding flags.acoustics — separate flag)
- permadeaf is set_in_config: rcfile only, not in-game O menu (options.c:5207)
- there is no `-Dpermadeaf` syntax; `-D` is the debug/wizard-mode flag (unixmain.c:359-365)
- Deaf only suppresses shrieker MESSAGES; makemon and aggravate still run (mon.c:4089-4106)
-->

いかなる音も聞こえない状態でプレイします。設定ファイルに `OPTIONS=permadeaf`（または `OPTIONS=deaf`）を記述します（設定ファイル専用であり、ゲーム内の `O` メニューでは切り替えられません。無関係な効果音設定の `acoustics` と混同しないようにしてください）。ゲームは第1ターンから恒久的な難聴（Deaf）の特性を持った状態として進行します：「水が流れる音がする」「誰かが金を数えている音がする」「扉が開く音がする」といった環境音メッセージや、モンスターの気配（「ズルズルという音がする」等）のメッセージがすべて抑制されます。

抑制されるのは *メッセージの表示だけ* です。叫びキノコ（シュリーカー）は依然として叫び声をあげ、モンスターを召喚し、フロア全体を怒らせます（あなたにその警告メッセージが表示されないだけです）。`F` クラスのキノコの近くの不気味な静寂を、通常の「叫び声をあげた」メッセージと同等の致命的脅威として察知しなければなりません。

完全聾プレイでは、視覚と論理的推論だけを頼りに迷宮を探索します。

