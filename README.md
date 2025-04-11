# แปลงคาราโอเกะNCNเป็นKAR

## ความต้องการ

- Python 3.x
- ไลบรารี `mido` สำหรับการจัดการไฟล์ MIDI

ติดตั้งไลบรารี `mido` โดยใช้คำสั่ง:

```bash
pip install mido
```
## การใช้งาน

1. เตรียมไฟล์ `.mid` (ทำนองเพลง), `.lyr` (เนื้อเพลง), และ `.cur` (ข้อมูลเวลา)
2. ใช้งานฟังก์ชัน `combine_to_kar` โดยระบุชื่อไฟล์ทั้งสาม และระบุชื่อไฟล์ `.kar` ที่ต้องการบันทึก

ตัวอย่างการเรียกใช้งาน:

```python
combine_to_kar("song.mid", "song.lyr", "song.cur", "output.kar")
```

หลังจากรันสคริปต์ จะได้ไฟล์ `.kar` ที่สร้างเสร็จในชื่อที่กำหนด

## ใบอนุญาต

โปรเจกต์นี้ใช้ใบอนุญาต **MIT License** ซึ่งหมายความว่าคุณสามารถใช้ แก้ไข และแจกจ่ายซอฟต์แวร์นี้ได้ตามต้องการ ภายใต้ข้อกำหนดในใบอนุญาต MIT

ดูรายละเอียดของใบอนุญาตได้ที่ [MIT License](https://opensource.org/licenses/MIT)
