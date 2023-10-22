from domain.requests.cart.create import CartRequest

from .abstract_class.cart_abstract import CartServiceAbstract
from repository.abstract_class.cart_abstract import CartAbstractRepository


class CartService(CartServiceAbstract):
    def __init__(self, cart_repository: CartAbstractRepository):
        """
        Konstruktor untuk CartService.

        Args:
            cart_repository (CartAbstractRepository): Repository untuk mengakses data keranjang.
        """
        self.cart_repository = cart_repository

    def get_cart_items(self, user_id):
        """
        Dapatkan daftar item dalam keranjang untuk seorang pengguna.

        Args:
            user_id (int): ID pengguna yang akan mengambil item keranjangnya.

        Returns:
            List[Cart]: Daftar objek Cart yang mewakili item keranjang pengguna.
        """
        return self.cart_repository.find_all_by_user_id(user_id=user_id)

    def add_to_cart(
        self,
        name: str,
        price: str,
        image_product: str,
        quantity: int,
        product_id: int,
        user_id: int,
        weight: int,
    ):
        """
        Tambahkan item ke keranjang pengguna.

        Args:
            name (str): Nama produk.
            price (str): Harga produk.
            image_product (str): URL gambar produk.
            quantity (int): Jumlah item yang akan ditambahkan.
            product_id (int): ID produk yang akan ditambahkan ke keranjang.
            user_id (int): ID pengguna yang akan menambahkan item ke keranjang.
            weight (int): Berat produk.

        Returns:
            Cart: Objek Cart yang telah ditambahkan ke keranjang pengguna.
        """
        cart_item = CartRequest(
            name=name,
            price=price,
            image_product=image_product,
            quantity=quantity,
            product_id=product_id,
            user_id=user_id,
            weight=weight,
        )
        return self.cart_repository.create(cart_item=cart_item)

    def remove_from_cart(self, cart_id):
        """
        Hapus item dari keranjang pengguna berdasarkan ID item.

        Args:
            cart_id (int): ID item yang akan dihapus dari keranjang pengguna.

        Returns:
            bool: True jika penghapusan berhasil, False jika tidak.
        """
        return self.cart_repository.delete(cart_id=cart_id)

    def remove_items_from_cart(self, cart_ids):
        """
        Hapus beberapa item dari keranjang pengguna berdasarkan ID item.

        Args:
            cart_ids (List[int]): Daftar ID item yang akan dihapus dari keranjang pengguna.

        Returns:
            int: Jumlah item yang berhasil dihapus dari keranjang pengguna.
        """
        return self.cart_repository.delete_many(cart_ids=cart_ids)
