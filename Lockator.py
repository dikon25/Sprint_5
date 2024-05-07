from selenium.webdriver.common.by import By
class Register:

    # Поле ввода ИМЕНИ на странице https://stellarburgers.nomoreparties.site/register
    r_name_fild=(By.XPATH,".//label[text()='Имя']/parent::div/input")
    # Поле ввода EMAIL
    r_email_fild=(By.XPATH,".//label[text()='Email']/parent::div/input")
    # Поле ввода PASSWORD
    r_password_fild=(By.XPATH,".//input [@type='password']")
    #Кнопка ЗАРЕГИСТРИРОВАТЬСЯ на странице https://stellarburgers.nomoreparties.site/register
    r_registration_button=(By.XPATH,'//*[@id="root"]/div/main/div/form/button[text()="Зарегистрироваться"]')
    # Кнопка ВОЙТИ на страницеhttps://stellarburgers.nomoreparties.site/register
    r_enter_button=(By.XPATH,'//*[@id="root"]/div/main/div/div/p/a')
    r_error_password=(By.XPATH,".//*[@id='root']/div/main/div/form/fieldset[3]/div/p")
class Button:
    #Войти в аккаунт на главной странице
    PLACE_ORDER=(By.XPATH,'.//*[@id="root"]/div/main/section[2]/div/button')
    #Кнопка ВОЙТИ на странице логин
    ENTER=(By.XPATH,'//*[@id="root"]/div/main/div/form/button[text()="Войти"]')
    #Надпись ВХОД на странице логин
    LOGIN_TEXT=(By.XPATH, '//*[@id="root"]/div/main/div/h2')
    #Кнопка ЛИЧНЫЙ КАБИНЕТ в хедере
    PERSONAL_ACCOUNT=(By.XPATH,'// *[ @ id = "root"] / div / header / nav / a / p')
    #Кнопка ОФОРМИТЬ ЗАКАЗ на главной странице после регистрации
    ENTER_ACCOUNT=(By.XPATH,'//*[@id="root"]/div/main/section[2]/div/button')
    #Кнопка ЗАРЕГИСТРИРОВАТЬСЯ на странице логин
    ENTER_FROM_REGISTRAITE=(By.XPATH,'// *[ @ id = "root"] / div / main / div / div / p / a')
    # Кнопка ВОССТАНОВИТЬ ПАРОЛЬ на странице логин
    RECOVER_PASS=(By.XPATH,'//*[@id="root"]/div/main/div/div/p[2]/a')
    #Кнопка ВОССТАНОВИТЬ на странице https://stellarburgers.nomoreparties.site/forgot-password
    RECOVER_BUTTON=(By.XPATH,'// *[ @ id = "root"] / div / main / div / form / button')
    # Кнопка ВОЙТИ на странице https://stellarburgers.nomoreparties.site/forgot-password
    ENTER_FROM_RECOVER=(By.XPATH,'//*[@id="root"]/div/main/div/div/p/a')
    #Кнопка ПРОФИЛЬ на странице https://stellarburgers.nomoreparties.site/account/profile
    PROFIL=(By.XPATH,'//*[@id="root"]/div/main/div/nav/ul/li[1]/a')
    # Кнопка КОНСТРУКТОР в хедере
    CONSTRUCTOR_BUTTON=(By.XPATH,'// *[ @ id = "root"] / div / header / nav / ul / li[1] / a / p')
    #Надпись СОБЕРИТЕ БУРГЕР на главной странице
    COLLECT_BREAD=(By.XPATH,'// *[ @ id = "root"] / div / main / section[1] / h1')
    #Кнопка ВЫХОД на странице https://stellarburgers.nomoreparties.site/account/profile
    BUTTON_EXIT=(By.XPATH,'// *[ @ id = "root"] / div / main / div / nav / ul / li[3] / button')
    #Кнопка СОУСЫ на главной странице
    SAUCE=(By.XPATH,'// *[ @ id = "root"] / div / main / section[1] / div[1] / div[2] / span')
    # Кнопка НАЧИНКИ на главной странице
    FILLINGS=(By.XPATH,'// *[ @ id = "root"] / div / main / section[1] / div[1] / div[3] / span')
    # Кнопка БУЛКИ на главной странице
    ROLLS=(By.XPATH,'// *[ @ id = "root"] / div / main / section[1] / div[1] / div[1] / span')
    # Надпись СОУСЫ на главной странице в зоне скролла
    SAUCE_SCROLL_TEXT=(By.XPATH,'// *[ @ id = "root"] / div / main / section[1] / div[2] / h2[2]')
    # Надпись НАЧИНКИ на главной странице в зоне скролла
    FILLINGS_SCROLL_TEXT=(By.XPATH,'//*[@id="root"]/div/main/section[1]/div[2]/h2[3]')
    # Надпись БУЛКИ на главной странице в зоне скролла
    ROLLS_SCROLL_TEXT=(By.XPATH,'//*[@id="root"]/div/main/section[1]/div[2]/h2[1]')
    #Кнопка РЕГИСТРАЦИЯ на станице https://stellarburgers.nomoreparties.site/login
    REGESTRATION_BUTTON=(By.XPATH,'// *[ @ id = "root"] / div / main / div / div / p[1] / a')
