from pages.registration_page import RegistrationPage


def test_student_registration_form():
    registration_page = RegistrationPage()
    registration_page.open()

    # WHEN
    registration_page.fill_first_name('Seyfi')

    registration_page.fill_last_name('Ismailov')

    registration_page.fill_email('seyfullahismailly@gmail.com')

    registration_page.select_gender('Male')

    registration_page.fill_mobile_phone('9219212121')

    registration_page.fill_date_of_birth('August', "1993", "21")

    registration_page.select_subject('English')

    registration_page.select_hobbie('Sports')

    registration_page.upload_picture('foto.jpg')

    registration_page.fill_current_address('Ushinskogo street, 3')

    registration_page.select_state('NCR')

    registration_page.select_city('Delhi')

    registration_page.click_submit_button()

    registration_page.should_registered_user_with(
        'Seyfi',
        'Ismailov',
        'seyfullahismailly@gmail.com',
        'Male',
        '9219212121',
        '21',
        'August',
        '1993',
        'English',
        'Sports',
        'foto.jpg',
        'Ushinskogo street, 3',
        'NCR Delhi'
    )
