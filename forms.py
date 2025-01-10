from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, BooleanField, DateField, SubmitField, PasswordField,  SelectField
from wtforms.validators import DataRequired, Optional, Length, EqualTo

class SignUpForm(FlaskForm):
    nickname = StringField('Nickname', validators=[DataRequired(), Length(min=2, max=80)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=200)])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    nickname = StringField('Nickname', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class RegistrationForm(FlaskForm):
    nickname = StringField('Nickname', validators=[DataRequired(), Length(min=3, max=50)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    secret_key = SelectField('Secret Key (only for admin)', choices=[(str(i), str(i)) for i in range(1001)])
    submit = SubmitField('Register')

class AdminLoginForm(FlaskForm):
    nickname = StringField('Nickname', validators=[DataRequired(), Length(min=3, max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    secret_key = StringField('Secret Key (only for admin)', validators=[Length(min=0, max=4)])
    submit = SubmitField('Login')


from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, DateField, SubmitField
from wtforms.validators import DataRequired, Optional



class ProductForm(FlaskForm):
    type = StringField('Type', validators=[DataRequired()])
    brand = StringField('Brand', validators=[DataRequired()])
    model = StringField('Model', validators=[DataRequired()])
    cores = StringField('Cores', validators=[Optional()])
    threads = StringField('Threads', validators=[Optional()])
    speed = StringField('Speed', validators=[Optional()])
    vram = StringField('VRAM', validators=[Optional()])
    wattage = StringField('Wattage', validators=[Optional()])
    efficiency = StringField('Efficiency', validators=[Optional()])
    modularity = StringField('Modularity', validators=[Optional()])
    capacity = StringField('Capacity', validators=[Optional()])
    read_speed = StringField('Read Speed', validators=[Optional()])
    write_speed = StringField('Write Speed', validators=[Optional()])
    form_factor = StringField('Form Factor', validators=[Optional()])
    color = StringField('Color', validators=[Optional()])
    tdp = StringField("TDP", validators=[Optional()])
    ram_type = StringField("Ram Type", validators=[Optional()])
    material = StringField('Material', validators=[Optional()])
    case_type = StringField('Case Type', validators=[Optional()])
    motherboard_type = StringField("Motherboard Type", validators=[Optional()])
    socket = StringField('Socket', validators=[Optional()])
    ram_slots = StringField('RAM Slots', validators=[Optional()])
    max_ram_capacity = StringField('Max RAM Capacity', validators=[Optional()])
    integrated_graphics = BooleanField('Integrated Graphics', validators=[Optional()])
    overclockable = BooleanField('Overclockable', validators=[Optional()])
    wifi = BooleanField('Wifi', validators=[Optional()])
    cooling_type = StringField('Cooling Type', validators=[Optional()])
    power_consumption = StringField('Power Consumption', validators=[Optional()])
    connector_types = StringField('Connector Types', validators=[Optional()])
    fan_size = StringField('Fan Size', validators=[Optional()])
    heat_spreader = BooleanField('Heat Spreader', validators=[Optional()])
    ecc_support = BooleanField('ECC Support', validators=[Optional()])
    nand_type = StringField('NAND Type', validators=[Optional()])
    interface = StringField('Interface', validators=[Optional()])
    chipset = StringField('Chipset', validators=[Optional()])
    release_date = DateField('Release Date', format='%Y-%m-%d', validators=[Optional()])
    cpu = StringField('CPU', validators=[Optional()])
    gpu = StringField('GPU', validators=[Optional()])
    psu = StringField('PSU', validators=[Optional()])
    case = StringField("case", validators=[Optional()])
    mb = StringField('mb', validators=[Optional()])
    ssd = StringField('SSD', validators=[Optional()])
    ram = StringField('RAM', validators=[Optional()])
    price = IntegerField('Price', validators=[Optional()])
    image_url = StringField('Image URL', validators=[Optional()])
    submit = SubmitField('Add Product')
