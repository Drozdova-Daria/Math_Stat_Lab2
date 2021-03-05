# Математическая статистика. Лабораторная работа №2

Требуется построить выборки размером 10, 100, 1000 элементов для следующих распределений:
- Нормальное распределение <a href="https://www.codecogs.com/eqnedit.php?latex=N(x,0,1)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?N(x,0,1)" title="N(x,0,1)" /></a>
- Распределение Коши <a href="https://www.codecogs.com/eqnedit.php?latex=C(x,0,1)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?C(x,0,1)" title="C(x,0,1)" /></a>
- Распределение Лапласа <a href="https://www.codecogs.com/eqnedit.php?latex=L(x,0,\sqrt{2})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?L(x,0,\sqrt{2})" title="L(x,0,\sqrt{2})" /></a>
- Распределение Пуассона <a href="https://www.codecogs.com/eqnedit.php?latex=P(k,10)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?P(k,10)" title="P(k,10)" /></a>
- Равномерное распределение <a href="https://www.codecogs.com/eqnedit.php?latex=U(x,-\sqrt{3},&space;\sqrt{3})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?U(x,-\sqrt{3},&space;\sqrt{3})" title="U(x,-\sqrt{3}, \sqrt{3})" /></a>

Для каждой выборки каждого распределение вычислить статистические положения данных:
- Выборочное среднее - <a href="https://www.codecogs.com/eqnedit.php?latex=\overline{x}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\overline{x}" title="\overline{x}" /></a>
- Выборочная медиана - <a href="https://www.codecogs.com/eqnedit.php?latex=med\;x" target="_blank"><img src="https://latex.codecogs.com/gif.latex?med\;x" title="med\;x" /></a>
- Полусумма экстремальных выборочных элементов - <a href="https://www.codecogs.com/eqnedit.php?latex=z_R" target="_blank"><img src="https://latex.codecogs.com/gif.latex?z_R" title="z_R" /></a>
- Полусумма квартилей - <a href="https://www.codecogs.com/eqnedit.php?latex=z_Q" target="_blank"><img src="https://latex.codecogs.com/gif.latex?z_Q" title="z_Q" /></a>
- Усеченое среднее - <a href="https://www.codecogs.com/eqnedit.php?latex=z_{tr}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?z_{tr}" title="z_{tr}" /></a>

Повторить вычисления 1000 раз для каждой выборки и найти среднее характеристик положения и их квадратов: <a href="https://www.codecogs.com/eqnedit.php?latex=E(z)=\overline{z}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?E(z)=\overline{z}" title="E(z)=\overline{z}" /></a>
Вычислить оценку дисперсии по формуле: <a href="https://www.codecogs.com/eqnedit.php?latex=D(z)=\overline{z^2}&space;-&space;\overline{z}^2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?D(z)=\overline{z^2}&space;-&space;\overline{z}^2" title="D(z)=\overline{z^2} - \overline{z}^2" /></a>
Полученные данные представить в виде таблиц

Программа выполнена на языке программирования Python с использованием библиотек ```skipy, nympy ``` для построения выборок и вычисления плотности вероятности. 
