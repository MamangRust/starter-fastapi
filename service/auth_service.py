from .abstract_class.auth_abstract import AuthAbstractService
from repository.abstract_class.user_abstract import UserAbstractRepository
from domain.requests.user.create import CreateUserRequest
from database.models.user import User


class AuthService(AuthAbstractService):
    def __init__(self, user_repository: UserAbstractRepository) -> None:
        self.user_repository = user_repository

    def register_user(self, firstname, lastname, email, password) -> User:
        """
        Mendaftarkan pengguna baru.

        Args:
            firstname (str): Nama depan pengguna yang akan didaftarkan.
            lastname (str): Nama belakang pengguna yang akan didaftarkan.
            email (str): Alamat surel pengguna.
            password (str): Kata sandi pengguna.


        Returns:
            User: Objek pengguna yang telah didaftarkan.
        """
        user = CreateUserRequest(
            firstname=firstname,
            lastname=lastname,
            email=email,
            password=password,
        )

        return self.user_repository.create(request=user)

    def login_user(self, email) -> User:
        """
        Melakukan proses masuk (login) pengguna.

        Args:
            email (str): Alamat surel pengguna.

        Returns:
            User: Objek pengguna yang berhasil masuk, atau None jika gagal.
        """
        user = self.user_repository.get_user_by_email(email=email)

        return user
