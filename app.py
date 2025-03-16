# save this as app.py
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db=SQLAlchemy(app)

class Todo(db.Model):
    sno =db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(200),nullable=False)
    desc=db.Column(db.String(500),nullable=False)
    date_created=db.Column(db.DateTime,default=lambda:datetime.now(timezone.utc))

    def __repr__(self):
        return f"{self.sno} - {self.title}"
@app.route("/",methods=['GET','POST'])
def hello():
    if request.method=='POST':
        title=request.form["title"]
        desc=request.form["desc"]
        todo=Todo(title=title, desc=desc)
        db.session.add(todo)
        db.session.commit()

    search_query=request.args.get('search','')
    if search_query:
        allTodo=Todo.query.filter(
            (Todo.title.contains(search_query)) |(Todo.desc.contains(search_query))
        ).all()
    else:
        allTodo=Todo.query.all()
    
    print(allTodo)
    return render_template('index.html',allTodo=allTodo,search_query=search_query)
    
@app.route("/delete/<int:sno>")
def delete(sno):
    allTodo=Todo.query.filter_by(sno=sno).first()
    db.session.delete(allTodo)
    db.session.commit()
    return redirect("/")
@app.route("/update/<int:sno>",methods=['GET','POST'])
def update(sno):
    
    if request.method=='POST':
        title=request.form["title"]
        desc=request.form["desc"]
        todo=Todo.query.filter_by(sno=sno).first()
        todo.title=title
        todo.desc=desc
        db.session.add(todo)
        db.session.commit()
        return redirect("/")
    allTodo=Todo.query.filter_by(sno=sno).first()
    return render_template('update.html',allTodo=allTodo)

if __name__=="__main__":
    app.run(debug=True)