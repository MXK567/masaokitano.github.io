import re

def convert_sty_to_mathjax_macros(sty_text):
    newcommand_pattern = re.compile(r'\\newcommand\s*{\\(\w+)}(?:\[(\d+)\])?{(.+?)}')
    def_pattern = re.compile(r'\\def\\(\w+)(#\d)?{(.+?)}')

    macros = {}

    for match in newcommand_pattern.finditer(sty_text):
        name, nargs, body = match.groups()
        if nargs:
            macros[name] = [body, int(nargs)]
        else:
            macros[name] = body

    for match in def_pattern.finditer(sty_text):
        name, arg, body = match.groups()
        if arg:
            macros[name] = [body, int(arg[1])]
        else:
            macros[name] = body

    return macros

sty_content = r"""
\newcommand{\R}{\mathbb{R}}
\def\degree{\mbox{$^\circ$}}
\def\ii{{\mathrm{i}}}
\def\jj{\,\mathrm{j}}
\def\ee{{\mathrm{e}}}
\def\dd{{\mathrm{d}}}
\def\Re{\mathop{\mathrm{Re}}}
\def\Im{\mathop{\mathrm{Im}}}
\def\cc{\mbox{c.c.}}
\def\Hc{\mbox{H.c.}}
\def\bra#1{\langle #1|}
\def\ket#1{|\mbox{$#1$}\rangle}
\def\bracket#1{\langle\mbox{$#1$}\rangle}
\def\bracketi#1#2{\langle\mbox{$#1$}|\mbox{$#2$}\rangle}
\def\bracketii#1#2#3{\langle\mbox{$#1$}|\mbox{$#2$}|\mbox{$#3$}\rangle}
\def\diver{\mathop{\mathrm{div}}}
\def\curl{\mathop{\mathrm{curl}}}
\def\rot{\mathop{\mathrm{rot}}}
\def\grad{\mathop{\mathrm{grad}}}
\def\sub#1{_{\mbox{\scriptsize#1}}}
\def\sur#1{^{\mbox{\scriptsize#1}}}
\def\vct#1{{\mathchoice{\mbox{\boldmath$#1$}}{\mbox{\boldmath$#1$}}%
  {\mbox{\scriptsize\boldmath$#1$}}{\mbox{\scriptsize\boldmath$#1$}}}}
\def\ph#1{\tilde{#1}}
\def\fracpd#1#2{\frac{\partial#1}{\partial#2}}
\newcommand{\simD}[1][\text{\scriptsize SI}]{\stackrel{#1}{\sim}}
\def\U#1{\mathrm{#1}}}
\newcommand{\pdfrac}[2]{\frac{\partial#1}{\partial#2}}
\newcommand{\vnabla}{\vct{\nabla}}
\newcommand{\NN}{\nonumber\\}
\newcommand{\esu}[2][]{#2\sub{#1esu}}
\newcommand{\emu}[2][]{#2\sub{#1emu}}
\newcommand{\SI}[2][]{#2\sub{#1SI}}
\newcommand{\Gauss}[2][]{#2\sub{#1G}}
\newcommand{\sqdyn}{\sqrt{dyn}}
\newcommand{\Ufrac}[2]{\frac{\U{#1}}{\U{#2}}}
"""


macros = convert_sty_to_mathjax_macros(sty_content)
print(macros)

for k in macros:
    print(macros[k])
    
