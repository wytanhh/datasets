import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta

# Khởi tạo Faker
fake = Faker()

# Danh sách sản phẩm và giá
products = {
    'P001': {'name': 'Tinh Dầu Bio-Oil Skincare Oil (200ml)', 'price': 440000},
    'P002': {'name': 'Muối Tắm A Bonne Sữa Bò (350g)', 'price': 49000},
    'P003': {'name': "Kem Dưỡng Thể Tesori d'Oriente (300ml)", 'price': 279000},
    'P004': {'name': 'Nước Hoa Carolina Herrera Very Good Girl EDP (50ml)', 'price': 3000000},
    'P005': {'name': 'Sữa Tắm Trắng White Conc (360ml)', 'price': 350000},
    'P006': {'name': 'Nước Tẩy Trang Simple Water Boost Cấp Ẩm 400ml', 'price': 198000},
    'P007': {'name': 'Dầu Tẩy Trang Bioderma Sensibio Micellar Cleansing Oil 150ml', 'price': 565000},
    'P008': {'name': 'Dầu Tẩy Trang Cocoon Rose Cleansing Oil Chiết Xuất Hoa Hồng 140ml', 'price': 180000},
    'P009': {'name': 'Sáp Tẩy Trang Banila Co Clean It Zero Acerola+ Cleansing Balm Original 100ml (Hồng) New', 'price': 299000},
    'P010': {'name': 'Nước Tẩy Trang Loreal Revitalift Hyaluronic Acid Micellar Water Căng Mịn Da 400ml', 'price': 269000},
    'P011': {'name': 'Kem Lót Catrice The Vitamin C Fresh Glow Primer 30ml', 'price': 170000},
    'P012': {'name': 'Kem Lót Maybelline Baby Skin Pore Eraser 22ml', 'price': 208000},
    'P013': {'name': 'Kem Lót The Face Shop Air Cotton Makeup Base SPF30 PA++', 'price': 85500},
    'P014': {'name': 'Kem Nền Maybelline Fit Me Foundation Fresh Tint SPF50 Sáng Da, Chống Nắng 30ml', 'price': 228000},
    'P015': {'name': 'Kem Nền Estee Lauder Double Wear Lâu Trôi 30ml', 'price': 960000},
    'P016': {'name': 'Kem Nền CLIO Mini Kill Cover Founwear Foundation SPF30 PA+++', 'price': 229000},
    'P017': {'name': 'Kem Nền Focallure Fluid Foundation 30g', 'price': 60000},
    'P018': {'name': 'Che Khuyết Điểm The Saem Cover Perfection Tip Concealer SPF28/PA++ 6.5g', 'price': 75000},
    'P019': {'name': 'Che Khuyết Điểm Peripera Double Longwear Cover Concealer', 'price': 95000},
    'P020': {'name': 'Son Kem Peripera Ink Velvet', 'price': 148000},
    'P021': {'name': 'Son Kem 3CE Blur Water Tint Lì Mềm Mượt Môi 4.6g', 'price': 209000},
    'P022': {'name': 'Son Kem Romand Zero Velvet Tint 5.5g', 'price': 79500},
    'P023': {'name': 'Son Tint Espoir Couture Lip Tint Glaze', 'price': 295000},
    'P024': {'name': 'Son Kem Romand Blur Fudge Tint', 'price': 159000},
    'P025': {'name': 'Tẩy Tế Bào Chết Môi Cocoon Từ Cà Phê Đắk Lắk 5g', 'price': 79000},
    'P026': {'name': 'Kem Tắm Trắng Secret Key Snow White Milky Pack (200g)', 'price': 325000},
    
}

# Tạo danh sách giao dịch
data = []
start_date = datetime(2023, 1, 1)
end_date = datetime(2024, 6, 30)

while start_date <= end_date:
    num_transactions = random.randint(200, 300)
    for _ in range(num_transactions):
        invoice_id = fake.uuid4()
        purchase_date = start_date.strftime('%Y-%m-%d')
        customer_name = fake.name()
        phone_number = '0' + ''.join([str(random.randint(0, 9)) for _ in range(9)])
        product_code, product_info = random.choice(list(products.items()))
        product_name = product_info['name']
        unit_price = product_info['price']
        quantity = random.randint(1, 10)
        discount = random.uniform(0, 0.2)
        total_amount = quantity * unit_price * (1 - discount)
        payment_method = random.choice(['Tiền mặt', 'Thẻ tín dụng', 'Chuyển khoản'])
        
        data.append([invoice_id, purchase_date, customer_name, phone_number, product_code, product_name, quantity, unit_price, discount, total_amount, payment_method])
    
    start_date += timedelta(days=1)

# Tạo DataFrame và lưu vào file CSV
df = pd.DataFrame(data, columns=['Mã hóa đơn', 'Ngày mua', 'Tên khách hàng', 'Số điện thoại khách hàng', 'Mã sản phẩm', 'Tên sản phẩm', 'Số lượng', 'Đơn giá', 'Chiết khấu', 'Thành tiền', 'Phương thức thanh toán'])
df.to_csv('transactions.csv', index=False)
