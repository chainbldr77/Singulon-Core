import datetime

class Logger:
    @staticmethod
    def log(message: str):
        ts = datetime.datetime.utcnow().isoformat()
        print(f"[{ts}] [SINGULON] {message}")
