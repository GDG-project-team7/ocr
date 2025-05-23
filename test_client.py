import requests

url = "https://f6d6-39-120-211-141.ngrok-free.app/ocr"  # 본인 ngrok 주소
data = {"image_id": "ocr.test1.png"}  # 이미지 파일명

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, json=data, headers=headers)

print("Status code:", response.status_code)
print("Response:", response.json())
