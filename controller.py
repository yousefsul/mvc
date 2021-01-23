import view
from model import Product


def show_all_product():
    all_product_list = Product.get_all_product()
    return view.show_all_product(all_product_list)


def start():
    view.start_view()
    user_choice = input().lower()
    if user_choice == "y" or "yes":
        return show_all_product()
    else:
        view.end_view()


if __name__ == "__main__":
    start()
