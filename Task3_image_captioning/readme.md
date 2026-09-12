# Task 3 - image captioning AI

## Description
this project combines computer vision and natural language processing to 
generate descriptive captions for images it uses the pretrained BLIP 
Bootstrapping Language-Image Pretraining model which internally uses a 
vision transformer to extract image features and a language decoder to 
generate natural language captions

## Technologies Used
Python 3
Hugging Face Transformers
PyTorch
BLIP (pretrained Vision-Language model)
PIL (image handling)

## How to Run
1. install dependencies:
   run in terminal - pip install transformers torch pillow
2. run the script:
   use run button in vs code
3. enter the path of an image when prompted

## How It Works
1. the image is passed through a vision encoder to extract visual features
2. these features are fed into a language decoder (transformer-based)
3. the decoder generates a natural language caption describing the image

## Learning Outcome
combining computer vision and NLP
using pretrained transformer based models
image feature extraction and sequence generation

## sample output 
\python.exe "c:/Users/Nikhi/OneDrive/Documents/Desktop/codoft ai internhip/CODSOFT_TASKSNO/Task3_image_captioning/image_caption.py"
Loading model... (first time, this will download the model)
Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
Loading weights: 100%|█| 473/473 [00:00<00:00
Enter image path (e.g. sample.jpg): C:\Users\Nikhi\OneDrive\Documents\Desktop\codoft ai internhip\CODSOFT_TASKSNO\Task3_image_captioning\sample.jpg

Generated Caption: a dog sitting in the grass

## Internship
this task is part of the CodSoft Artificial Intelligence Internship

#codsoft #internship #artificialintelligence
