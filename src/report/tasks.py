from celery import shared_task
from django.core.mail import send_mail
# @shared_task
# def read_photo_using_ocr(image):
#     image = Image.open(image)
#     pixel_values = processor(image, return_tensors="pt").pixel_values
#     generated_ids = model.generate(pixel_values)
#     generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)
#     return generated_text
