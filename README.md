# Nakrutka bot — qo‘lda yig‘iladigan loyiha

## Fayllar
Barcha Python fayllari bitta papkada. `bot.db` ishga tushganda avtomatik yaratiladi.

## O‘rnatish
```bash
pip install -r requirements.txt
```

`.env.example` nusxasini `.env` deb nomlang va token hamda admin ID ni kiriting.

Linux/macOS:
```bash
export BOT_TOKEN="TOKEN"
export ADMIN_ID="123456789"
python bot.py
```

Windows PowerShell:
```powershell
$env:BOT_TOKEN="TOKEN"
$env:ADMIN_ID="123456789"
python bot.py
```

## Buyruqlar
- `/start` — foydalanuvchi menyusi
- `/admin` — admin statistikasi
- `/status 3 Bajarildi` — buyurtma holatini yangilash

Bu starter buyurtmalarni qabul qiladi va admin tekshiruviga yuboradi. Avtomatik soxta obunachi/layk yetkazib berish yoki to‘lov funksiyasi yo‘q. Keyingi bosqichda ruxsatli marketing xizmatlari, narxlash va xavfsiz to‘lov jarayonini alohida qo‘shish mumkin.
