import ktrain
from ktrain import text

from flask  import Flask ,jsonify ,request ,render_template


#test_text = "سئ جدا هدا الفيلم "

model_path=r"C:\Users\rehab\OneDrive\Desktop\arabic_sentiment_analysis\arabic_bert"

loaded_model = ktrain.load_predictor(model_path)

#sentiment=loaded_model.predict(test_text)

#print(sentiment)

app=Flask(__name__)


@app.route('/')
def main():
    return render_template("index.html")
    
    
@app.route('/predict',methods=['POST'])
def predict():
    if request.method == "POST":
        message = request.form['submission']
        classification=loaded_model.predict(message)
        print(classification)
        
        

        return render_template('index.html', message=message, classification=classification)
    


if __name__ == '__main__':
    app.run(debug=True)