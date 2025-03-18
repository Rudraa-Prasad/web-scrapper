from scrapegraphai.graphs import SmartScraperGraph

# Define the configuration for the graph
graph_config = {
    "llm": {
        "api_key": "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",
        "model": "mixtral-8x7b-32768"
    },
}

# Create the SmartScraperGraph instance
smart_scraper_graph = SmartScraperGraph(
    prompt="List me all the articles",
    source="https://perinim.github.io/projects",
    config=graph_config
)

# Run the scraping pipeline
result = smart_scraper_graph.run()

# Print the extracted information
print(result)