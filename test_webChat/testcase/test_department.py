from test_webChat.api.department import Department

class TestDapartment:
    def test_list(self):
        department = Department()
        r=department.list()
        print(r)
