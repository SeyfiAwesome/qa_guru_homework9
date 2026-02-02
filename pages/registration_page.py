from selene.support.shared import browser
from selene import have, command
from pathlib import Path

import tests


def resource_path(file_name: str) -> str:
    return str(Path(__file__).parent.parent.joinpath('tests', 'resources', file_name).resolve())

class RegistrationPage:

    def __init__(self):
        pass

    def open(self):
        browser.open('https://demoqa.com/automation-practice-form')

    def fill_first_name(self, first_name):
        browser.element('#firstName').type(first_name)

    def fill_last_name(self, last_name):
        browser.element('#lastName').type(last_name)

    def fill_email(self, user_email):
        browser.element('#userEmail').type(user_email)

    def select_gender(self, gender):
        valid_genders = ['Male', 'Female', 'Other']
        if gender not in valid_genders:
            raise ValueError(f'Gender must be one of {valid_genders}')
        browser.all('[name=gender]').element_by(have.value(gender)).element('..').click()

    def fill_mobile_phone(self, mobile_phone):
        browser.element('#userNumber').type(mobile_phone)

    def fill_date_of_birth(self, month, year, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(''
                        f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
                        ).click()

    def select_subject(self, subject):
        valid_subjects = ['English', 'Maths', 'Accounting', 'Arts', 'Social Studies', 'Biology', 'Computer Science',
                          'Commerce', 'Economics']
        if subject not in valid_subjects:
            raise ValueError(f'Subject myst be one of {valid_subjects}')
        browser.element('#subjectsInput').type(subject).press_enter()

    def select_hobbie(self, value):
        valid_hobbies = ['Sports', 'Reading', 'Music']
        if value not in valid_hobbies:
            raise ValueError(f'Hobbie must be one of {valid_hobbies}')
        browser.all('.custom-checkbox').element_by(have.exact_text(value)).click()

    def path(file_name):
        return str(
            Path(tests.__file__).parent.joinpath(f'resources/{file_name}').absolute()
        )

    def upload_picture(self, file_name: str):
        browser.element('#uploadPicture').set_value(resource_path(file_name))
        return self

    def fill_current_address(self, user_address):
        browser.element('#currentAddress').type(user_address)

    def select_state(self, state):
        valid_states = ['NCR', 'Uttar Pradesh', 'Haryana', 'Rajastan']
        if state not in valid_states:
            raise ValueError(f'Hobbies must be one of {valid_states}')
        browser.element('#state').perform(command.js.scroll_into_view)
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(state)
        ).click()

    def select_city(self, city):
        valid_cities = ['Delhi', 'Gurgaon', 'Noida']
        if city not in valid_cities:
            raise ValueError(f'Cities must be one of {valid_cities}')
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(city)
        ).click()

    def click_submit_button(self):
        browser.element('#submit').perform(command.js.click)

    def should_registered_user_with(self, first_name, last_name, email, gender, phone, day_of_birth, month_of_birth, year_of_birth, subject, hobbies, attaches, address, state_and_city):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                f'{first_name} {last_name}',
                f'{email}',
                f'{gender}',
                f'{phone}',
                f'{day_of_birth} {month_of_birth},{year_of_birth}',
                f'{subject}',
                f'{hobbies}',
                f'{attaches}',
                f'{address}',
                f'{state_and_city}',
            )
        )