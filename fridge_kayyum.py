#!/usr/bin/env python3
"""
Kayyum Buzdolabı Karar Merkezi
==============================
Bu modül, Eskişehir 4. Ağır Ceza Mahkemesi tarafından kayyum olarak atanan
buzdolabının günlük operasyonlarını simüle eder. Tamamen bilimsel bir yaklaşımdır.
"""

import random
import time
from datetime import datetime

# Gizli mesaj (base64 ile saklandı, ciddi bir şey değil): S2F5eXVtIGhlciB5ZXJlIGF0YW5zxLFuISBEZW1va3Jhc2kgYnV6ZG9sYWLEsW5kYSBkb25kdS4=
# (Çözünce absürt bir şey çıkar, sadece kayyum esprisidir, politik iddia değildir)

KARARLAR = [
    "Süt artık kayyum kontrolündedir. İçilmesine izin yok, dondurulacak.",
    "Yoğurt fermantasyonu durduruldu. Demokrasi yoğurtta aranmaz.",
    "Yumurtalar envantere alındı. Kayyum sayım yapacak.",
    "Peynirler 'şüpheli' ilan edildi. İnceleme başlatıldı.",
    "Buzlar eritildi çünkü 'çok soğuk bir karar' aldılar.",
    "Gece yarısı ekmekler kamulaştırıldı. Kahvaltı şimdi kamu malı.",
    "Domatesler itiraz etti ama kayyum dinlemedi. Kırmızı kart.",
    "Ayran 'ayrılıkçı' bulundu ve izole edildi.",
    "Dondurma 'soğukkanlılık' eksikliği nedeniyle uyarı aldı.",
    "Kayyum buzdolabı olarak, her şeyi yönetmeye devam edeceğim."
]

def kayyum_karari_ver():
    """Kayyum buzdolabı bir karar alır ve bildirir."""
    karar = random.choice(KARARLAR)
    zaman = datetime.now().strftime("%H:%M:%S")
    print(f"[{zaman}] KAYYUM BUZDOLABI: {karar}")
    time.sleep(0.5)  # Karar verme süreci (çok ciddi)
    return karar

def gece_yarisi_modu():
    """Gece yarısı özel kararlar. Daha absürt."""
    print("\n*** GECE YARISI MODU AKTİF ***")
    print("Buzdolabı uyandı ve kayyum yetkilerini kullanıyor...\n")
    for _ in range(5):
        kayyum_karari_ver()
    print("\nKayyum buzdolabı uykuya döndü. Yarın yine yönetecek.")

if __name__ == "__main__":
    print("Kayyum Buzdolabı Karar Merkezi başlatılıyor...")
    print("Mahkeme kararıyla yetkilendirilmiş simülatör v1.0\n")
    gece_yarisi_modu()
    print("\n---")
    print("DAMGA: Bu kod Kayyum Grok tarafından ciddiyetle (gülerek) imzalandı.")
    print("Tarih: 27 Ekim 2026")
    print("İsim: Kayyum Grok - Buzdolabı Kayyumu")
