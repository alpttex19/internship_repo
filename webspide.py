import argparse
import json
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC



def get_exchange_rate(date, currency):

    try:
        # 将日期从 "YYYYMMDD" 格式转换为 "YYYY-MM-DD" 格式
        date = datetime.strptime(date, "%Y%m%d").strftime("%Y-%m-%d")
        # 读入json文件，根据中文名获取货币代码
        with open("output.json", "r", encoding="utf-8") as f:
            currency_dict = json.load(f)
        currency_name = currency_dict[currency]

        # 设置 ChromeDriver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        # 打开中国银行外汇牌价网页
        driver.get("https://www.boc.cn/sourcedb/whpj/")
        # 等待页面加载完成
        driver.implicitly_wait(10)
        
        # 定位到输入框
        begin_date = driver.find_element(By.NAME, "erectDate")
        begin_date.clear()
        begin_date.send_keys(date)

        # 定位到输入框
        end_date = driver.find_element(By.NAME, "nothing")
        end_date.clear()
        end_date.send_keys(date)

        # 定位到下拉列表
        select = Select(driver.find_element(By.NAME, "pjname"))
        select.select_by_visible_text(currency_name)

        # 定位到按钮元素
        button = (driver.find_element(By.XPATH, "//input[@onclick='executeSearch()']"))
        button.click()
    
        # 定位到现汇卖出价
        xpath = f"//tr[td[contains(text(), '{currency_name}')]]/td[4]"
        sell_price = driver.find_element(By.XPATH, xpath).text

    except FileNotFoundError:
        print("文件未找到")
        return None

    except Exception as e:
        print(f"出现错误: {e}")
        return None
    finally:
        # 关闭浏览器
        driver.quit()
        
    return sell_price

if __name__ == "__main__":
    # 处理命令行参数
    parser = argparse.ArgumentParser()
    parser.add_argument("date", help="日期，格式为YYYYMMDD")
    parser.add_argument("currency", help="货币代码，如 USD")
    args = parser.parse_args()

    # 获取现汇卖出价
    rate = get_exchange_rate(args.date, args.currency)

    with open("result.txt", "w") as f:
        f.write(rate)
    print(rate)