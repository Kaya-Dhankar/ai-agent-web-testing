from playwright.sync_api import sync_playwright
import time
import json

def execute_steps(steps):
    report = {
        "status": "PASS",
        "steps_executed": [],
        "errors": []
    }

    video_path = None

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()

            for step in steps:
                action = step.get("action")
                report["steps_executed"].append(step)

                if action == "open":
                    page.goto(step["url"])
                elif action == "search":
                    page.fill(step["selector"], step["text"])
                    page.press(step["selector"], "Enter")
                elif action == "click":
                    page.click(step["selector"])


                time.sleep(2)  # give time for actions


    except Exception as e:
        report["status"] = "FAIL"
        report["errors"].append(str(e))

    return report


# Example steps to test Flipkart video scenario
steps = [
    {"action": "open", "url": "https://www.google.com"},
    {"action": "click", "selector": "button:has-text('I agree')"},  # Accept cookies
    {"action": "search", "selector": "input[name='q']", "text": "Flipkart mobiles"},
    {"action": "click", "selector": "h3 >> nth=0"},
]

if __name__ == "__main__":
    report = execute_steps(steps)
    print(json.dumps(report, indent=4))