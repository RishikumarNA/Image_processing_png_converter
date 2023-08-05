from imageai.Prediction import ImagePrediction
import os

execution_path=os.getcwd()
prediction= ImagePrediction()
prediction.setModelTypeAsInceptionV3()
prediction.setModelPath(os.path.join(execution_path,"inception_v3_google-1a9a5a14.pth"))
prediction.loadModel() 

predictions, probabilities = prediction.classifyImage(os.path.join(execution_path, "giraffe.jpg"), result_count=5 )
for eachPrediction, eachProbability in zip(predictions, probabilities):
    print(eachPrediction , " : " , eachProbability)