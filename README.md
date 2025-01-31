# mc_git
tips to use github

## План
<ol start="1">
<li>Создание репозитория github</li>
<li>
  
  [Клонирование по ssh и https](https://github.com/GenerativeMolMachines/mc_git?tab=readme-ov-file#%D0%BA%D0%BB%D0%BE%D0%BD%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BF%D0%BE-ssh)
</li>
<li>
  
  [Твой первый коммит](https://github.com/GenerativeMolMachines/mc_git?tab=readme-ov-file#%D0%BA%D0%BE%D0%BC%D0%B0%D0%BD%D0%B4%D1%8B-git)
</li>
<li>
  
  [Ветки](https://github.com/GenerativeMolMachines/mc_git?tab=readme-ov-file#%D0%BA%D0%BE%D0%BC%D0%B0%D0%BD%D0%B4%D1%8B-git)
</li>
<li>Просмотр истории</li>
<li>
  
  [Pull requests](https://github.com/GenerativeMolMachines/mc_git?tab=readme-ov-file#%D0%BA%D0%BE%D0%BC%D0%B0%D0%BD%D0%B4%D1%8B-git)</li>
<li>
  
  [Конфликты](https://github.com/GenerativeMolMachines/mc_git?tab=readme-ov-file#%D0%BA%D0%BE%D0%BC%D0%B0%D0%BD%D0%B4%D1%8B-git)</li>
<li>
  
  [Файловая структура](https://github.com/GenerativeMolMachines/mc_git?tab=readme-ov-file#%D1%84%D0%B0%D0%B9%D0%BB%D0%BE%D0%B2%D0%B0%D1%8F-%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%82%D1%83%D1%80%D0%B0)</li>
<li>
  
  [README.md и Wiki](https://github.com/GenerativeMolMachines/mc_git?tab=readme-ov-file#%D1%84%D0%B0%D0%B9%D0%BB%D0%BE%D0%B2%D0%B0%D1%8F-%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%82%D1%83%D1%80%D0%B0)</li>
</ol>
<br>
Если очень хочется поглубже в теорию, хорошее видео - 

[Git — инструмент для совместной работы, с нуля и до регламента в команде — Сергей Сергеев](https://youtu.be/yDSs80lu3ak?si=DmuxVQHfsHyKD7_8)
<br>

## клонирование по ssh
Создания ключей
```
ssh-keygen
```
```
cat ~/.ssh/id_rsa.pub
```
Клонирование
```
git clone git@github.com:djzhendogg/test.git
```
```
git clone https://github.com/djzhendogg/test.git
```

## команды git

```
git fetch
```
```
git pull
```
```
git add
```
```
git commit -m
```
```
git push (если новая то, upsteam)
```
```
git restore
```
```
git checkout (если новая -b)
```
```
git merge
```
```
git rebase
```
## Файловая структура
| -- project \
&emsp; &emsp;| -- .gitignore \
&emsp; &emsp;| -- README.md \
&emsp; &emsp;| -- requirements.txt \
&emsp; &emsp;| -- pyproject.toml \
&emsp; &emsp;| -- run_model.py \
&emsp; &emsp;| -- data \
&emsp; &emsp;&emsp; &emsp;| -- peptides.csv \
&emsp; &emsp;| -- model \
&emsp; &emsp;&emsp; &emsp;| -- model_v2.pkl \
&emsp; &emsp;| -- src \
&emsp; &emsp;&emsp; &emsp;| -- learning \
&emsp; &emsp;&emsp; &emsp;&emsp; &emsp;| -- learning.py \
&emsp; &emsp;&emsp; &emsp;&emsp; &emsp;| -- learning_tools.py \
&emsp; &emsp;&emsp; &emsp;| -- data_processing \
&emsp; &emsp;&emsp; &emsp;&emsp; &emsp;| -- merge.py \
&emsp; &emsp;&emsp; &emsp;&emsp; &emsp;| -- filling.py \
&emsp; &emsp;&emsp; &emsp;| -- analysis \
&emsp; &emsp;&emsp; &emsp;&emsp; &emsp;| -- statictics.py \
&emsp; &emsp;&emsp; &emsp;&emsp; &emsp;| -- DBSCAN.py 


# For read.me

[Дока базового синтаксиса записи и форматирования](https://docs.github.com/ru/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)

# Header 1

## Header 2

### Header 3

code

```
pip install requirements.txt
```

[some link](https://www.google.com/)
