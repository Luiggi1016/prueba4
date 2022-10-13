from flask import Flask, render_template
from modeloprediccion import prediccionresnet50
from flask import request
import forms
import base64
app= Flask(__name__)
foto=""
@app.route('/', methods=['GET'])
@app.route('/inicio', methods=['GET'])
def inicio():
    return render_template('index.html')
@app.route('/informacion', methods=['GET'])
def informacion():
    return render_template('about.html')
@app.route('/tomarfoto', methods=['GET','POST'])
def tomarfoto():
    comment_form = forms.CommentForm(request.form)
    if request.method=='POST':
        foto=comment_form.valor.data
        imagen=foto[22:]
        f = open ('linea.txt','w')
        f.write(imagen)
        f.close()
        decoded_data=base64.b64decode(imagen)
        img_file = open('image.jpeg', 'wb')
        img_file.write(decoded_data)
        img_file.close()
    datos=prediccionresnet50.prediccion().split("-")
    prediccion=datos[0]
    probabilidad=datos[1]
    return render_template('tomarfoto.html', predicc=prediccion,probab=probabilidad,form=comment_form)
if __name__ == '__main__':
    app.run(debug=True)

