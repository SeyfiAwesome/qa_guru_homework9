import tests
from os import path
from pathlib import Path
from selene.support.shared import browser
from selene import have, command
import time

def remove_banners():
    browser.driver.execute_script("""
        const fixedBan = document.getElementById('fixedban');
        if (fixedBan) fixedBan.remove();

        const footer = document.querySelector('footer');
        if (footer) footer.remove();
    """)



def test_student_registration_form():
    browser.open('https://demoqa.com/automation-practice-form')

    #WHEN
    browser.element('#firstName').type('Seyfi')
    browser.element('#lastName').type('Ismailov')
    browser.element('#userEmail').type('seyfullahismailly@gmail.com')

    browser.element("label[for='gender-radio-1']").click()

    browser.element('#userNumber').type('9219212121')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').type('August')
    browser.element('.react-datepicker__year-select').type('1993')
    browser.element(''
                    f'.react-datepicker__day--0{21}:not(.react-datepicker__day--outside-month)'
                    ).click()

    browser.element('#subjectsInput').type('English').press_enter()

    browser.all('.custom-checkbox').element_by(have.exact_text('Sports')).click()

    browser.element('#uploadPicture').set_value(
        str(Path(tests.__file__).parent.joinpath('resources/foto.jpg').absolute())
    )

    browser.element('#currentAddress').type("Ushinskogo street, 3")

    browser.element('#state').perform(command.js.scroll_into_view)
    browser.element('#state').click()
    browser.all('[id^=react-select][id*=option]').element_by(
        have.exact_text('NCR')
    ).click()

    browser.element('#city').click()
    browser.all('[id^=react-select][id*=option]').element_by(
        have.exact_text('Delhi')
    ).click()

    browser.element('#submit').perform(command.js.click)

    #THEN
    browser.element('.table').all('td').even.should(
        have.exact_texts(
            'Seyfi Ismailov',
            'seyfullahismailly@gmail.com',
            'Male',
            '9219212121',
            '21 August,1993',
            'English',
            'Sports',
            'foto.jpg',
            'Ushinskogo street, 3',
            'NCR Delhi'

        )
    )
    time.sleep(3)