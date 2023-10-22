from domain.requests.user import create, update
from .abstract_class.user_abstract import UserAbstractService
from repository.abstract_class.user_abstract import UserAbstractRepository


class UserService(UserAbstractService):
    def __init__(self, user_repository: UserAbstractRepository):
        self.user_repository = user_repository

    def get_all_users(self):
        """
        Mengambil semua entitas pengguna dalam penyimpanan.
        :return: Daftar entitas pengguna.
        """
        try:
            return self.user_repository.get_all()
        except Exception as e:
            raise e

    def get_user_by_email(self, email: str):
        """
        Mengambil entitas pengguna berdasarkan alamat email.
        :param email: Alamat email pengguna yang ingin diambil.
        :return: Entitas pengguna jika ditemukan, atau None jika tidak ada.
        """
        try:
            return self.user_repository.get_user_by_email(email)
        except Exception as e:
            raise e

    def create_user(self, firstname: str, lastname: str, email: str, password: str):
        """
        Membuat entitas pengguna baru dan menyimpannya dalam penyimpanan.
        :param request: Data permintaan untuk membuat pengguna baru.
        :return: Entitas pengguna yang baru dibuat.
        """
        try:
            user = create.CreateUserRequest(
                firstname=firstname,
                lastname=lastname,
                email=email,
                password=password,
            )

            return self.user_repository.create(request=user)
        except Exception as e:
            raise e

    def update_user(
        self,
        user_id: int,
        firstname: str,
        lastname: str,
        role: str,
        email: str,
        password: str,
    ):
        """
        Memperbarui entitas pengguna yang sudah ada dalam penyimpanan.
        :param request: Data permintaan untuk pembaruan pengguna.
        :return: Entitas pengguna yang sudah diperbarui.
        """
        try:
            user = update.UpdateUserRequest(
                id=user_id,
                firstname=firstname,
                lastname=lastname,
                email=email,
                role=role,
                password=password,
            )

            return self.user_repository.update(request=user)
        except Exception as e:
            raise e

    def delete_user(self, user_id: int):
        try:
            self.user_repository.delete(user_id)
        except Exception as e:
            raise e
