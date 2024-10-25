from playwright.sync_api import Playwright, sync_playwright, expect
import time
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()


    # Clear cache
    context.clear_cookies()
    context.clear_permissions()
    page = context.new_page()
    url_1="https://careers.walmart.ca/search-jobs/Scarborough%20Bluffs%20Park%2C%20Ontario/4853/4/6251999-6093943-6141897/43x70213/-79x24318/50/2"
    url_2="https://careers.walmart.ca/search-jobs/Toronto%2C%20Ontario/4853/4/6251999-6093943-6167865/43x70011/-79x4163/50/2"
    url_3="https://careers.walmart.ca/search-jobs/Brampton%2C%20Ontario/4853/4/6251999-6093943-5907364/43x68341/-79x76633/50/2"
    url_4="https://careers.walmart.ca/search-jobs/Oshawa%2C%20Ontario/4853/4/6251999-6093943-6094578/43x90012/-78x84957/50/2"
    for i in range(1, 5):  
        url = locals()[f'url_{i}']  
        page.goto(url)

        for i in range(1, 4):  # Loop to click first 5 job links
        # for i in range (3):
            job_link = page.locator(f"#search-results-list > ul > li:nth-child({i}) > a")
            # job_link = page.locator(f"#search-results-list > ul > li:nth-child(5) > a")

            try:
                job_link.wait_for()
                job_link.click(timeout=3000)
                page.locator("#ajd-header").get_by_role("link", name="Apply").click()
                page.get_by_role("button", name="Apply").click()
                page.get_by_role("button", name="Use My Last Application").click()
                page.wait_for_load_state("networkidle")
                if page.locator("label[for='input-4']").count() > 0:
                    try:
                        page.get_by_label("Email Address").fill("tarunsaic0007@gmail.com")
                        # page.get_by_label("Email Address").fill("techiebears007@gmail.com")
                        page.get_by_label("Password").fill("Tarunc007@")
                        page.get_by_label("Sign In").click()
                        page.get_by_label("How Did You Hear About Us?*").click()
                        page.get_by_text("Referral").click()
                    except TimeoutError:
                        pass
                else:
                    page.get_by_label("How Did You Hear About Us?*").click()
                    page.get_by_text("Referral").click()

                # page.get_by_role("radio").check()
                page.get_by_text("I know someone who works here").click()
                # page.get_by_label("How Did You Hear About Us?*").press("Tab")
                page.get_by_text("What's their name or email").click()
                page.get_by_text("What's their name or email").fill("S0V05PQ.s01199@ca.wal-mart.com")

                page.locator('[data-automation-id="bottom-navigation-next-button"]').click()
                # page.get_by_role("button", name="Save and Continue").click()
                page.wait_for_load_state("networkidle")
                # page.get_by_text("Job Title").click()
                page.get_by_role("group", name="Work Experience 1").get_by_label("Job Title*").click()
                page.get_by_role("group", name="Work Experience 1").get_by_label("Job Title*").fill("Store / Sales Associate")
                page.locator('[data-automation-id="bottom-navigation-next-button"]').click()
                page.get_by_label("Do you certify you meet all").click()
                page.get_by_text("Yes").click()
                
                page.get_by_label("Would you like to receive").click()
                page.get_by_text("Opt-Out – you will NOT").click()
                # page.get_by_label("Are you legally able to work").click()
                # page.get_by_role("option", name="Yes").locator("div").click()
                # page.get_by_label("Please select your age").click()
                # page.get_by_text("years of age and Over").click()
                page.get_by_text("Are you legally able to work in the country where this job is located?", exact=True).click()
                page.get_by_label("Are you legally able to work").click()
                page.get_by_role("option", name="Yes").locator("div").click()
                page.get_by_text("Please select your age category:", exact=True).click()
                page.get_by_label("Please select your age").click()
                page.get_by_text("years of age and Over").click()
                page.get_by_text("Are you able to provide your SIN number within 3 days of your hire?", exact=True).click()
                page.get_by_label("Are you able to provide your").click()
                page.get_by_role("option", name="Yes").locator("div").click() 
                # page.get_by_label("Are you able to provide your").click()
                # page.get_by_role("option", name="Yes").locator("div").click()
                page.get_by_text("Please select your Walmart Associate Status/Affiliation:", exact=True).click()
                page.get_by_label("Please select your Walmart").click()
                page.get_by_role("option", name="Have never been an employee").locator("div").click()

                page.get_by_label("Walmart is an equal").click()
                page.get_by_role("option", name="Yes").locator("div").click()
                page.get_by_label("Have you ever been charged or").click()
                page.get_by_role("option", name="No, I have not").click()
                
                page.get_by_role("button", name="Save and Continue").click()
                page.get_by_label("Sunday").get_by_text("All Times Below Work for Me").click()
                page.get_by_label("Monday").get_by_text("All Times Below Work for Me").click()
                page.get_by_label("Tuesday").get_by_text("All Times Below Work for Me").click()
                page.get_by_label("Wednesday").get_by_text("All Times Below Work for Me").click()
                page.get_by_label("Thursday").get_by_text("All Times Below Work for Me").click()
                page.get_by_label("Friday").get_by_text("All Times Below Work for Me").click()
                page.get_by_label("Saturday").get_by_text("All Times Below Work for Me").click()
                
                page.get_by_label("My availability is: select").click()
                page.get_by_text("Either Full Time or Part Time").click()
                page.get_by_role("button", name="Save and Continue").click()
                # page.get_by_label("Yes, I have read and consent").check()
                page.get_by_text("Yes, I have read and consent").click()
                # page.locator("#input-102").check()
                time.sleep(2)
                page.wait_for_load_state("networkidle")
                page.locator('[data-automation-id="bottom-navigation-next-button"]').click()
                # page.get_by_role("button", name="Save and Continue").click()
                time.sleep(2)
                page.wait_for_load_state("networkidle")
                page.locator('[data-automation-id="bottom-navigation-next-button"]').click()

                # page.get_by_role("button", name="Submit").click()

                time.sleep(2)

            except Exception as e:
                print(f"An error occurred at job link {i}: {e}")
                page.goto(url)
                # page.goto("https://careers.walmart.ca/search-jobs/Waterloo%2C%20Ontario/4853/4/6251999-6093943-6176823/43x4668/-80x51639/50/2")
                continue  # Skip to the next iteration if an error occurs

    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
