from django.shortcuts import render
from django.http import HttpResponse
from .forms import ImageForm, ImageView
import PIL
from PIL import Image
import numpy as np
import io
import tensorflow as tf
from modelo_red_predict_numbers import settings

# Create your views here.
def hello1(request):
    return render(request, 'index.html')

def hello(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        formView = ImageView()
        if form.is_valid():
            # Procesar la imagen aquí
            image = form.cleaned_data['image_upload']
            formView.fields['image_view'].initial = image
            
            stream = io.BytesIO(image.read())
            result = ""
            img = np.asarray(Image.open(stream))
            img = img / 255.0 * 100
            img_final = np.reshape(img * 100, (1, 784))
            model = tf.keras.models.load_model(settings.H5_FILE_PATH)
            y_predicted = model.predict(img_final)
            result += str(np.argmax(y_predicted[0]))
            
            # Hacer algo con la imagen, como guardarla o manipularla
            print(result)
            return render(request, 'index.html', {'form': form, 'resultado': result})
    else:
        form = ImageForm()
    
    return render(request, 'index.html', {'form': form})
