# 1.Cài đặt virtualenv:

  pip install virtualenv
  
Nếu bạn không thể chạy lệnh trên, thử chạy

  pip install -r requirements.txt
  
Điều này sẽ cài đặt các gói module cần thiết global trong máy thay vì cài đặt chúng vào môi trường ảo.

Nếu chưa có file requirements.txt thì hãy tạo và thêm vào file:

certifi==2020.6.20

chardet==3.0.4

click==7.1.2

cycler==0.10.0

Flask==1.1.2

gunicorn==20.0.4

idna==2.10

itsdangerous==1.1.0

Jinja2==2.11.3

joblib==0.16.0  

jsonify==0.5

kiwisolver==1.2.0

MarkupSafe==1.1.1

matplotlib 

mkl

numpy==1.18.5

pandas 

pyparsing==2.4.7

python-dateutil==2.8.1

pytz==2020.1

requests==2.24.0

scikit-learn==0.23.1

scipy 

seaborn==0.10.1

six==1.15.0

sklearn==0.0

threadpoolctl==2.1.0

tornado==6.0.4

urllib3==1.26.5

Werkzeug==1.0.1

wincertstore==0.2

Sau đó chạy lại lệnh

# 2. Tạo môi trường ảo:

virtualenv env

# 3. Kích hoạt môi trường ảo:
Windows:
    env\Scripts\activate
Linux/Mac:
    source env/bin/activate
# 4. Cài đặt các package cần thiết:
    pip install -r requirements.txt
# 5. Chạy server
    flask run
