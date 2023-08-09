# from flask import Flask,render_template
# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello,'

# @app.route('/products')
# def products():
#     return 'this is product'



# if __name__=="__main__":
#     app.run(debug=True)

# from flask import Flask,render_template
# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return render_template("index.html")
#     # return 'Hello,World'

# @app.route('/products')
# def products():
#     return 'this is product'



# if __name__=="__main__":
#     app.run(debug=True)









# from flask import Flask
# app = Flask(__name__)

# @app.route('/hello/<name>')
# def hello_name(name):
#    return 'Hello %s!' % name

# if __name__ == '__main__':
#    app.run(debug = True)



# from flask import Flask, redirect, url_for, request
# app = Flask(__name__)

# @app.route('/success/<name>')
# def success(name):
#    return 'welcome %s' % name

# @app.route('/login',methods = ['POST', 'GET'])
# def login():
#    if request.method == 'POST':
#       user = request.form['nm']
#       return redirect(url_for('success',name = user))
#    else:
#       user = request.args.get('nm')
#       return redirect(url_for('success',name = user))

# if __name__ == '__main__':
#    app.run(debug = True)

from flask import Flask
app = Flask(__name__)

@app.route('/blog/<int:postID>')
def show_blog(postID):
    return 'Blog Number %d' % postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
    return 'Revision Number %f' % revNo
if __name__ == '__main__':
    app.run()