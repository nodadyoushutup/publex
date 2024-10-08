# library.py

from .config import db
from .model import Model
from .section import Section


class Library(Model):
    identifier = db.Column(db.String)
    mediaTagVersion = db.Column(db.String)
    title1 = db.Column(db.String)
    title2 = db.Column(db.String)
    key = db.Column(db.String)

    @classmethod
    def create(cls, _obj=None, **kwargs):
        # if obj:
        #     for section in obj.sections():
        #         if section.get("movie"):
        #             Section.create(section)
        return super().create(_obj=_obj, **kwargs)