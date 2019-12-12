from config import db, ma


class PointToMoneyModel(db.Model):
    __tablename__ = 'point_to_money'

    id = db.Column(db.Integer, primary_key=True, server_default=db.text("nextval('point_to_money_id_seq'::regclass)"))
    start_date = db.Column(db.Date, nullable=True)
    end_date = db.Column(db.Date, nullable=True)
    rate_to_money = db.Column(db.Float(53), nullable=True)

class PointToMoneySchema(ma.ModelSchema):
    class Meta:
        model = PointToMoneyModel
        sqla_session = db.session
        fields = (
            'id',
            'start_date',
            'end_date',
            'rate_to_money'
        )

    def make(self, data, **kwargs):
        return PointToMoneyModel(**data)