from selenium.webdriver.common.by import By
class Register:

    # Поле ввода ИМЕНИ на странице https://stellarburgers.nomoreparties.site/register
    r_name_fild=(By.XPATH,".//label[text()='Имя']/parent::div/input")
    # Поле ввода EMAIL
    r_email_fild=(By.XPATH,".//label[text()='Email']/parent::div/input")
    # Поле ввода PASSWORD
    r_password_fild=(By.XPATH,".//input [@type='password']")
    #Кнопка ЗАРЕГИСТРИРОВАТЬСЯ на странице https://stellarburgers.nomoreparties.site/register
    r_registration_button=(By.XPATH,'//button[text()="Зарегистрироваться"]')
    # Кнопка ВОЙТИ на страницеhttps://stellarburgers.nomoreparties.site/register
    r_enter_button=(By.XPATH,'//a[@href="/login"]')
    # сообщение НЕККОРЕТ+КТНЫЙ ПАРОЛЬ на странице https://stellarburgers.nomoreparties.site/register
    r_error_password=(By.XPATH,'//p[text()="Некорректный пароль"]')
class Button:
    #Кнопка ОФОРМИТЬ ЗАКАЗ на главной странице после регистрации
    PLACE_ORDER=(By.XPATH,'//button[text()="Оформить заказ"]')
    #Кнопка ВОЙТИ на странице логин
    ENTER=(By.XPATH,'//button[text()="Войти"]')
    #Надпись ВХОД на странице логин
    LOGIN_TEXT=(By.XPATH, '//h2[text()="Вход"]')
    #Кнопка ЛИЧНЫЙ КАБИНЕТ в хедере
    PERSONAL_ACCOUNT=(By.XPATH,'//p[text()="Личный Кабинет"]')
    # Войти в аккаунт на главной странице
    ENTER_ACCOUNT=(By.XPATH,'.//button[text()="Войти в аккаунт"]')
    #Кнопка ЗАРЕГИСТРИРОВАТЬСЯ на странице логин
    ENTER_FROM_REGISTRAITE=(By.XPATH,'// a [@href="/register"]')
    # Кнопка ВОССТАНОВИТЬ ПАРОЛЬ на странице логин
    RECOVER_PASS=(By.XPATH,'// a[@href="/forgot-password"]')
    #Кнопка ВОССТАНОВИТЬ на странице https://stellarburgers.nomoreparties.site/forgot-password
    RECOVER_BUTTON=(By.XPATH,'// button[text()="Восстановить"]')
    # Кнопка ВОЙТИ на странице https://stellarburgers.nomoreparties.site/forgot-password
    ENTER_FROM_RECOVER=(By.XPATH,'//a[@href="/login"]')
    #Кнопка ПРОФИЛЬ на странице https://stellarburgers.nomoreparties.site/account/profile
    PROFIL=(By.XPATH,'//a[@href="/account/profile"]')
    # Кнопка КОНСТРУКТОР в хедере
    CONSTRUCTOR_BUTTON=(By.XPATH,'// p[text()="Конструктор"]')
    #Надпись СОБЕРИТЕ БУРГЕР на главной странице
    COLLECT_BREAD=(By.XPATH,'//h1[text()="Соберите бургер"]')
    #Кнопка ВЫХОД на странице https://stellarburgers.nomoreparties.site/account/profile
    BUTTON_EXIT=(By.XPATH,'// button[text()="Выход"]')
    #Кнопка СОУСЫ на главной странице
    SAUCE=(By.XPATH,'// span[text()="Соусы"]')
    # Кнопка НАЧИНКИ на главной странице
    FILLINGS=(By.XPATH,'// span[text()="Начинки"]')
    # Кнопка БУЛКИ на главной странице
    ROLLS=(By.XPATH,'//span[text()="Булки"]')
    # Надпись СОУСЫ на главной странице в зоне скролла
    SAUCE_SCROLL_TEXT=(By.XPATH,'// h2[2][text()="Соусы"]')
    # Надпись НАЧИНКИ на главной странице в зоне скролла
    FILLINGS_SCROLL_TEXT=(By.XPATH,'//h2[3][text()="Начинки"]')
    # Надпись БУЛКИ на главной странице в зоне скролла
    ROLLS_SCROLL_TEXT=(By.XPATH,'//h2[1][text()="Булки"]')
    #Кнопка РЕГИСТРАЦИЯ на станице https://stellarburgers.nomoreparties.site/login
    REGESTRATION_BUTTON=(By.XPATH,'// a[@href="/register"]')
