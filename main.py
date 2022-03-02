from flask import *
import json
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/view")
def view():
    con = sqlite3.connect("School.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from School")
    rows = cur.fetchall()
    return json.dumps([dict(ix) for ix in rows])

@app.route("/savedetails/", methods=["POST"])
def saveDetails():
    msg = "msg"
    try:
        data = request.get_json(force=True)
        print(data)
        nev = data["nev"]
        suly = data["suly"]
        nem = data["nem"]
        magassag = data["magassag"]
        with sqlite3.connect("School.db") as con:
            cur = con.cursor()
            cur.execute("INSERT into School (nev, suly, nem, magassag) values (?,?,?,?)", (nev, suly, nem, magassag))
            con.commit()
            msg = "School successfully Added"
    except:
        con.rollback()
        msg = "We can not add the employee to the list"
    finally:
        return nev
        con.close()

@app.route("/deleterecord/", methods=["POST"])
def deleterecord():
    data = request.get_json(force=True)
    id = str(data["id"])
    print(id)
    with sqlite3.connect("School.db") as con:
        try:
            cur = con.cursor()
            cur.execute("delete from School where id = ?", id)
            msg = "record successfully deleted"
        except:
            msg = "can't be deleted"

@app.route("/updatedetails/", methods=["POST"])
def updaterecord():
    try:
        data = request.get_json(force=True)
        print(data)
        id = data["id"]
        nev = data["nev"]
        suly = data["suly"]
        nem = data["nem"]
        magassag = data["magassag"]

        with sqlite3.connect("School.db") as con:
            cur = con.cursor()
            cur.execute("UPDATE School SET nev=?, suly=?, nem=? WHERE id=?", (nev, suly, nem, id))
            con.commit()
            msg = "School successfully Updated"
    except:
        con.rollback()
        msg = "We can not update the employee to the list"
    finally:
        return msg
        con.close()
if __name__ == "__main__":
    app.run(debug=True)