# mc_git
tips to use github

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

# Header 1

## Header 2

### Header 3

code

```
pip install requirements.txt
```

[some link](https://www.google.com/)
