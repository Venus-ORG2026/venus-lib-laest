import webview
from app.api import Api

if __name__ == "__main__":
    api = Api()
    webview.create_window(
        "Venus Library",
        "ui/login.html",
        js_api=api,
        width=1200,
        height=800
    )
    webview.start()
