# 7.2 call centre
class Employee():

    def __init__(self):
        self.available = True
        self.call = None


class Respondent(Employee):

    def __init__(self):
        super().__init__()


class Manager(Employee):

    def __init__(self):
        super().__init__()


class Director(Employee):

    def __init__(self):
        super().__init__()


class Call:

    def __init__(self):
        self.handler = None


class NoHandler(Exception):
    pass


class NoEscalation(Exception):
    pass


class CallCentre:

    def __init__(self):
        self.respondents = []
        self.managers = []
        self.directors = []
        self.available_repondents = []
        self.available_managers = []
        self.available_directors = []
        self.active_calls = []

    def add_respondent(self):
        resp = Respondent()
        self.respondents.append(resp)
        self.available_respondents.append(resp)

    def add_manager(self):
        manager = Manager()
        self.managers.append(manager)
        self.available_managers.append(manager)

    def add_director(self):
        director = Director()
        self.directors.append(director)
        self.available_directors.append(director)

    def dispatch_call(self, call):
        if self.available_respondents:
            resp = self.available_respondents.pop()
            call.handler = resp
            resp.available = False
            resp.call = call
            self.active_calls.append(call)
        else:
            raise NoHandler("There is no respondent available")

    def escalate(self, call):
        old_handler = call.handler
        if old_handler.type() == Respondent:
            if self.available_managers:
                handler = self.available_managers.pop()
                call.handler = handler
                handler.available = False
                handler.call = call
                self.available_respondents.append(old_handler)
            else:
                raise NoHandler("There is no manager availbale")
        elif old_handler.type() == Manager:
            if self.available_directors:
                handler = self.available_directors.pop()
                call.handler = handler
                handler.available = False
                handler.call = call
                self.available_managers.append(old_handler)
            else:
                raise NoHandler("There is no director available")
        else:
            raise NoEscalation("The call cannot be escalated above the director level")
        old_handler.available = True
        old_handler.call = None

    def end_call(self, call):
        self.active_calls.remove(call)
        if call.handler.type() == Respondent:
            self.available_respondents.append(call.handler)
        elif call.handler.type() == Manager:
            self.available_managers.append(call.handler)
        else:
            self.available_directors.append(call.handler)
        call.handler.available = True
        call.handler.call = None
        call.handler = None

