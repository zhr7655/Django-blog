from flask import Flask, render_template, request, redirect, url_for
from flask import jsonify
import json
import os

app = Flask(__name__)
DATA_FILE = "grades.json"

"""把文件内容加载出来"""
def load_grades():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE,"r",encoding = "utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

"""保存内容到文件内"""
def save_grade(grades):
    try:
        with open(DATA_FILE,"w",encoding="utf-8") as f:
            json.dump(grades,f,ensure_ascii=False,indent=2)
    except OSError as e:
        print(f"保存文件失败:{e}")

@app.route("/")
def index():
    grades = load_grades()

    avg = None
    if grades:
        avg = sum(s["成绩"] for s in grades) / len(grades)

    top = top_grade(grades)
    min = lowest_grade(grades)

    return render_template("index.html",grades = grades,avg = avg,top=top,min=min)

@app.route("/add",methods = ["POST"])
def add():
    student = request.form.get("name","").strip()
    grade_str = request.form.get("score","").strip()

    if not student or not grade_str:
        return redirect(url_for("index"))

    try:
        grade = float(grade_str)
        if not (0 <= grade <= 100):
            return redirect(url_for("index"))
    except ValueError:
            return redirect(url_for("index"))

    grades = load_grades()
    grades.append({"姓名":student,"成绩":grade})
    save_grade(grades)
    return redirect(url_for("index"))

@app.route("/delete/<name>")
def delete(name):
    grades = load_grades()
    new_grades = [s for s in grades if s["姓名"] != name]
    save_grade(new_grades)
    return redirect(url_for("index"))

@app.route("/update/<name>",methods=["POST"])
def update(name):
    grades = load_grades()
    s = find_student(grades,name)
    if s is None:
        return jsonify({"success":False,"message":"学生不存在"})
    data = request.get_json()
    if not data or "score" not in data:
        return jsonify({"success":False,"message":"成绩不存在"})
    
    try:
        new_data = float(data["score"])
        if not (0 <= new_data <= 100):
            raise ValueError
    except ValueError:
        return jsonify({"success":False,"message":"成绩必须在0-100之间"})

    s["成绩"] = new_data
    save_grade(grades)

    return jsonify({"success":True,"message":"修改成功","new_score":new_data})


def find_student():
    for i,s in enumerate(grades):
        if s["姓名"] == student:
            return jsonify('success':True,"message":'查找成功')
    return None

def top_grade(grades):
    if len(grades) == 0:
        return 0
    t = max(s["成绩"] for s in grades)
    return t


def lowest_grade(grades):
    if len(grades) == 0:
        return 0
    m = min(s["成绩"] for s in grades)
    return m

if __name__ == "__main__":
    app.run(debug=True)
