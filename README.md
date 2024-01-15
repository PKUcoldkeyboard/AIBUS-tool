# Aibus-tool
自动打卡AIbus

## 安装chrome

```shell
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt-get update
sudo apt install ./google-chrome-stable_current_amd64.deb
```

- 验证是否安装成功

```shell
google-chrome --version
```

## 安装chromedriver

- chromedriver 对应 google chrome 第一个大数字就行，比如 `119` 。

```shell
wget https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/{google chrome 版本号}/linux64/chromedriver-linux64.zip
unzip chromedriver-linux64.zip;
sudo mv ./chromedriver-linux64/chromedriver /usr/bin/
```

- 验证一下

```shell
chromedriver --version
```

## 安装依赖库

```shell
pip3 install -r requirements.txt
```

## 克隆项目

```shell
git clone https://github.com/PKUColdkeyboard/AIBUS-tool.git
```

## 配置文件
### config.ini
- 用于登录 AIBUS 网站的账号与密码

### apikey.json
请首先将 apikey.sample.json 复制一份并改名为 apikey.json，并按照以下说明进行配置。

该文件为 [TT识图](http://www.ttshitu.com/) 平台的 API 密钥，在平台注册后，填入用户名与密码即可。由于该 API 需要收费，须在平台充值后方可使用（1 RMB 足够用到天荒地老了，实际测试识别一次计算题验证码需要 0.008 RMB）。

```json
{
    "username": "yourusername",
    "password": "yourpassword"
}
```


## 运行项目

```shell
mv config.example.ini config.ini
mv apikey.sample.json apikey.json

# 然后修改 config.ini 为自己账号，修改 apikey.json 为自己在 TT 识图上注册的账号

python3 main.py
```

## 定时运行

- 自行查阅 `crontab` 用法，只要项目目录中有 `config.ini` 这个文件，然后设置执行 `python3 main.py` 就行。
- 要支持多账号签到，提前创建几个文件如 `config.ini.1` ，`config.ini.2` 等，每个文件放入一个账号，然后定时的时候加一行 `mv config.ini.1 config.ini` ，有几个账号就重复几次 `mv` 和 `python3 main.py` 的步骤。
