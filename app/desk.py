from flask import redirect, request, url_for
from flask_admin.contrib.sqla import ModelView


class PanelView(ModelView):
    page_size = 20

    def inaccessible_callback(self, name, **kwargs):
        redirect(url_for("admin.login", next=request.url))
