from pages.application_manager import ApplicationManager


def test_simple_registration_form():
    app = ApplicationManager()

    app.left_panel.open_simple_registration_form()

    app.left_panel.simple_registration_page \
        .fill_full_name("Seyfi Ismailov") \
        .fill_email("seyfullahismailly@gmail.com") \
        .fill_current_address("Ushinskogo street, 3") \
        .fill_permanent_address("Ushinskogo street, 3") \
        .submit()

    app.left_panel.simple_registration_page.should_have_registered(
        "Seyfi Ismailov",
        "seyfullahismailly@gmail.com",
        "Ushinskogo street, 3",
        "Ushinskogo street, 3"
    )