#!/usr/bin/env python3
"""
NetHack Companion 日本語版 ビルドスクリプト (Python)
companion.ja.md → index.ja.html → companion.ja.pdf
"""

import os
import subprocess
import sys

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

def build(skip_pdf=False):
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    spoilers_dir = os.path.join(root_dir, 'spoilers')
    os.chdir(spoilers_dir)

    # Pandoc のパス追加 (Windows)
    pandoc_candidates = [
        os.path.expandvars(r"%LOCALAPPDATA%\Pandoc"),
        r"C:\Users\satok\AppData\Local\Pandoc",
        r"C:\Program Files\Pandoc",
        r"C:\Program Files (x86)\Pandoc"
    ]
    for pc in pandoc_candidates:
        if os.path.exists(pc) and pc not in os.environ.get('PATH', ''):
            os.environ['PATH'] = pc + os.pathsep + os.environ.get('PATH', '')
            break

    print("=== 1. ASCII マップ整合性検証 ===")
    ja_md = 'companion.ja.md'
    if os.path.exists(ja_md):
        try:
            res = subprocess.run([sys.executable, 'check_ascii_maps.py', ja_md], capture_output=True, text=True)
            if res.returncode == 0:
                print("✓ ASCII マップ検証に合格しました。")
            else:
                print("警告: ASCII マップ検証で警告が発生しました:\n", res.stdout, res.stderr)
        except Exception as e:
            print(f"ASCII マップ検証の実行をスキップしました ({e})")
    else:
        print("companion.ja.md が存在しないためスキップします。")

    print("\n=== 2. 日本語 HTML 版のビルド (Pandoc) ===")
    cmd_pandoc = [
        'pandoc',
        ja_md,
        '--from=markdown',
        '--to=html5',
        '--template=template.ja.html',
        '--section-divs',
        '--syntax-highlighting=none',
        '--output=index.ja.html'
    ]
    
    try:
        subprocess.run(cmd_pandoc, check=True)
        print("✓ index.ja.html を正常に生成しました。")
    except FileNotFoundError:
        print("エラー: pandoc が見つかりません。PATH を確認してください。")
        return False
    except subprocess.CalledProcessError as e:
        print(f"エラー: Pandoc の変換に失敗しました: {e}")
        return False

    if not skip_pdf:
        print("\n=== 3. 日本語 PDF 版のビルド (Edge / Chromium Headless) ===")
        edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
        chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        browser_path = None

        if os.path.exists(chrome_path):
            browser_path = chrome_path
        elif os.path.exists(edge_path):
            browser_path = edge_path

        if browser_path:
            import tempfile
            html_abs = os.path.abspath('index.ja.html')
            pdf_out = os.path.abspath('companion.ja.pdf')
            html_uri = 'file:///' + html_abs.replace('\\', '/')
            temp_profile = os.path.join(tempfile.gettempdir(), 'nh_pdf_profile')
            
            print(f"ブラウザ ({os.path.basename(browser_path)}) で PDF レンダリング中...")
            cmd_browser = [
                browser_path,
                '--headless',
                '--disable-gpu',
                '--no-pdf-header-footer',
                f'--print-to-pdf={pdf_out}',
                html_uri
            ]
            try:
                subprocess.run(cmd_browser, check=True)
                if os.path.exists(pdf_out):
                    size_kb = os.path.getsize(pdf_out) // 1024
                    print(f"✓ companion.ja.pdf を正常に生成しました ({size_kb} KB)。")
                else:
                    print("警告: PDF ファイルが生成されませんでした。")
            except Exception as e:
                print(f"エラー: PDF 生成中にエラーが発生しました: {e}")
        else:
            print("Edge/Chrome が見つからないため PDF 生成をスキップしました。")

    print("\n=== ビルド完了 ===")
    return True

if __name__ == '__main__':
    skip = '--skip-pdf' in sys.argv
    build(skip_pdf=skip)