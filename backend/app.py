# flask: https://flask.palletsprojects.com/en/2.0.x/quickstart/#
from flask import Flask, jsonify, send_file, request, make_response
import sys
import base64
import psycopg2
from urllib.parse import quote
app = Flask(__name__)

def fetchdata(ID):
    conn = psycopg2.connect(database="trademark1", user="tm_root", password="roottm_9823a", host="trueint.lu.im.ntu.edu.tw", port="5433")
    cur = conn.cursor()
    cur.execute("SELECT doc,trademark_name,sdate,edate FROM trademark WHERE caseno = %s"%ID)
    main = cur.fetchall()
    cur.execute("SELECT bchinese FROM rca WHERE caseno = %s"%ID)
    rca = cur.fetchall()
    cur.execute("SELECT class FROM rcc WHERE caseno = %s"%ID)
    rcc = cur.fetchall()
    cur.execute("SELECT achinese,aenglish,address FROM rco WHERE caseno = %s"%ID)
    rco = cur.fetchall()
    cur.execute("SELECT filename FROM rcp WHERE caseno = %s"%ID)
    rcp = cur.fetchall()
    conn.close()

    [doc,trademark_name,sdate,edate] = main[0]
    [bchinese] = rca[0]
    [class_] = rcc[0]
    [achinese,aenglish,address] = rco[0]
    [filename] = rcp[0]   

    # print("doc: ", doc, file=sys.stdout)
    # print("filename: ", filename, file=sys.stdout)
    Path = '/service/trademark/raw_register_data/' + doc + "/" + filename
    # print("Path: ", Path, file=sys.stdout)
    res = make_response(send_file(Path, mimetype="image/jpeg"))
    res.headers['trademark_name'] = quote(trademark_name)
    res.headers['sdate'] = sdate
    res.headers['edate'] = edate
    res.headers['bchinese'] = quote(bchinese)
    res.headers['class_'] = class_
    res.headers['achinese'] = quote(achinese)
    res.headers['aenglish'] = aenglish
    res.headers['address'] = quote(address)

    # os.chdir('/service/trademark/raw_register_data')
    # img = mpimg.imread(Path)
    # imgplot = plt.imshow(img)
    # plt.show()

    return res




@app.route('/function1', methods=["GET"])
def function1():
    return jsonify({"Hello":"World"})

@app.route('/function2', methods=["GET"])
def function2():
    # print(request.args["caseno"], file=sys.stdout)
    res = fetchdata(request.args["caseno"])
    return res
    # return send_file("./rabbit.jpeg", mimetype="image/jpeg")
@app.route('/function3', methods=['POST'])
def function3():
    # print(request.method, file=sys.stdout)   
    print(request.form['name'], file=sys.stdout)   
    photo = request.form["file_attachment"]
    with open("/home/dragons/flask/backend/{}.png".format(request.form['name']), "wb") as f:
        img = base64.decodebytes(photo.encode('ascii'))
        f.write(img)    
    return jsonify({"status":1})



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8081, debug=True)