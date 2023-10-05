from datetime import time


def test_dark_theme_by_time():
    current_time = time(hour=23)
    if time(hour=22) <= current_time or current_time < time(hour=6):
        is_dark_theme = True
    else:
        is_dark_theme = False
    assert is_dark_theme is True


def test_dark_theme_by_time_and_user_choice():

    current_time = time(hour=16)
    dark_theme_enabled_by_user = True
    if dark_theme_enabled_by_user is not None:
        is_dark_theme = dark_theme_enabled_by_user
    else:
        if time(hour=22) <= current_time or current_time < time(hour=6):
            is_dark_theme = True
        else:
            is_dark_theme = False
    assert is_dark_theme is True


def test_find_suitable_user():

    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]

    suitable_users = [i for i in users if i["name"] == "Olga"]
    suitable_users = suitable_users[0]
    assert suitable_users == {"name": "Olga", "age": 45}

    suitable_users = [i for i in users if i["age"] < 20]
    assert suitable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]

def print_function_info(func, **kwargs):
    func_name = func.__name__.replace("_", " ").title()
    args_str = ", ".join(f"{value}" for key, value in kwargs.items())
    print(f"{func_name} [{args_str}]")
    return f"{func_name} [{args_str}]"


def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")


def open_browser(browser_name):
    actual_result = print_function_info(open_browser, browser_name=browser_name)
    assert actual_result == "Open Browser [Chrome]"


def go_to_companyname_homepage(page_url):
    actual_result = print_function_info(go_to_companyname_homepage, page_url=page_url)
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"


def find_registration_button_on_login_page(page_url, button_text):
    actual_result = print_function_info(find_registration_button_on_login_page, page_url=page_url, button_text=button_text)
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"
