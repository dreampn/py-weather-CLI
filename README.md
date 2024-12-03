# Weather CLI (Command-Line Interface)

## Overview / ภาพรวม
โปรเจคนี้เป็นเครื่องมือ CLI ที่ช่วยให้ผู้ใช้สามารถดึงข้อมูลสภาพอากาศจากเมืองที่เลือก โดยโปรแกรมจะรองรับการเปลี่ยนแปลงภาษา (ภาษาอังกฤษ และ ภาษาไทย) และใช้งาน API จาก [OpenWeatherMap](https://openweathermap.org/) เพื่อดึงข้อมูลสภาพอากาศ

This is a CLI tool that allows users to get weather information for a selected city. The program supports multiple languages (English and Thai) and uses the [OpenWeatherMap API](https://openweathermap.org/) to fetch weather data.

## Features / ฟีเจอร์
- รองรับหลายภาษา (อังกฤษ, ไทย)
- แสดงสภาพอากาศจาก API ของ OpenWeatherMap
- รองรับการกรอกเมืองเพื่อค้นหาสภาพอากาศ
- รองรับการตั้งค่าอุณหภูมิเป็น Celsius

Supports multiple languages (English, Thai).
Fetches weather data using the OpenWeatherMap API.
Allows users to input a city and get weather information.
Temperature is displayed in Celsius.

## Requirements / ความต้องการ
- Python 3.x
- Requests library (สามารถติดตั้งได้ด้วยคำสั่ง ```pip install requests```)
- OpenWeatherMap API Key (สามารถสมัครได้ที่ [OpenWeatherMap](https://openweathermap.org/))

## วิธีการใช้งาน

1. ติดตั้ง dependencies ด้วยคำสั่ง:
```pip install requests```

2. สร้างไฟล์ JSON สำหรับภาษาที่ต้องการใช้งานในโฟลเดอร์ `locales/` เช่น `en.json` และ `th.json`

3. ใส่ API Key และ Base URL ในฟังก์ชัน `get_weather`:
```python
api_key = "YOUR_API_KEY"
base_url = "http://api.openweathermap.org/data/2.5/weather" 
```
4. รันโปรแกรม:
```
python weather_cli.py
```
โปรแกรมจะถามให้เลือกภาษา (en สำหรับภาษาอังกฤษ หรือ th สำหรับภาษาไทย) และให้กรอกชื่อเมืองที่ต้องการตรวจสอบสภาพอากาศ

Example / ตัวอย่างการใช้งาน

Output Example (English):
Choose language (en/th): en
Welcome to Weather CLI!
Enter city: London
The current weather in London is clear sky with a temperature of 15°C.

Example Output (Thai):
Choose language (en/th): th
ยินดีต้อนรับสู่ Weather CLI!
กรุณากรอกชื่อเมือง: กรุงเทพ
สภาพอากาศปัจจุบันในกรุงเทพคือท้องฟ้าแจ่มใส อุณหภูมิ 30°C




---

