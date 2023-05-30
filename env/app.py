from flask import Flask, render_template

app=Flask(__name__, template_folder='Templates')

@app.route('/')
def main():
    return render_template('venta.html')

if __name__=='__main__':

  app.run(debug=True, port=5000)