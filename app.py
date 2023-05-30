from flask import Flask,render_template
FAI=Flask(__name__)
@FAI.route('/static_file')
def static_file():
    return render_template('static_file.html')
@FAI.route('/new')
def new():
    return render_template('new.html')

if __name__=='__main__':
    FAI.run(debug=True)