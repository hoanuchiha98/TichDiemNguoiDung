from config import db, ma

class ProductModel(db.Model):
    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key=True, server_default=db.text("nextval('product_id_seq'::regclass)"))
    product_name = db.Column(db.String, nullable=False)
    product_price = db.Column(db.Float(53), nullable=False)

class ProductSchema(ma.ModelSchema):
    class Meta:
        model = ProductModel
        sqla_session = db.session
        fields = (
            'id',
            'product_name',
            'product_price'
        )

    def make(self, data, **kwargs):
        return ProductModel(**data)