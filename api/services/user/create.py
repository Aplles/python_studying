import random
import string
from functools import lru_cache

from service_objects.services import ServiceWithResult

from models_app.models import User

LENGTH = 10


class UserCreateService(ServiceWithResult):

    def process(self):
        self._create_user()
        self.result = {
            'username': self._get_username,
            'password': self._get_password
        }
        return self

    def _create_user(self) -> User:
        return User.objects.create_user(
            username=self._get_username,
            password=self._get_password
        )

    @property
    @lru_cache()
    def _get_username(self):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(LENGTH))

    @property
    @lru_cache()
    def _get_password(self):
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(characters) for _ in range(LENGTH))
