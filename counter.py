from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  
app.secret_key = 'keep it secret, keep it safe'


@app.route('/')
def index():
    if 'counter' in session:
        print('counter exists!')
        session['counter'] += 1
        times = 'times'
    else:
        print("session 'counter' does NOT exist")
        session['counter'] = 1
        times = 'time'
    return render_template("index.html", times=times)

@app.route('/destroy_session')
def destroy():
    print('Destroying Session!')
    session.clear()
    return redirect('/')




if __name__=="__main__":   
    app.run(debug=True)    

