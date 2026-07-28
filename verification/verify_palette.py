import os
import time
import threading
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
from playwright.sync_api import sync_playwright

PORT = 8082

class MyHTTPHandler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        return os.path.join("/app", path.lstrip("/"))

def start_server():
    os.chdir("/app")
    handler = MyHTTPHandler
    TCPServer.allow_reuse_address = True
    with TCPServer(("", PORT), handler) as httpd:
        print(f"Serving HTTP on port {PORT}")
        httpd.serve_forever()

def run_cuj(page):
    page.goto(f"http://localhost:{PORT}")
    page.wait_for_timeout(1000)

    # Switch to contact page
    page.evaluate("showPage('contacto')")
    page.wait_for_timeout(1000)

    # Locate contact form
    contact_form = page.locator(".contact-form")
    contact_form.scroll_into_view_if_needed()
    page.wait_for_timeout(500)

    # Take screenshot before filling/submitting
    page.screenshot(path="/home/jules/verification/screenshots/1_contact_form_empty.png")
    page.wait_for_timeout(500)

    # Fill form fields
    page.locator("#owner-name").fill("Juan Pérez")
    page.locator("#phone").fill("+57 321 9876543")
    page.locator("#pet-name").fill("Firulais")
    page.locator("#species").select_option("Perro")
    page.locator("#service-type").select_option("Consulta general")
    page.locator("#date").fill("2026-08-15")
    page.locator("#time").select_option("10:00 AM")
    page.locator("#message").fill("Mi perro necesita una revisión general preventiva.")
    page.wait_for_timeout(500)

    # Set up alert dialog handler
    page.on("dialog", lambda dialog: dialog.accept())

    # Take screenshot after filling but before submit
    page.screenshot(path="/home/jules/verification/screenshots/2_contact_form_filled.png")
    page.wait_for_timeout(500)

    # Click the submit button
    submit_btn = contact_form.locator('button[type="submit"]')
    submit_btn.click()

    # Immediately check disabled state and text
    page.wait_for_timeout(100)
    is_disabled = submit_btn.is_disabled()
    btn_text = submit_btn.inner_html()
    print(f"Submit button state during submission: disabled={is_disabled}, text='{btn_text}'")

    # Capture a screenshot showing the submitting state (Enviando... with disabled button)
    page.screenshot(path="/home/jules/verification/screenshots/3_contact_form_submitting.png")

    # Wait for simulation to finish
    page.wait_for_timeout(1200)

    # Verify that form is reset and button is restored
    is_disabled_after = submit_btn.is_disabled()
    btn_text_after = submit_btn.inner_html()
    print(f"Submit button state after submission: disabled={is_disabled_after}, text='{btn_text_after}'")

    owner_name_val = page.locator("#owner-name").input_value()
    print(f"Owner name input value after form reset: '{owner_name_val}'")

    # Take final screenshot showing successful reset
    page.screenshot(path="/home/jules/verification/screenshots/verification.png")
    page.wait_for_timeout(1000)

if __name__ == "__main__":
    server_thread = threading.Thread(target=start_server, daemon=True)
    server_thread.start()
    time.sleep(1)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            record_video_dir="/home/jules/verification/videos"
        )
        page = context.new_page()
        try:
            run_cuj(page)
        finally:
            context.close()
            browser.close()
    print("Verification completed successfully!")
