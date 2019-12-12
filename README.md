# Overview

## Database
- Database design
    - https://dbdiagram.io/d/5deb814aedf08a25543ed1b2

### Cài đặt && run
```
# create virtual env
virtualenv venv_name
# install python depedendcies
pip install -r requirements.txt

# create database from script
- copy and run script form file database/database-script.sql in postgresSQL
- Change string connection from database/db-connections.py

# run app
python server.py

# Port
http://127.0.0.1:5000/api/ui
```

## Link Tham khảo
- SQLAlchemy type
https://docs.sqlalchemy.org/en/13/core/type_basics.html

## Hướng dẫn khác

## Project Structure
### Cách hệ thống xử lý 1 request:
- __*Step 1: Validation*__ đầu vào - còn gọi là xác thực dữ liệu. Nếu dữ liệu fail thì không xử lý nữa
- __*Step 2: Processed*__ - xử lý dữ liệu và nghiệp vụ
- __*Step 3: Response*__ - xử lý dữ liệu đầu ra - để mapping đầu ra với frontend

### Cấu trúc thư mục chính

```bash
--/ common:
    --/ database:
        -- database_helper.py: Chứa các hàm xử lý chung từ database
    --/ enum:
    --/ log:
    --/ utils: chứa các hàm xử lý dùng chung
--/ controllers: lấy dữ liệu đầu vào => gọi tới service => xử lý dữ liệu đầu ra
     chứa các helper và các xử lý dữ liệu trong controller
 
--/ database: chứa các query khởi tạo và xử lý trên database
    -- db_connections: chứa chuỗi giá trị khởi tạo cho các database: postgrest

--/ models: models tương ứng với 
    --/ models_gen.py - file này chứa tất cả các models trong postgres

--/ services: - thao tác với database, update, create, delete, select.
   
--/ static: - chứa image và các file: relative path và absolute path

--/ swagger-doc - chứa mô tả cho swagger
    --/ main.yaml: cấu hình chính của swagger

config.py
    - config sqlalchemy
    - config flask

swagger_config.py
    - config swagger

server.py - cấu hình cho server
```
### Step 1: Validation dữ liệu
- Lý do: ngăn chặn các dữ liệu sida
- Implement: Cấu hình trong swagger. Có 2 điểm chú ý:
    - Khi truyền tham số trong __parameter__
    - Khai báo tham số trong __schema__

### Step 2: Processed
- Lý do: Tách riêng phần xử lý để có thể tái sử dụng code __re-use__
- Implement:
    - Trong __controllers__ không thực hiện trực tiếp việc xử lý trong database
    - __controller__ sẽ gọi các nhiệm vụ dính tới database như insert, update, delete, select thông qua __service__
    - __service__ vì chưa phải xử lý các nghiệp vụ phức tạp nên service sẽ đóng vai trò như __DAO__ là gọi tới database.
- __Xử lý với SQL__:
    - __Select__ thì gọi câu query nếu join nhiều bảng. Nếu có 1 bảng thì ta dùng luôn ORM
        - Khi select chú ý việc __phân trang__
        - __Total__ là total của tất cả bản ghi chứ không phải của 1 trang
    - __Create, update, delete__ thì thông qua ORM - vì thằng này nó xác thực dữ liệu một lần nữa. tránh cho việc dữ liệu không đúng
 
### Step 3: Response
- Lý do: để mapping với cả front-end
- Implement:
    - Trong __controller/common/utils/response_status_utils.py__ có chứa các hàm hỗ trợ việc xử lý đầu ra
    - __send_response__: response trả về 

### Step 4: Lưu ý khi code:
- Đã xác thực dữ liệu đầu vào chưa?
- Để xử lý với database thì phải gọi trong service?
- Response trả về đã đủ chưa - đã mapping với frontend chưa
- Phải ghi lại docstring: mô tả đầu vào, đầu ra scho các funtion
- Thêm thư viện đã thêm vào requirements.txt

## Step 5: Naming Convention - Quy ước đặt tên
- controller
    - tên file có hâu tố là controller: __user_controller.py__
    - tên hàm tương ứng tới các method trong swagger: 
    ```py
    def get():
    def get_by_id(user_id):
    def put(user_id):
    def post():
    def delete(user_id):
    ```
- service
    - tên file có hậu tố là service: __user_service.py__
- common
    - tên file có hậu tố là helper: __string_helper.py__

