import requests
import time
import threading
import argparse
import random

def googd0rk(query, user_agent):
  # Set Google Search URL
  url = "https://www.google.com/search?q=" + query
  # Set User-Agent header
  headers = {'User-Agent': user_agent}
  # Send HTTP GET request
  response = requests.get(url, headers=headers)
  # Return response
  return response.text

def dorkthosethreads(query, user_agent, output_file):
  # Perform the dorking
  result = googd0rk(query, user_agent)
  # Write the results to a log file
  with open(output_file, "a") as log_file:
    log_file.write(result)
  # Sleep for 5 seconds
  jitter = random.uniform(0, 2)
  time.sleep(5 + jitter)


def main():
      # Parse command line arguments
  parser = argparse.ArgumentParser()
  parser.add_argument("domain", help="the domain to be dorked")
  parser.add_argument("-o", "--output_file", default="d0rklog.log", help="the file to write the dorking results to")
  parser.add_argument("-q", "--query_file", default="dork_queries.txt", help="the file containing the dorking queries")
  parser.add_argument("-t", "--threads", type=int, default=1, help="the maximum number of parallel threads")
  parser.add_argument("-u", "--user_agent_file", default="user_agents.txt", help="the file containing the User-Agent strings")
  args = parser.parse_args()
  # Read the dork queries from a file
  with open(args.query_file, "r") as queries_file:
    queries = queries_file.readlines()
  # Read the User-Agent strings from a file
  with open(args.user_agent_file, "r") as user_agents_file:
    user_agents = user_agents_file.readlines()
  # Create a list of threads
  threads = []
  # Iterate through the queries
  for query in queries:
    # Choose a random User-Agent string
    user_agent = random.choice(user_agents)
    # Check if the maximum number of threads has been reached
    while len(threads) >= args.threads:
      # Wait for a thread to finish
      for t in threads:
        t.join(1)
        if not t.is_alive():
          threads.remove(t)
    # Create a new thread for the query
    t = threading.Thread(target=dorkthosethreads, args=(query, user_agent, args.output_file))
    # Add the thread to the list
    threads.append(t)
    # Start the thread
    t.start()

if __name__ == "__main__":
  main()
