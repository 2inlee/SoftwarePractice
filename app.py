from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # 사용자 입력 처리
        user_input = request.form['user_input']
        # 여기서 user_input을 처리하고 결과를 얻습니다.
        result = process_input(user_input)
        return render_template('result.html', result=result)
    return render_template('index.html')

def process_input(user_input):
    # 여기에 사용자 입력을 처리하는 로직을 작성합니다.
    # 예시로 사용자 입력을 그대로 반환합니다.
    return user_input

if __name__ == '__main__':
    app.run(debug=True, port=5001)
