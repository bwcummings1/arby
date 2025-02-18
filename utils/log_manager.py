import logging

logging.basicConfig(filename="system_logs.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

def log_event(event):
    logging.info(event)

if __name__ == "__main__":
    log_event("✅ System initialized.")
