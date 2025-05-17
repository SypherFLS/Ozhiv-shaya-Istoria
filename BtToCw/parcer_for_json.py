from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json

# Количество итераций
ITERATIONS = 500

def main():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  
    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 10)  
    driver.get("https://www.may9.ru/our-victory/letters/")

    data = {}

    for i in range(ITERATIONS):
        try:
            if (i+2)%6 == 0:
                load_button = wait.until(
                    EC.element_to_be_clickable((By.ID, "btn_load_more"))
                )
                load_button.click()
                
            element = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, f"#body > div.page-content > div:nth-child(2) > div > div:nth-child(3) > div:nth-child({i+1}) > div"))
            )                                                        
            try:                                                
                element.click()

                try:
                    modal_body = wait.until(
                        EC.visibility_of_element_located((By.ID, "letterTextBlock"))
                    )
                
                    try:
                        text = modal_body.text.strip()

                        data[i+1] = text 

                        try:
                            close_button = wait.until(
                                EC.element_to_be_clickable((By.CLASS_NAME, "close"))
                            )
                            close_button.click()
                            driver.execute_script("window.scrollBy(0, 180)") 
                            print(f"иттерация {i} пройдена")
                        except Exception:
                            print(f"Не найдена кнопка закрытия окна {i+1}")
                            break
                    except Exception:
                        print(f"Ошибка считывания текста {i+1}")
                        break
                except Exception:
                    print(f"Ошибка открытия окна {i+1}")
                    break
            except Exception:
                time.sleep(25)
                print(f"Ошибка открытия элемента {i+1}")
                break
            
        except Exception as e:
            print(f"Элемент не найден {i+1}: {e}")
            break
    
    # for i in range(len(data)):
    #     with open('training_data.json', 'w', encoding='utf-8') as file:
    #         json.dump(data[i], file, ensure_ascii=False, indent=4)
    #     print(f"добавлен элемент {i+1}")

    

    with open('training_data.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    driver.quit()

if __name__ == "__main__":
    main()