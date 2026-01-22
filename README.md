# Playwright_Testautomation

öncelikle bir pytest.ini dosyasi yapiyoruz proje kökunde.
# pytest.ini
[pytest]
#run chromium with UI
addopts = --headed --browser chromium --slowmo 2000

Burada chromium seçtiğimiz için test chrome de sürülür. Safari yazarsak safaride sürülür.

# kurulum aşamaları
#To install (not part of pytest.ini):
#To instal 'Playwright' 
#pip install playwright

# install browser which is used by Playwright
#Playwright install

# test klasşrü içinde 
#import pytest
#from playwright.sync_api import Page, expect, Playwright


