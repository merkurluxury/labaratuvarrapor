import tkinter as tk
import pandas as pd

# Uygulama penceresini oluşturmak için Tkinter kullanalım
window = tk.Tk()
window.title("Laboratuvar Raporlama Uygulaması")

# Verileri depolamak için bir Pandas DataFrame'i oluşturalım
data = pd.DataFrame(columns=["Örnek Adı", "Sonuç"])

# Kullanıcıdan veri girişi alacak olan fonksiyonu tanımlayalım
def submit_data():
    sample_name = sample_name_entry.get()
    result = result_entry.get()

    # Verileri DataFrame'e ekleme
    data.loc[len(data)] = [sample_name, result]

    # Veri girişinden sonra metin kutularını temizleme
    sample_name_entry.delete(0, tk.END)
    result_entry.delete(0, tk.END)

# Rapor oluşturma fonksiyonu
def generate_report():
    # Raporu Pandas DataFrame üzerinden oluşturma
    report = data.to_string(index=False)

    # Raporu ekrana yazdırma
    report_text.insert(tk.END, report)

# Kullanıcı arayüzünü oluşturma
sample_name_label = tk.Label(window, text="Örnek Adı:")
sample_name_label.pack()
sample_name_entry = tk.Entry(window)
sample_name_entry.pack()

result_label = tk.Label(window, text="Sonuç:")
result_label.pack()
result_entry = tk.Entry(window)
result_entry.pack()

submit_button = tk.Button(window, text="Veri Gönder", command=submit_data)
submit_button.pack()

generate_report_button = tk.Button(window, text="Rapor Oluştur", command=generate_report)
generate_report_button.pack()

report_text = tk.Text(window)
report_text.pack()

window.mainloop()