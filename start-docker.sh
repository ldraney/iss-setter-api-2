docker build -f Dockerfile.llm -t llm-api .
docker run -v /path/to/Llama-2-7b-hf:/app/Llama-2-7b-hf -p 5000:5000 llm-api
