from config import db, ma

class MoneyToPointModel(db.Model):
    __tablename__ = 'money_to_point'

    id = db.Column(db.Integer, primary_key=True, server_default=db.text("nextval('money_to_point_id_seq'::regclass)"))
    start_date = db.Column(db.Date, nullable=True)
    end_date = db.Column(db.Date, nullable=True)
    rate_to_point = db.Column(db.Float(53), nullable=True)

class MoneyToPointSchema(ma.ModelSchema):
    class Meta:
        model = MoneyToPointModel
        sqla_session = db.session
        fields = (
            'id',
            'start_date',
            'end_date',
            'rate_to_point'
        )

    def make(self, data, **kwargs):
        return MoneyToPointModel(**data)