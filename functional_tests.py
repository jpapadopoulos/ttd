from selenium import webdriver

browser = webdriver.Firefox()

# Edith has heard about a cool new online to-do app. She goes
# check it's homepage
browser.get('http://localhost:8000')

# She notices the page title and header mention to-do lists
assert 'To-Do' in browser.title

# She is invited to enter a to-do item right away

# She types "Buy peackock feathers" into a text box(Edith's hobby
# is tying fly-fishing lures)

# When she hits enter, the page updates, and now the page lists
# "1: Buy peackock feathers" as an item in a to-do list


# There is still a text box inviting her to add another item. She
# enters "Use peackock feathers to make a fly" (Edith is very methodical)

# The page updates again, and now shows items on her list

# Edith wonders whether the site will remember her list. Then she sees
# that the site has generated a unique URL for her -- there is some
# explanatory text to that effect

# She visits that URL - her to-do list is still there.

# Satisfied, she goes back to sleep

browser.quit()
