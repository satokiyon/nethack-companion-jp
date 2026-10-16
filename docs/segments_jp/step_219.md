### 高度な操作法 (Advanced Controls) {#advanced-controls}

<!-- audit
2026-07-30 accuracy pass vs NetHack-5.0 source:
- runmode sets display refresh rate during a run (teleport/run/walk/crawl = no-redraw / every-7 / every-step / step+delay, flag.h:547-551), not stopping behavior. Reworded.
- Verified correct: all command bindings (F/G/g/m/_/@/^A/^P/^R/^O/v), count cap 32767, paranoid_confirmation values, pickup_burden default, autopickup_exception, statushilites, pickup_types etc.
-->
<!-- audit
2026-05-19:
- F/G/g/m/O/v/_/;//, Ctrl+A/P/R/O, #overview, #chronicle, #annotate, #conduct all verified (cmd.c:1662-2065)
- `verbose` controls extra descriptive messages (wielding/digging/sounds/pets), NOT "why multi-commands stopped" (optlist.h:813-815 declares flags.verbose; gated at dig.c:711/1441/1468/2157, ball.c:61, attrib.c:176, apply.c:438 etc. — none are multi-command stop messages)
- double-tap F cancels the attack lock (cmd.c:1622-1633)
- `m` prefix on e/a/, opens a menu
- Ctrl+A repeats only the last EXECUTED command, not the last input (cmd.c:3732-3736)
- repeat-count cap is 32767 (global.h:135)
- number_pad/autopickup/pickup_types option semantics consistent with optlist.h
2026-05-31 audit:
- travel command (`_`) enters background-symbol-target mode (getpos.c:194-218). Typing a background symbol after `_` jumps the cursor to the next instance; `.` confirms and walks. So the patterns are `_<.` (upstair), `_>.` (downstair), `__.` (altar). The book originally showed `__` without the trailing `.`, which is inconsistent with the other two.
-->

基本的なキー操作だけで迷宮のあらゆる状況を乗り切ることは可能ですが、以下に挙げるコマンドを活用すれば遥かに素早く快適に操作できます。何千ターンにもわたって `s` キーを連打したり、通路を1マスずつ歩いたりした経験があれば、これらのショートカットがいかに指先に馴染むかを実感できるはずです。
