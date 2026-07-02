An Apache access log is available at:

/app/access.log

Generate a JSON report at:

/app/report.json

Requirements:

1. Count the total number of requests.
2. Count the number of unique client IP addresses.
3. Determine the most frequently requested path.
4. Write a JSON object with exactly these fields:

{
  "total_requests": <integer>,
  "unique_ips": <integer>,
  "top_path": "<string>"
}