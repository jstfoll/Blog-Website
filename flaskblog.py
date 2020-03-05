from flask import Flask, render_template
app = Flask(__name__)

posts=[
    {
        'SoftwareEngineering':'Module 1','CO':'Module 1'
        
    },
    {
        'SoftwareEngineering':'Module 322','CO':'Module 2'
        
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',posts=posts)

@app.route('/about')
def hell():
    return render_template('about.html',title=)


if __name__ == "__main__":
    app.run(debug=True)
