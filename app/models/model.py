from flask_sqlalchemy import Model


class UtilModel(Model):

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
