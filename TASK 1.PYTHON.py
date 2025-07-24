from PIL import Image
import torch
from torchvision import models, transforms
from transformers import GPT2Tokenizer, GPT2LMHeadModel

# 🔧 Load pre-trained models
resnet = models.resnet50(pretrained=True)
resnet.eval()

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
caption_model = GPT2LMHeadModel.from_pretrained("gpt2")
caption_model.eval()

# 🖼 Image preprocessing
def preprocess_image(image_path):
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406], 
            std=[0.229, 0.224, 0.225]
        )
    ])
    image = Image.open(image_path).convert("RGB")
    return transform(image).unsqueeze(0)

# 🧠 Extract features
def extract_features(image_tensor):
    with torch.no_grad():
        features = resnet(image_tensor)
    return features

# 📝 Generate caption
def generate_caption(image_path):
    image_tensor = preprocess_image(image_path)
    features = extract_features(image_tensor)
    
    # Create prompt with dummy description
    prompt = "This image shows"
    inputs = tokenizer(prompt, return_tensors="pt")
    
    with torch.no_grad():
        outputs = caption_model.generate(
            inputs["input_ids"], 
            max_length=20, 
            num_return_sequences=1,
            do_sample=True,
            top_k=50
        )
    
    caption = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print("🖼 Caption:", caption)

# 📸 Test with an image
generate_caption("your_image.jpg")
