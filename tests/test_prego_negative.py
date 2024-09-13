def test_empty_fields_authorization(final_project):
    final_project.open_url('https://prego.ua/')
    final_project.open_login_form()
    final_project.click_login_button()
    final_project.check_error_message_for_empty_phone_field("ПОЛЕ ОБОВ'ЯЗКОВЕ ДЛЯ ЗАПОВНЕННЯ")



def test_incorrect_email(final_project):
    final_project.open_url('https://prego.ua/uk/zhenskaya-obuv/botinki/botinki-na-kabluke/t_gu_bok_24_g182_3227_01')
    final_project.add_to_cart()
    final_project.view_cart()
    final_project.email('4444444444')
    final_project.check_error_message_email_field("АДРЕСА ЕЛЕКТРОННОЇ ПОШТИ НЕВІРНА")


