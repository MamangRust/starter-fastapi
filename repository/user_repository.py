from typing import List, Optional
from sqlalchemy.orm import Session
from repository.abstract_class.user_abstract import UserAbstractRepository
from database.models.user import User
from domain.requests.user import create, update
from core.hashing import Hashing


class UserRepository(UserAbstractRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> List[User]:
        """
        Mengambil semua entitas pengguna dalam penyimpanan.
        """
        try:
            return self.session.query(User).all()
        except Exception as e:
            raise e

    def get_user_by_email(self, email: str) -> User | None:
        """
        Mengambil entitas pengguna berdasarkan alamat email.

        Parameters:
            email (str): Alamat email pengguna yang akan diambil.
        """
        try:
            user = self.session.query(User).filter_by(email=email).first()

            return user
        except Exception as e:
            raise e

    def get_by_id(self, user_id: int):
        """
        Mengambil entitas pengguna berdasarkan ID.

        Parameters:
            user_id (int): ID pengguna yang akan diambil.
        """
        try:
            return self.session.query(User).filter_by(user_id=user_id).first()
        except Exception as e:
            raise e

    def create(self, request: create.CreateUserRequest):
        """
        Membuat entitas pengguna baru dan menyimpannya dalam penyimpanan.

        Parameters:
            request (CreateUserRequest): Data yang digunakan untuk membuat pengguna baru.
        """
        try:
            db_user = User(
                firstname=request.firstname,
                lastname=request.lastname,
                email=request.email,
                password=Hashing.bcrypt(request.password),
            )
            self.session.add(db_user)
            self.session.commit()
            self.session.refresh(db_user)

            db_user.password = None

            return db_user
        except Exception as e:
            raise e

    def update(self, request: update.UpdateUserRequest):
        """
        Memperbarui entitas pengguna yang sudah ada dalam penyimpanan.

        Parameters:
            request (UpdateUserRequest): Data yang digunakan untuk memperbarui pengguna yang ada.
        """
        try:
            db_user = self.get_by_id(request.id)

            db_user.firstname = request.firstname
            db_user.lastname = request.lastname
            db_user.email = request.email
            db_user.password = Hashing.bcrypt(request.password)
            db_user.role = request.role

            self.session.refresh(db_user)

            db_user.password = None

            return db_user
        except Exception as e:
            raise e

    def delete(self, user_id: int):
        """
        Menghapus entitas pengguna dari penyimpanan.

        Parameters:
            user_id (int): ID pengguna yang akan dihapus.
        """
        try:
            db_userid = self.session.query(User).filter_by(user_id=user_id).first()

            self.session.delete(db_userid)
            self.session.commit()
        except Exception as e:
            raise e
