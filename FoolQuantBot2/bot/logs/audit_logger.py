import datetime

class AuditLogger:
    def log_event(self, event):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open('FoolQuantBot2/logs/trading_audit.log', 'a') as log_file:
            log_file.write(f"{timestamp} - {event}\n")
        print(f"📝 {timestamp} - {event}")
