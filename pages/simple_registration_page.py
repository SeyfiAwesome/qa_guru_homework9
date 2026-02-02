from selene import browser, have


class SimpleUserRegistrationPage:
    def __init__(self):
        self.full_name_input = browser.element('#userName')
        self.email_input = browser.element('#userEmail')
        self.current_address_input = browser.element('#currentAddress')
        self.permanent_address_input = browser.element('#permanentAddress')
        self.submit_button = browser.element('#submit')

    def open(self):
        browser.open('https://demoqa.com/text-box')
        return self

    def fill_full_name(self, value):
        self.full_name_input.type(value)
        return self

    def fill_email(self, value):
        self.email_input.type(value)
        return self

    def fill_current_address(self, value):
        self.current_address_input.type(value)
        return self

    def fill_permanent_address(self, value):
        self.permanent_address_input.type(value)
        return self

    def submit(self):
        self.submit_button.click()
        return self

    def should_have_registered(self, name, email, current_address, permanent_address):
        output = browser.element('#output')
        output.should(have.text(name))
        output.should(have.text(email))
        output.should(have.text(current_address))
        output.should(have.text(permanent_address))
        return self
