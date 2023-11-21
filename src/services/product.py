from src.models.product import Product


class ProductService:
    def create_product(db, product_data):
        db_product = Product(**product_data.model_dump())
        db.add(db_product)
        db.commit()
        db.refresh(db_product)
        return db_product

    def get_products(db):
        return db.query(Product).all()

    def get_product_by_id(db, product_id):
        return db.query(Product).filter(Product.id == product_id).first()

    def update_product(db, product_id, product_data):
        product_data = product_data.model_dump()
        db_product = db.query(Product).filter(Product.id == product_id).first()
        for key, value in product_data.items():
            setattr(db_product, key, value)
        db.commit()
        db.refresh(db_product)
        return db_product

    def delete_product(db, product_id):
        db_product = db.query(Product).filter(Product.id == product_id).first()
        db.delete(db_product)
        db.commit()
        return True
