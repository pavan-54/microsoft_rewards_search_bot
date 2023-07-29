from selenium import webdriver
import time

def generate_unique_keyword(base_keyword, iteration):
    return base_keyword + "i" * iteration

def edge_search_bot_unique(base_keyword, num_searches):
    # Create an instance of Edge WebDriver
    driver = webdriver.Edge()

    # Maximize the browser window
    driver.maximize_window()

    # Perform searches
    for i in range(num_searches):
        print(f"Performing search {i+1}/{num_searches}")
        # Generate a unique search query
        search_query = generate_unique_keyword(base_keyword, i)

        # Construct the search URL with the unique search query
        search_url = f"https://www.bing.com/search?q={search_query}"

        # Navigate to the search URL directly
        driver.get(search_url)

        # Wait for a short time to prevent overloading the search engine
        time.sleep(5)

    # Close the browser after all searches are done
    driver.quit()
    print("All searches completed successfully.")

if __name__ == "__main__":
    base_keyword = "hi"  # The initial keyword
    num_searches = 45    # Set the number of searches you want to perform

    edge_search_bot_unique(base_keyword, num_searches)
