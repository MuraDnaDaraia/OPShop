from functools import wraps
from flask import render_template, redirect, url_for, flash, request
from ext import db, app
from models import User, Product
from flask_login import login_user, logout_user, current_user, login_required
from forms import SignUpForm, LoginForm, RegistrationForm, AdminLoginForm, ProductForm

@app.route("/product", endpoint="Product_choose")
def productchoose():
    return render_template("parts.html")

@app.route("/error")
def error():
    return render_template("productshtml/other_detail.html")
@app.route("/")
def index():
    return render_template("index.html")

@app.route('/products/<int:id>', endpoint='product_detail')
@login_required
def product_detail(id):
    product = Product.query.get(id)
    if product is None:
        flash('Product not found.', 'danger')
        return redirect(url_for('products'))

    template_name = f'productshtml/{product.type.lower()}_detail.html'


    return render_template(template_name, product=product)


@app.route('/products/<type>')
def products(type):
    product = Product.query.filter_by(type=type).all()

    sort = request.args.get('sort')

    if sort == 'model_asc':
        product = sorted(product, key=lambda p: p.model)
    elif sort == 'model_desc':
        product = sorted(product, key=lambda p: p.model, reverse=True)
    elif sort == 'price_asc':
        product = sorted(product, key=lambda p: p.price)
    elif sort == 'price_desc':
        product = sorted(product, key=lambda p: p.price, reverse=True)

    if not product:
        flash(f"No Products in {type}", 'danger')

    return render_template('products.html', products=product, type=type, sort=sort)

@app.route('/products/')
def productssee():
    product = Product.query.all()
    sort = request.args.get('sort')

    if sort == 'model_asc':
        product = sorted(product, key=lambda p: p.model.lower())
    elif sort == 'model_desc':
        product = sorted(product, key=lambda p: p.model.lower(), reverse=True)
    elif sort == 'price_asc':
        product = sorted(product, key=lambda p: p.price)
    elif sort == 'price_desc':
        product = sorted(product, key=lambda p: p.price, reverse=True)

    return render_template('productsall.html', products=product)
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or current_user.role != "admin":
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/delete/<int:product_id>', methods=['POST'])
@login_required
@admin_required
def delete_product(product_id):
    product = Product.query.get(product_id)
    if product:
        db.session.delete(product)
        db.session.commit()
    return redirect(url_for('add_product'))


@app.route('/add_product', methods=['GET', 'POST'])
@admin_required
@login_required
def add_product():
    form = ProductForm()
    if form.validate_on_submit():
        product = Product(
            type=form.type.data,
            brand=form.brand.data,
            model=form.model.data,
            cores=form.cores.data,
            threads=form.threads.data,
            speed=form.speed.data,
            vram=form.vram.data,
            wattage=form.wattage.data,
            efficiency=form.efficiency.data,
            modularity=form.modularity.data,
            capacity=form.capacity.data,
            read_speed=form.read_speed.data,
            write_speed=form.write_speed.data,
            form_factor=form.form_factor.data,
            color=form.color.data,
            material=form.material.data,
            wifi=form.wifi.data,
            case_type=form.case_type.data,
            motherboard_type=form.motherboard_type.data,
            tdp=form.tdp.data,
            socket=form.socket.data,
            ram_slots=form.ram_slots.data,
            max_ram_capacity=form.max_ram_capacity.data,
            integrated_graphics=form.integrated_graphics.data,
            overclockable=form.overclockable.data,
            cooling_type=form.cooling_type.data,
            power_consumption=form.power_consumption.data,
            connector_types=form.connector_types.data,
            fan_size=form.fan_size.data,
            heat_spreader=form.heat_spreader.data,
            ecc_support=form.ecc_support.data,
            nand_type=form.nand_type.data,
            interface=form.interface.data,
            chipset=form.chipset.data,
            release_date=form.release_date.data,
            price=form.price.data,
            cpu=form.cpu.data,
            gpu=form.gpu.data,
            psu=form.psu.data,
            ram_type= form.ram_type.data,
            mb=form.mb.data,
            ssd=form.ssd.data,
            ram=form.ram.data,
            image_url=form.image_url.data,
        )
        db.session.add(product)
        db.session.commit()
        flash("Product Uploaded Successfully", "success")
    else:
        print("Error: Form validation failed. Errors:", form.errors)
    return render_template('productform.html', form=form)

@app.route('/admin/dashboard')
@admin_required
@login_required
def admin_dashboard():
    return render_template('admin_dashboard.html')

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect("/")

@app.route('/admin/register', methods=['GET', 'POST'])
def admin_register():
    form = RegistrationForm()
    if form.validate_on_submit():
        if form.secret_key.data != '420':
            flash('Invalid secret key! Admin registration failed.', 'danger')
            return redirect(url_for('admin_register'))
        else:
            admin = User(nickname=form.nickname.data, password=form.password.data, role='admin')
            admin.create()
            flash('Admin registered successfully!', 'success')
        return redirect(url_for('admin_login'))

    return render_template('admin_register.html', form=form)


@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    form = AdminLoginForm()
    if form.validate_on_submit():

        admin = User.query.filter_by(nickname=form.nickname.data).first()
        if admin and admin.check_password(form.password.data) and admin.role == 'admin':
            login_user(admin)
            print(current_user.is_authenticated)
            return redirect(url_for('admin_dashboard'))

        flash('Invalid credentials or access denied.', 'danger')
    return render_template('admin_login.html', form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = SignUpForm()
    if form.validate_on_submit():

        existing_user = User.query.filter_by(nickname=form.nickname.data).first()
        if existing_user:
            flash('Nickname already taken. Please choose another one.')
        else:
            new_user = User(nickname=form.nickname.data,
                            password=form.password.data,
                            role="user")
            new_user.create()
            flash('Sign up successful! You can now log in.')
            return redirect(url_for('login'))
    else:
        print("Form errors:", form.errors)
    return render_template("register.html", form=form)
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if current_user.is_authenticated:
        return render_template("index.html")
    if form.validate_on_submit():
        user = User.query.filter(User.nickname == form.nickname.data).first()
        if user != None and user.check_password(form.password.data):
            login_user(user)
    return render_template('login.html', form=form)