from ext import app
from routes import productchoose, error, index, product_detail, products, productssee, delete_product, add_product, admin_dashboard, admin_register, admin_login, register, login
app.run(host="0.0.0.0",debug=True)
