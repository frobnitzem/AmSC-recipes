curl -X 'POST' \
  'https://api.i2-core.american-science-cloud.org/cost/estimate' \
  -H 'accept: application/json' \
  -H "x-litellm-api-key: $AMSCAI_API_KEY"
  -H 'Content-Type: application/json' \
  -d '{
  "model": "claude-sonnet-4-5",
  "input_tokens": 10000,
  "output_tokens": 1000,
  "num_requests_per_day": 10,
  "num_requests_per_month": 300
}'

curl -X 'POST' \
  'https://api.i2-core.american-science-cloud.org/chat/completions' \
  -H 'accept: application/json' \
  -H "x-litellm-api-key: $AMSCAI_API_KEY"
  -H 'Content-Type: application/json' \
  -d '{
  "model": "claude-sonnet-4-5",
  "messages": [
    {
      "role": "user",
      "content": "Write a list of scientific theory, modeling and simulation challenges that can be solved in the next year using help from large language models that would otherwise have taken much longer to solve."
    }
  ],
  "max_tokens": 5000,
  "temperature": 0.5
}'
