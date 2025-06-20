% 2012/08/18 14:04:54(3票)
```{tags} ノート, 電磁気学, 微分形式
```

# Levi-Civita の記号の縮約公式の幾何学的解釈

3階の完全反対称テンソル(レヴィ・チビタの記号)の縮約公式は添え字による
ベクトル解析の計算において中心的な働きをしている.
いろいろな導出方法があるが, ここでは幾何学的意味を中心にした方法を提示する.
これによって公式が自然なものに見えるようになり, わざわざ覚える必要がなくなるであろう.
「新版マクスウェル方程式」問題A3の解答例にもなっている.

[pdf](levi-civita.pdf)

---

## 別解

Levi-Civita の公式
\begin{align*}
\sum_{i=1}^3 e_{ijk}e_{ilm}
= \delta_{jl}\delta_{km}  - \delta_{jm}\delta_{kl}   
\end{align*}
はベクトル解析の公式の証明に使われるが,
ここでは, 逆にベクトル解析の公式から Levi-Civita の式を導いてみよう.
まず, 正規直交基底 $(\vct e_1,\vct e_2,\vct e_3)$
に対して
\begin{align*}
e_{ijk} = \vct e_i\cdot(\vct e_j\times\vct e_k)
= (\vct e_j\times\vct e_k)_i
\end{align*}
が成り立つ.
ベクトル解析の公式
$
\vct a\cdot(\vct b\times\vct c) = \vct c\cdot(\vct a\times\vct b)
$
,
$
\vct a\times(\vct b\times\vct c)
= \vct b(\vct a\cdot\vct c) - \vct c(\vct a\cdot\vct b)
$
を用いると,
\begin{align*}
\text{左辺}
&=
 (\vct e_j\times\vct e_k)\cdot(\vct e_l\times\vct e_m)
=  \vct e_l\cdot[\vct e_m\times(\vct e_j\times\vct e_k)]
\\
&=   \vct e_l\cdot
  [\vct e_j(\vct e_m\cdot\vct e_k)
   - \vct e_k(\vct e_m\cdot\vct e_j)]
= \text{右辺}
\end{align*}
となる.
