from .models import Menu, MenuImage


def get_menu_info(request, pk):

    menu = Menu.objects.filter(id=pk).first()
    menu_image_list = MenuImage.objects.filter(menu_id=pk).all()

    menu_info = {
        "menu": menu,
        "imageList": menu_image_list,
    }

    return menu_info
