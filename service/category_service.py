from domain.requests.category import create, update
from .abstract_class.category_abstract import CategoryAbstractService
from repository.abstract_class.category_abstract import CategoryAbstractRepository


class CategoryService(CategoryAbstractService):
    def __init__(self, category_repository: CategoryAbstractRepository):
        self.category_repository = category_repository

    def get_all_categories(self):
        """
        Mengambil semua kategori yang tersedia.
        """
        return self.category_repository.get_all()

    def get_category_by_id(self, category_id: int):
        """
        Mengambil kategori berdasarkan ID.

        Parameters:
            category_id (int): ID kategori yang akan diambil.
        """
        return self.category_repository.get_by_id(category_id)

    def get_category_by_slug(self, slug: str):
        """
        Mengambil kategori berdasarkan ID.

        Parameters:
            slug (str): slug yang akan diambil.
        """
        category = self.category_repository.get_by_slug(slug=slug)

        response_category = {
            "category_id": category.category_id,
            "name_category": category.name_category,
            "slug_category": category.slug_category,
            "image_category": category.image_category,
            "products": category.products,
        }

        return response_category

    def create_category(self, name: str, file_path: str):
        """
        Membuat kategori baru.

        Parameters:
            name (str): Nama kategori yang akan dibuat.
            file_path (str): Path ke file gambar kategori.

        Returns:
            Category: Kategori yang baru saja dibuat.
        """
        category = create.CreateCategoryRequest(name=name, file_path=file_path)
        return self.category_repository.create(request=category)

    def update_category_by_id(self, category_id: int, name: str, file_path: str):
        """
        Memperbarui kategori yang sudah ada berdasarkan ID.

        Parameters:
            category_id (int): ID kategori yang akan diperbarui.
            name (str): Nama baru untuk kategori.
            file_path (str): Path ke file gambar yang akan digunakan untuk kategori.

        Returns:
            Category: Kategori yang sudah diperbarui.
        """
        category = update.UpdateCategoryRequest(
            id=category_id, name=name, file_path=file_path
        )
        return self.category_repository.update_by_id(updated_category=category)

    def delete_category_by_id(self, category_id: int):
        """
        Menghapus kategori berdasarkan ID.

        Parameters:
            category_id (int): ID kategori yang akan dihapus.
        """
        self.category_repository.delete_by_id(category_id)
