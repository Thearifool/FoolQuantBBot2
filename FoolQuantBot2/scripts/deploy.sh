
#!/bin/bash
echo '?? Deploying FoolQuantBot...'
docker compose -f prod.yml up -d --scale traders=3
echo '? Deployment Successful!'

