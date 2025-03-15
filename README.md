# 🛠️ Discord Görev Yönetim Botu

Bu proje, Discord üzerinde **küçük ekipler için görev yönetimi yapmayı sağlayan bir bot** içerir.  
Görev ekleme, silme, listeleme ve tamamlama gibi işlemleri yapabilir. Veriler **SQLite veritabanında saklanır**.

---

## 📌 Özellikler
- ✅ **Görev Ekleme:** Kullanıcılar kolayca yeni görevler ekleyebilir.
- 👋 **Görev Listeleme:** Kayıtlı tüm görevleri listeleyebilir.
- 🟢 **Görev Tamamlama:** Tamamlanan görevleri işaretleyebilir.
- 🛢 **Görev Silme:** İstenilen görevleri silebilir.
- 💾 **Veritabanı:** **SQLite** kullanılarak görevler saklanır.

---

## 🚀 Kurulum ve Çalıştırma

### 1️⃣ Gerekli Bağımlılıkları Yükleyin
Python yüklü değilse, **[Python 3.x](https://www.python.org/downloads/)** sürümünü kurun.  
Ardından, **proje dizinine girin** ve şu komutu çalıştırın:

```sh
pip install -r requirements.txt
```

Eğer `requirements.txt` yoksa, bağımlılıkları tek tek yüklemek için:

```sh
pip install discord.py aiosqlite
```

---

### 2️⃣ Discord Bot Tokenını Alın
1. **[Discord Developer Portal](https://discord.com/developers/applications/)** sitesine gir.
2. **"New Application"** oluştur ve adını belirle.
3. **"Bot"** sekmesine geç, **"Add Bot"** butonuna tıkla.
4. **Token'ı kopyalayın ve `config.py` dosyasına yapıştırın.**

Token projede verilmiştir
```python
# config.py
BOT_TOKEN = "BURAYA_BOT_TOKENİNİ_YAPIŞTIR"
DATABASE_NAME = "tasks.db"
```

---

### 3️⃣ Botu Sunucuya Ekle
1. **[Discord Developer Portal](https://discord.com/developers/applications/)** sayfasına gidin.
2. **OAuth2 > URL Generator** sekmesine tıklayın.
3. **Scopes** bölümünde **"bot"** seçeneğini işaretleyin.
4. **Bot Permissions** kısmında şu izinleri verin:
   - Read Messages
   - Send Messages
   - Read Message History
   - Use Slash Commands (isteğe bağlı)
5. **Oluşan URL'yi kopyalayın** ve tarayıcınıza yapıştırarak botu sunucunuza ekleyin.

---

### 4️⃣ Botu Çalıştırın
Terminal veya komut satırında **bot dosyasının olduğu dizine girin**:

```sh
cd task_manager_bot
python bot.py
```

Eğer her şey doğru yapılandırıldıysa **şu mesajı görmelisiniz:**
```
Bot <Bot İsmi> olarak giriş yaptı!
```

---

## 💚 Kullanım

### Komutlar

#### `!add_task <görev açıklaması>`
Yeni bir görev ekler.  
**Örnek:** `!add_task Sunum hazırla`

#### `!show_tasks`
Tüm görevleri listeler.  
**Örnek:** `!show_tasks`

#### `!complete_task <ID>`
Belirtilen görevi tamamlandı olarak işaretler.  
**Örnek:** `!complete_task 1`

#### `!delete_task <ID>`
Belirtilen ID'ye sahip görevi siler.  
**Örnek:** `!delete_task 2`

---

## 🧪 Testler
Botun düzgün çalıştığını kontrol etmek için testleri çalıştırabilirsiniz.

```sh
python run_tests.py
```

Eğer testler başarılı olursa, şu sonucu almalısınız:
```
....
----------------------------------------------------------------------
Ran 4 tests in 0.002s

OK
```

---

## 🛠️ Proje Dosya Yapısı

```
task_manager_bot/
├── bot.py                # Discord botunun ana dosyası
├── database.py           # Veritabanı işlemleri
├── config.py             # Yapılandırma dosyası (TOKEN, DB adı)
├── tests/                # Testler
│   ├── test_add_task.py
│   ├── test_delete_task.py
│   ├── test_show_tasks.py
│   ├── test_complete_task.py
├── requirements.txt      # Bağımlıklar
├── README.md             # Kurulum ve kullanım talimatları
└── run_tests.py          # Testleri çalıştıran dosya
```

---

## 🐟 Lisans
Bu proje **MIT Lisansı** ile lisanslanmıştır. **İstediğiniz gibi kullanabilir, değiştirebilir ve geliştirebilirsiniz.**  

---


