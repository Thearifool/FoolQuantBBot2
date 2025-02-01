#!/bin/bash
echo "?? Deploying FoolQuantBot..."
export BINANCE_API_KEY=$(vault get binance_key)
export BINANCE_API_SECRET=$(vault get binance_secret)
docker compose up -d
