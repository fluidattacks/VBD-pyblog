from flask_login import current_user

from .desk import PanelView


class UserAdmin(PanelView):
    can_delete = False

    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin()
