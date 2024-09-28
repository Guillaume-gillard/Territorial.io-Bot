from selenium import webdriver

# Create the Firefox driver using the default configuration
driver = webdriver.Firefox()

# Open the game Territorial.io
driver.get("https://territorial.io")

# Keep the browser open for verification
input("Press Enter to close the browser...")


# Close the browser and end the session
driver.quit()
