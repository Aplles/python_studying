from service_objects.services import ServiceWithResult

from models_app.models import User


class UserLoginService(ServiceWithResult):
    custom_validations = ['_login']

    def process(self):
        self.run_custom_validations()
        if self.is_valid():
            self.result = self._user
        return self

    @property
    def _user(self) -> User:
        return User.objects.get(username=self.data['username'])

    def _login(self):
        if not self._user.check_password(self.data['password']):
            self.error = 'Неверный логин или пароль'
