import os
import sys
import time
import threading
from http.server import SimpleHTTPRequestHandler, HTTPServer
from playwright.sync_api import sync_playwright

PORT = 8082

def serve_site():
    os.chdir('/app')
    server_address = ('', PORT)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print(f"Serving VetVida on port {PORT}...")
    httpd.serve_forever()

def run_verification():
    # Start the local HTTP server in a daemon thread
    server_thread = threading.Thread(target=serve_site, daemon=True)
    server_thread.start()

    # Wait a brief moment for the server to spin up
    time.sleep(1.5)

    screenshot_dir = "/home/jules/verification/screenshots"
    video_dir = "/home/jules/verification/videos"
    os.makedirs(screenshot_dir, exist_ok=True)
    os.makedirs(video_dir, exist_ok=True)

    print("Launching browser via Playwright...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            record_video_dir=video_dir,
            viewport={"width": 1280, "height": 800}
        )
        page = context.new_page()

        # Enable dialog auto-accept and log alerts
        dialog_accepted = False
        def handle_dialog(dialog):
            nonlocal dialog_accepted
            print(f"Dialog encountered: [{dialog.type}] {dialog.message}")
            dialog.accept()
            dialog_accepted = True

        page.on("dialog", handle_dialog)

        # Navigate to VetVida
        url = f"http://localhost:{PORT}/index.html"
        print(f"Navigating to {url}...")
        page.goto(url)

        # Navigate to the Contact/Booking page
        print("Clicking 'Reservar Cita' to show contact form...")
        page.click("#nav-contacto")
        time.sleep(0.5)

        # Locate form and fields
        form = page.locator(".contact-form")
        form.scroll_into_view_if_needed()

        # Fill in form values
        print("Filling the contact form...")
        page.fill("#owner-name", "Juan Perez")
        page.fill("#phone", "+57 300 1234567")
        page.fill("#pet-name", "Firulais")
        page.select_option("#species", "Perro")
        page.select_option("#service-type", "Consulta general")
        page.fill("#date", "2026-10-15")
        page.select_option("#time", "10:00 AM")
        page.fill("#message", "Chequeo médico de rutina y desparasitación.")

        # Capture form filled state
        filled_screenshot = os.path.join(screenshot_dir, "form_filled.png")
        page.screenshot(path=filled_screenshot)
        print(f"Saved pre-submit screenshot to {filled_screenshot}")

        # Find the submit button
        submit_btn = form.locator('button[type="submit"]')

        # Submit the form
        print("Submitting the form...")
        submit_btn.click()

        # Verify the disabled state and text transition immediately
        time.sleep(0.2)
        btn_text = submit_btn.inner_html()
        btn_disabled = submit_btn.is_disabled()
        print(f"During submission - Button disabled: {btn_disabled}, Button text: '{btn_text}'")

        loading_screenshot = os.path.join(screenshot_dir, "form_loading.png")
        page.screenshot(path=loading_screenshot)
        print(f"Saved loading state screenshot to {loading_screenshot}")

        assert btn_disabled == True, "Error: Submit button was not disabled during submission!"
        assert "Enviando" in btn_text, f"Error: Submit button text was '{btn_text}', expected to contain 'Enviando'!"

        # Wait for simulation to finish (1000ms duration) and alert to trigger
        print("Waiting for submission simulation to complete...")
        page.wait_for_function("document.querySelector('.contact-form button[type=\"submit\"]').disabled === false")

        # Check restored state
        final_text = submit_btn.inner_html()
        final_disabled = submit_btn.is_disabled()
        print(f"Post submission - Button disabled: {final_disabled}, Button text: '{final_text}'")

        success_screenshot = os.path.join(screenshot_dir, "form_success.png")
        page.screenshot(path=success_screenshot)
        print(f"Saved final state screenshot to {success_screenshot}")

        assert final_disabled == False, "Error: Submit button was not re-enabled post-submission!"
        assert dialog_accepted == True, "Error: Standard alert dialog was not accepted or triggered!"

        # Close context and browser
        context.close()
        browser.close()

    print("Verification completed successfully! All assertions passed!")

if __name__ == "__main__":
    try:
        run_verification()
        sys.exit(0)
    except Exception as e:
        print(f"Verification failed: {e}")
        sys.exit(1)
