""" Page Service Section """

from app.main import db
from app.main.model.page import AboutPage
from app.main.util.response import Response
from werkzeug.exceptions import Forbidden


class PageService(object):
    """ Page Service Class """

    @staticmethod
    def save_page(data):
        """ Save Page """
        page = AboutPage(**data)
        db.session.add(page)
        db.session.commit()
        res = Response('Success').__dict__
        return res, 200

    @staticmethod
    def get_page():
        """ Getting Page """
        raise Forbidden
        pages = AboutPage.query.all()
        res = Response('Success', data=pages, message='List of Pages').__dict__
        return res, 200
