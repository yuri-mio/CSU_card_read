import os

from DrissionPage import ChromiumPage

from utils import code_input, login, pushplus

# 创建 driver
driver = ChromiumPage()
driver.get("https://ecard.csu.edu.cn/plat-pc/login")

# 从环境变量读取账号密码
COUNT = os.environ["COUNT"]
PWD = os.environ["PASSWORD"]
PUSH_PLUS_TOKEN = os.environ["PUSH_PLUS_TOKEN"]
GITHUB_TRIGGERING_ACTOR = os.environ["GITHUB_TRIGGERING_ACTOR"]

# 账号输入
count_input = driver.ele("@type=text")
count_input.input("8212210728")

# 密码输入
pwd_input = driver.ele("@type=password")
pwd_input.input("121517")

code_input(driver)
login(driver)


card_body = driver.ele("css:#cardService > div > div:nth-child(1) > div > div > div")
card_body.click()
remain = driver.ele(".value font-size-18")
cost = remain.text[1:]
print(remain.text[1:])
driver.quit()
pushplus(float(cost), COUNT, GITHUB_TRIGGERING_ACTOR, PUSH_PLUS_TOKEN)
