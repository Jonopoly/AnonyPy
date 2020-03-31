from faker import Faker

fake = Faker()
UniqueCompany = []
uniqueEmails = []


def fake_word_with_int(num):
    words = fake.random_int(1, 3)
    return f"{' '.join(fake.words(words))}_{str(fake.random_int(1000, 9999))}"


def slightly_more_unique_company(num):
    company = f"{fake.company()} {fake.company_suffix()}{fake.random_int(1, 9999)}"
    if company not in UniqueCompany:
        UniqueCompany.append(company)
        return company
    else:
        attempts = 0
        while company in UniqueCompany:
            company = (
                f"{fake.company()} {fake.company_suffix()}{fake.random_int(1, 9999)}"
            )
            attempts = attempts + 1
        UniqueCompany.append(company)
        print(f"Took {attempts}  attempts to generate unique email.")
        return company


def fake_sentence(num):
    words = fake.random_int(10, 50)
    return str(fake.sentence(words)).replace("'", "\\'")


def fake_comment(num):
    words = fake.random_int(1, 50)
    return str(fake.sentence(words)).replace("'", "\\'")


def fake_email_address(num):
    email = f"{fake.random_letter()}{fake.last_name()}{fake.random_int(1, 99999)}@anony-fake.py"
    if email not in uniqueEmails:
        uniqueEmails.append(email)
        return email
    else:
        attempts = 0
        while email in uniqueEmails:
            email = f"{fake.random_letter()}{fake.last_name()}{fake.random_int(1, 99999)}@anony-fake.py"
            attempts = attempts + 1
        uniqueEmails.append(email)
        print(f"Took {attempts}  attempts to generate unique email.")
        return email


def fake_phone_number(num):
    chance = fake.random_int(1, 2)
    if chance == 1:
        return f"0{fake.random_int(100, 999)} {fake.random_int(100, 999)} {fake.random_int(1000, 9999)}"
    else:
        return f"+{fake.random_int(10, 99)}({fake.random_int(0, 20)}) {fake.random_int(1000, 9999)} {fake.random_int(1000, 9999)} "


def fake_password(num):
    return "{}==".format(
        fake.password(
            length=25,
            special_chars=False,
            digits=True,
            upper_case=True,
            lower_case=True,
        )
    )


def fake_html_answer(num):
    words = fake.random_int(1, 50)
    return "<p>{}</p>".format(str(fake.sentence(words)))


def fake_job(num):
    return fake.job()


def fake_name(num):
    return fake.name()


def fake_first_name(num):
    return fake.first_name()


def fake_last_name(num):
    return fake.last_name()


def fake_country(num):
    return fake.country()


def fake_words_replace(num):
    return " ".join(fake.words(num)).replace("'", "\\'")


def fake_street_address(num):
    return fake.street_address()


def fake_us_postcode(num):
    return fake.postcode()


fake_map = {
    "fake_name": fake_name,
    "fake_email": fake_email_address,
    "fake_phone_number": fake_phone_number,
    "fake_first_name": fake_first_name,
    "fake_last_name": fake_last_name,
    "fake_location": fake_country,
    "fake_job": fake_job,
    "fake_company_name": slightly_more_unique_company,
    "fake_random_words": fake_word_with_int,
    "fake_paragraph": fake_sentence,
    "fake_comment": fake_comment,
    "fake_password": fake_password,
    "fake_html_answer": fake_html_answer,
    "fake_words_replace": fake_words_replace,
    "fake_street": fake_street_address,
    "fake_us_postcode": fake_us_postcode,
}
