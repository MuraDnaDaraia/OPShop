from wtforms.validators import Optional

from ext import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(32), unique=True, nullable=False)
    password = db.Column(db.String(400), nullable=False)
    role = db.Column(db.String(10), nullable=False, default="user")

    def __init__(self, nickname, password, role="user"):
        self.nickname = nickname
        self.password = generate_password_hash(password)
        self.role = role

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def create(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def save():
        db.session.commit()

    def __repr__(self):
        return f'<User {self.nickname}>'

class Product(db.Model):
    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)
    brand = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    cores = db.Column(db.String, nullable=True)
    threads = db.Column(db.String, nullable=True)
    speed = db.Column(db.String, nullable=True)
    vram = db.Column(db.String, nullable=True)
    wattage = db.Column(db.String, nullable=True)
    efficiency = db.Column(db.String(50), nullable=True)
    modularity = db.Column(db.String(50), nullable=True)
    ram_type = db.Column(db.String(50), nullable=True)
    warranty = db.Column(db.String, nullable=True)
    capacity = db.Column(db.String, nullable=True)
    read_speed = db.Column(db.String, nullable=True)
    write_speed = db.Column(db.String, nullable=True)
    form_factor = db.Column(db.String(50), nullable=True)
    color = db.Column(db.String(50), nullable=True)
    material = db.Column(db.String(50), nullable=True)
    socket = db.Column(db.String(50), nullable=True)
    ram_slots = db.Column(db.String, nullable=True)
    max_ram_capacity = db.Column(db.String, nullable=True)
    integrated_graphics = db.Column(db.Boolean, default=False)
    overclockable = db.Column(db.Boolean, default=False)
    wifi = db.Column(db.Boolean, default=False)
    cooling_type = db.Column(db.String(50), nullable=True)
    power_consumption = db.Column(db.String, nullable=True)
    connector_types = db.Column(db.String(50), nullable=True)
    fan_size = db.Column(db.String, nullable=True)
    heat_spreader = db.Column(db.Boolean, default=False)
    ecc_support = db.Column(db.Boolean, default=False)
    nand_type = db.Column(db.String(50), nullable=True)
    interface = db.Column(db.String(50), nullable=True)
    chipset = db.Column(db.String(50), nullable=True)
    release_date = db.Column(db.Date, nullable=True)
    case_type = db.Column(db.String(50), nullable=True)
    tdp = db.Column(db.String(50), nullable=True)
    motherboard_type = db.Column(db.String(50), nullable=True)
    cpu = db.Column(db.String(50), nullable=True)
    gpu = db.Column(db.String(50), nullable=True)
    psu = db.Column(db.String(50), nullable=True)
    mb = db.Column(db.String(50), nullable=True)
    ssd = db.Column(db.String(50), nullable=True)
    ram = db.Column(db.String(50), nullable=True)
    price = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(255), nullable=True)
    def __repr__(self):
        return f"<Product {self.brand} {self.model}>"
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))