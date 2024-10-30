# HashTracker

**HashTracker** to narzędzie do monitorowania integralności plików i katalogów, które pozwala wykrywać wszelkie zmiany w ich zawartości. Narzędzie tworzy i przechowuje skróty (hashe) dla plików w określonym katalogu, a następnie porównuje je w regularnych odstępach czasu, aby zidentyfikować wszelkie modyfikacje, dodane lub usunięte pliki.

## Funkcjonalności
- **Tworzenie skrótów (hashy) dla plików** w wybranym katalogu za pomocą algorytmu SHA-256.
- **Monitorowanie zmian** – wykrywanie dodanych, usuniętych lub zmodyfikowanych plików.
- **Raportowanie zmian** – generowanie raportów dotyczących zmienionych plików.
- **Tryb ciągły** – monitorowanie katalogu w czasie rzeczywistym z opcją zapisania wyników do pliku dziennika.
- **Powiadomienia** – opcjonalne powiadomienia o wykrytych zmianach (e-mail/SMS).

## Wymagania
- Python 3.6+
- Moduły: `hashlib`, `os`, `time`, `json`, `smtplib` (opcjonalnie dla e-maili)

## Instalacja
Zainstaluj wymagane moduły:
```bash
pip install hashlib
```

## Przykładowe dane

```bash
[Dodano] Nowy plik: C:\Users\gordu\Desktop\projekty\hashstracker\pedal.txt
[Dodano] Nowy plik: C:\Users\gordu\Desktop\projekty\hashstracker\euj.txt
[Zmiana] Zmieniono plik: C:\Users\gordu\Desktop\projekty\hashstracker\hashtracker.py
[Usunieto] Usunieto plik: C:\Users\gordu\Desktop\projekty\hashstracker\test.txt
```

## Bezpieczeństwo
HashTracker zapewnia ochronę integralności plików, ale nie zabezpiecza przed nieautoryzowanym dostępem. Aby zwiększyć bezpieczeństwo, rozważ użycie narzędzi antywirusowych i firewalli oraz korzystanie z zaszyfrowanych kopii zapasowych.

## Licencja
Projekt jest udostępniony na licencji MIT. Możesz dowolnie korzystać z kodu, modyfikować go i rozprowadzać, jednak autor nie ponosi odpowiedzialności za użycie narzędzia.
