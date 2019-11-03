import request

class Department:
    def list(self):
        pass

    def create(self):
        request.post(self, json={
            "name":name, "parentid":parentid, "order":order, id:""}),json()


    def update(self):
        pass

    def delete(self):
        pass