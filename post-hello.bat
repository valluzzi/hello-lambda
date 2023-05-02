@echo off
set endpoint=http://localhost:3003
curl -X POST -H "Content-Type: application/json" -d "{\"name\":\"Jack\"}" %endpoint%