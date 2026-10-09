import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello Python!</h1><p>سایت پایتونی شما با موفقیت روی Runflare اجرا شد.</p>'


if __name__ == '__main__':
    # دریافت پورت از متغیرهای محیطی سیستم
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port)
