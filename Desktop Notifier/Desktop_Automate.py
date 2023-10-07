import time
import subprocess
from plyer import notification

def send_notification(title, message):
    script = f'display notification "{message}" with title "{title}"'
    subprocess.run(['osascript', '-e', script])

if __name__ == '__main__':
    while True:
        notification.notify(
            title="*** Take Rest ***",
            message="Work Hard and Keep Working",
            timeout=5
        )
        time.sleep(10)

        # Example usage:
    send_notification("Notification Title", "This is a notification message.")
