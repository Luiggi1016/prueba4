
from fastai.vision.all import load_learner,PILImage
from fastai.vision.widgets import widgets
from pathlib import Path

import pathlib
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

def prediccion():
    learn_inf = load_learner('modeloprediccion/resnet50_modelo.pkl')
    lbl_pred = widgets.Label()


    lbl_pred.value = ''
    img = PILImage.create('image.jpeg')
    #out_pl.clear_output()
    #with out_pl: display(img.to_thumb(224,224))
    pred,pred_idx,probs = learn_inf.predict(img)
    lbl_pred.value = f'Predicción: {pred}; Probabilidad: {probs[pred_idx]:.04f}'

    #btn_run = widgets.Button(description='Clasificar')

    predic=pred
    prob=(float)(f'{probs[pred_idx]:.04f}')*100
    probabil=str(prob)+" %"
    mezcla=predic+"-"+probabil
    return mezcla
