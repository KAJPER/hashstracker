import hashlib
import os
import json
import time

class HashTracker:
    def __init__(self, directory):
        self.directory = directory
        self.hashes = {}

    def create_hash(self, file_path):
        hasher = hashlib.sha256()
        with open(file_path, 'rb') as f:
            buf = f.read()
            hasher.update(buf)
        return hasher.hexdigest()

    def scan_directory(self):
        for root, dirs, files in os.walk(self.directory):
            for file in files:
                file_path = os.path.join(root, file)
                self.hashes[file_path] = self.create_hash(file_path)

    def monitor_changes(self):
        while True:
            current_hashes = {}
            for root, dirs, files in os.walk(self.directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    current_hashes[file_path] = self.create_hash(file_path)

            self.compare_hashes(current_hashes)
            time.sleep(60)

    def compare_hashes(self, current_hashes):
        for file_path, file_hash in current_hashes.items():
            if file_path not in self.hashes:
                print(f"[Dodano] Nowy plik: {file_path}")
            elif self.hashes[file_path] != file_hash:
                print(f"[Zmiana] Zmieniono plik: {file_path}")

        for file_path in self.hashes:
            if file_path not in current_hashes:
                print(f"[Usunięto] Usunięty plik: {file_path}")

# Przykładowe użycie
tracker = HashTracker("C:\\przykladowe\\directory\\")
tracker.scan_directory()
tracker.monitor_changes()
