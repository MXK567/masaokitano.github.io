import re

def convert_sty_to_mathjax_v5(sty_file_path, output_js_path):
    """
    LaTeX の .sty ファイルを解析し、MathJax で利用するための JavaScript コードを生成するスクリプト (引数ありのコマンドと \def に対応、バックスラッシュと右 curly bracket のエスケープを修正、波括弧の閉じ忘れを修正)。
    すべての .sty ファイルに対応できるわけではありません。
    """
    macros = {}

    with open(sty_file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line.startswith('%'):
                continue

            # \newcommand の解析 (引数あり)
            newcommand_match = re.match(r'\\newcommand{\\(.+?)}\[(\d+)\]{(.+?)}', line)
            if newcommand_match:
                command = newcommand_match.group(1)
                num_args = int(newcommand_match.group(2))
                definition = newcommand_match.group(3).replace('\\', '\\\\').replace('}', '\\}')
                macros[command] = [definition]
                continue

            # \newcommand の解析 (引数なし)
            newcommand_noarg_match = re.match(r'\\newcommand{\\(.+?)}{(.+?)}', line)
            if newcommand_noarg_match:
                command = newcommand_noarg_match.group(1)
                definition = newcommand_noarg_match.group(2).replace('\\', '\\\\').replace('}', '\\}')
                macros[command] = [definition]
                continue

            # \def の解析
            def_match = re.match(r'\\def\\(.+?)(?:#(\d+))?{(.+?)}', line)
            if def_match:
                command = def_match.group(1)
                arg_num_str = def_match.group(2)
                definition = def_match.group(3).replace('\\', '\\\\').replace('}', '\\}')
                if arg_num_str:
                    num_args = int(arg_num_str)
                    macros[command] = [definition]
                else:
                    macros[command] = [definition]
                continue

            # より複雑なコマンド定義はここでは扱いません

    # MathJax の設定を記述した JavaScript コードを生成
    js_code = "MathJax = {\n  tex: {\n    macros: {\n"
    macro_items = []
    for cmd, defs in macros.items():
        macro_items.append(f"      '{cmd}': ['{defs[0]}']")
    js_code += ",\n".join(macro_items)
    if macro_items:
        js_code += "\n    }\n  }\n};\n"
    else:
        js_code += "    }\n  }\n};\n"

    # JavaScript ファイルに保存
    with open(output_js_path, 'w', encoding='utf-8') as f:
        f.write(js_code)

    print(f"'{sty_file_path}' を解析し、'{output_js_path}' に MathJax 設定を保存しました (波括弧の閉じ忘れを修正)。")

# スクリプトの使用例
if __name__ == "__main__":
    sty_file = 'unit.sty'  # 変換したい .sty ファイルのパス
    output_js = 'mathjax_config.js'  # 出力する JavaScript ファイルのパス
    convert_sty_to_mathjax_v5(sty_file, output_js)
