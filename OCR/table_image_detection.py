import requests
from PIL import Image
from transformers import AutoProcessor, AutoModelForCausalLM 

model = AutoModelForCausalLM.from_pretrained("yifeihu/TFT-ID-1.0", trust_remote_code=True)
processor = AutoProcessor.from_pretrained("yifeihu/TFT-ID-1.0", trust_remote_code=True)

prompt = "<OD>"

url = "https://huggingface.co/yifeihu/TF-ID-base/resolve/main/arxiv_2305_10853_5.png?download=true"
image = Image.open(requests.get(url, stream=True).raw)

inputs = processor(text=prompt, images=image, return_tensors="pt")

generated_ids = model.generate(
    input_ids=inputs["input_ids"],
    pixel_values=inputs["pixel_values"],
    max_new_tokens=1024,
    do_sample=False,
    num_beams=3
)
generated_text = processor.batch_decode(generated_ids, skip_special_tokens=False)[0]

parsed_answer = processor.post_process_generation(generated_text, task="<OD>", image_size=(image.width, image.height))

print(parsed_answer)