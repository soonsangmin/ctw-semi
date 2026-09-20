from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# 1. Route hiển thị trang chủ (Giao diện Frontend)
@app.route("/")
def home():
    return render_template("index.html")

# 2. Route Backend nhận dữ liệu từ form "SoC Builder" hoặc "Contact Us"
@app.route("/submit-request", methods=["POST"])
def submit_request():
    # Lấy dữ liệu do khách hàng nhập từ Frontend gửi lên
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")
    
    # Bạn có thể xử lý lưu vào Database, gửi email thông báo, hoặc in ra terminal để kiểm tra
    print(f"Nhận yêu cầu mới từ: {name} ({email}) - Nội dung: {message}")
    
    # Trả về phản hồi cho phía Frontend
    return jsonify({
        "status": "success", 
        "message": f"Cảm ơn {name}, yêu cầu của bạn đã được gửi thành công đến CTW Semi!"
    })

if __name__ == "__main__":
    # Chạy server ở cổng 5000 (truy cập: http://127.0.0.1:5000)
    app.run(debug=True, port=5000)