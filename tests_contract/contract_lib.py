from fixture.variables import UserLogin
from functools import wraps
from fixture.variables import Profinity
from sys import maxsize


def connection(fn):
    @wraps(fn)
    def wrapper(app):
        app.session.login(UserLogin.name, UserLogin.password)
        try:
            fn(app)
        finally:
            app.session.logout()

    return wrapper


class Contact:
    def __init__(self, first_name=None, middle_name=None, last_name=None, nickname=None, title=None, company_name=None,
                 address_name=None, home=None, mobile=None, work=None, fax=None, email1=None, email2=None, email3=None,
                 homepage=None, address=None, phone=None, notes=None, add_year=None, id=None, contact_name=None):

        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nickname = nickname
        self.title = title
        self.company_name = company_name
        self.address_name = address_name
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.address = address
        self.phone = phone
        self.notes = notes
        self.add_year = add_year
        self.contract_name = contact_name
        self.id = id

    def __repr__(self):
        return '%s:%s:%s' % (self.id, self.first_name, self.last_name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.first_name == other.first_name and \
                self.last_name == other.last_name

    def if_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize


class ContactBase():
    def __init__(self, app):
        self.app = app

    def count(self):
        wd = self.app.wd
        self.open_contract_page()
        return len(wd.find_elements_by_name("selected[]"))

    def open_contract_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith('addressbook/')): #and len(wd.find_elements_by_name('new')) > 0):
            wd.find_element_by_link_text("home").click()

    def validation_of_contact_exist(self):
        if self.count() == 0:
            self.create((Contact(first_name=Profinity.correct_data, last_name=Profinity.correct_data,
                        middle_name=Profinity.correct_data, nickname=Profinity.correct_data)))

    def edit_contract(self, Contract):
        wd = self.app.wd
        self.open_contract_page()

        wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()
        self.contract_field(Contract)
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        self.open_contract_page()

    def contract_field(self, Contact):
        wd = self.app.wd
        if Contact.first_name:
            wd.find_element_by_name("firstname").click()
            wd.find_element_by_name("firstname").clear()
            wd.find_element_by_name("firstname").send_keys("%s" % Contact.first_name)
        if Contact.middle_name:
            wd.find_element_by_name("middlename").click()
            wd.find_element_by_name("middlename").clear()
            wd.find_element_by_name("middlename").send_keys("%s" % Contact.middle_name)
        if Contact.last_name:
            wd.find_element_by_name("lastname").click()
            wd.find_element_by_name("lastname").clear()
            wd.find_element_by_name("lastname").send_keys("%s" % Contact.last_name)
        if Contact.nickname:
            wd.find_element_by_name("nickname").click()
            wd.find_element_by_name("nickname").clear()
            wd.find_element_by_name("nickname").send_keys("%s" % Contact.nickname)

        if Contact.title:
            wd.find_element_by_name("title").click()
            wd.find_element_by_name("title").clear()
            wd.find_element_by_name("title").send_keys("%s" % Contact.title)

        if Contact.company_name:
            wd.find_element_by_name("company").click()
            wd.find_element_by_name("company").clear()
            wd.find_element_by_name("company").send_keys("%s" % Contact.company_name)

        if Contact.address_name:
            wd.find_element_by_name("address").click()
            wd.find_element_by_name("address").clear()
            wd.find_element_by_name("address").send_keys("%s" % Contact.address_name)

        if Contact.home:
            wd.find_element_by_name("home").click()
            wd.find_element_by_name("home").clear()
            wd.find_element_by_name("home").send_keys("%s" % Contact.home)
        if Contact.mobile:
            wd.find_element_by_name("mobile").click()
            wd.find_element_by_name("mobile").clear()
            wd.find_element_by_name("mobile").send_keys("%s" % Contact.mobile)
        if Contact.work:
            wd.find_element_by_name("work").click()
            wd.find_element_by_name("work").clear()
            wd.find_element_by_name("work").send_keys("%s" % Contact.work)
        if Contact.fax:
            wd.find_element_by_name("fax").click()
            wd.find_element_by_name("fax").clear()
            wd.find_element_by_name("fax").send_keys("%s" % Contact.fax)

        if Contact.email1:
            wd.find_element_by_name("email").click()
            wd.find_element_by_name("email").click()
            wd.find_element_by_name("email").clear()
            wd.find_element_by_name("email").send_keys("%s" % Contact.email1)
        if Contact.email2:
            wd.find_element_by_name("email2").click()
            wd.find_element_by_name("email2").clear()
            wd.find_element_by_name("email2").send_keys("%s" % Contact.email2)
        if Contact.email3:
            wd.find_element_by_name("email3").click()
            wd.find_element_by_name("email3").clear()
            wd.find_element_by_name("email3").send_keys("%s" % Contact.email3)

        if Contact.homepage:
            wd.find_element_by_name("homepage").click()
            wd.find_element_by_name("homepage").clear()
            wd.find_element_by_name("homepage").send_keys("%s" % Contact.homepage)

        if Contact.add_year:
            # in futures we can made function where we will sent date and it choose it with similar way as previous
            if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[3]").is_selected():
                wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[3]").click()
            if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[2]").is_selected():
                wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[2]").click()
            wd.find_element_by_name("byear").click()
            wd.find_element_by_name("byear").clear()
            wd.find_element_by_name("byear").send_keys("1999")
            if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[3]").is_selected():
                wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[3]").click()
            if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[2]").is_selected():
                wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[2]").click()
            wd.find_element_by_name("ayear").click()
            wd.find_element_by_name("ayear").clear()
            wd.find_element_by_name("ayear").send_keys("1999")

        if Contact.address:
            wd.find_element_by_name("address2").click()
            wd.find_element_by_name("address2").clear()
            wd.find_element_by_name("address2").send_keys("%s" % Contact.address)

        if Contact.phone:
            wd.find_element_by_name("phone2").click()
            wd.find_element_by_name("phone2").clear()
            wd.find_element_by_name("phone2").send_keys("%s" % Contact.phone)

        if Contact.notes:
            wd.find_element_by_name("notes").click()
            wd.find_element_by_name("notes").clear()
            wd.find_element_by_name("notes").send_keys("%s" % Contact.notes)


    def create(self, Contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

        self.contract_field(Contact)

        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def delete_contract(self):
        wd = self.app.wd
        self.open_contract_page()

        if not wd.find_element_by_name("selected[]").is_selected():
            wd.find_element_by_name("selected[]").click()

        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()

    def get_contact_list(self):
        wd = self.app.wd
        self.open_contract_page()
        id_contact = []
        row = 2
        # this code does not work and i dont know how to deal with it
        '''
        for element in wd.find_elements_by_css_selector('tr'):

        for element in wd.find_elements_by_name('entry'):
            for element2 in element.find_elements_by_css_selector('td.center'):
                for element3 in element2.find_elements_by_xpath('//*[@id=maintable]'):
                    text = element.text
            id = element.find_element_by_name('selected[]').get_attribute('value')
                    id_contract.append(Contact(contact_name=text, id=id))



            id_contact.append(Contact(id=id))'''

        # in this case we have not name and lastname

        '''
        for element in wd.find_elements_by_xpath("//input[contains(@type,'checkbox')]"):
            text = element.text'''

        # so i cheated(((((
        for element in wd.find_elements_by_name("entry"):
            text = []
            for column in range(2, 4):
                text.append(wd.find_element_by_xpath("//*[@id='maintable']/tbody/tr["+str(row)+"]/td["+str(column)+"]").text)

            my_id = element.find_element_by_name("selected[]").get_attribute("value")

            id_contact.append(Contact(first_name=text[1], last_name=text[0], id=my_id))
            row += 1

        return id_contact
