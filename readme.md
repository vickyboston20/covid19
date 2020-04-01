# COVID 19 stats for India

The covid stats for india statewise using scrapy framework-python (web scraped form the http://www.mohfw.gov.in/ ) 

## PREREQUISITE
docker

docker-compose

## How to run docker
docker-compose build

docker-compose up -d

## For accessing api

http://localhost:3000/crawl.json?start_requests=true&spider_name=india_states

## OUTPUT as Json
covid.json
----
```
{
  "status": "ok",
  "items": [
    {
      "states_no": "1",
      "states_name": "Andhra Pradesh",
      "total_confirmed_cases": "40",
      "cured_discharged_migrated": "1",
      "death": "0"
    },
    {
      "states_no": "2",
      "states_name": "Andaman and Nicobar Islands",
      "total_confirmed_cases": "10",
      "cured_discharged_migrated": "0",
      "death": "0"
    },
    {
      "states_no": "3",
      "states_name": "Bihar",
      "total_confirmed_cases": "15",
      "cured_discharged_migrated": "0",
      "death": "1"
    },
    {
      "states_no": "4",
      "states_name": "Chandigarh",
      "total_confirmed_cases": "13",
      "cured_discharged_migrated": "0",
      "death": "0"
    },
    {
      "states_no": "5",
      "states_name": "Chhattisgarh",
      "total_confirmed_cases": "8",
      "cured_discharged_migrated": "0",
      "death": "0"
    },
    {
      "states_no": "6",
      "states_name": "Delhi",
      "total_confirmed_cases": "97",
      "cured_discharged_migrated": "6",
      "death": "2"
    },
    {
      "states_no": "7",
      "states_name": "Goa",
      "total_confirmed_cases": "5",
      "cured_discharged_migrated": "0",
      "death": "0"
    },
    {
      "states_no": "8",
      "states_name": "Gujarat",
      "total_confirmed_cases": "73",
      "cured_discharged_migrated": "3",
      "death": "6"
    },
    {
      "states_no": "9",
      "states_name": "Haryana",
      "total_confirmed_cases": "40",
      "cured_discharged_migrated": "21",
      "death": "0"
    },
    {
      "states_no": "10",
      "states_name": "Himachal Pradesh",
      "total_confirmed_cases": "3",
      "cured_discharged_migrated": "0",
      "death": "1"
    },
    {
      "states_no": "11",
      "states_name": "Jammu and Kashmir",
      "total_confirmed_cases": "54",
      "cured_discharged_migrated": "2",
      "death": "2"
    },
    {
      "states_no": "12",
      "states_name": "Karnataka",
      "total_confirmed_cases": "83",
      "cured_discharged_migrated": "5",
      "death": "3"
    },
    {
      "states_no": "13",
      "states_name": "Kerala",
      "total_confirmed_cases": "234",
      "cured_discharged_migrated": "19",
      "death": "1"
    },
    {
      "states_no": "14",
      "states_name": "Ladakh",
      "total_confirmed_cases": "13",
      "cured_discharged_migrated": "3",
      "death": "0"
    },
    {
      "states_no": "15",
      "states_name": "Madhya Pradesh",
      "total_confirmed_cases": "47",
      "cured_discharged_migrated": "0",
      "death": "3"
    },
    {
      "states_no": "16",
      "states_name": "Maharashtra",
      "total_confirmed_cases": "216",
      "cured_discharged_migrated": "39",
      "death": "9"
    },
    {
      "states_no": "17",
      "states_name": "Manipur",
      "total_confirmed_cases": "1",
      "cured_discharged_migrated": "0",
      "death": "0"
    },
    {
      "states_no": "18",
      "states_name": "Mizoram",
      "total_confirmed_cases": "1",
      "cured_discharged_migrated": "0",
      "death": "0"
    },
    {
      "states_no": "19",
      "states_name": "Odisha",
      "total_confirmed_cases": "3",
      "cured_discharged_migrated": "0",
      "death": "0"
    },
    {
      "states_no": "20",
      "states_name": "Puducherry",
      "total_confirmed_cases": "1",
      "cured_discharged_migrated": "0",
      "death": "0"
    },
    {
      "states_no": "21",
      "states_name": "Punjab",
      "total_confirmed_cases": "41",
      "cured_discharged_migrated": "1",
      "death": "3"
    },
    {
      "states_no": "22",
      "states_name": "Rajasthan",
      "total_confirmed_cases": "74",
      "cured_discharged_migrated": "3",
      "death": "0"
    },
    {
      "states_no": "23",
      "states_name": "Tamil Nadu",
      "total_confirmed_cases": "74",
      "cured_discharged_migrated": "4",
      "death": "1"
    },
    {
      "states_no": "24",
      "states_name": "Telengana",
      "total_confirmed_cases": "79",
      "cured_discharged_migrated": "1",
      "death": "1"
    },
    {
      "states_no": "25",
      "states_name": "Uttarakhand",
      "total_confirmed_cases": "7",
      "cured_discharged_migrated": "2",
      "death": "0"
    },
    {
      "states_no": "26",
      "states_name": "Uttar Pradesh",
      "total_confirmed_cases": "101",
      "cured_discharged_migrated": "14",
      "death": "0"
    },
    {
      "states_no": "27",
      "states_name": "West Bengal",
      "total_confirmed_cases": "26",
      "cured_discharged_migrated": "0",
      "death": "2"
    },
    {
      "total_india": "Total number of confirmed cases in India",
      "total_confirmed_cases_india": "1397#",
      "total_cured_discharged_migrated": "124",
      "total_death": "35"
    }
  ],
  "items_dropped": [ ],
  "stats": {
    "downloader/request_bytes": 880,
    "downloader/request_count": 4,
    "downloader/request_method_count/GET": 4,
    "downloader/response_bytes": 12966,
    "downloader/response_count": 4,
    "downloader/response_status_count/200": 1,
    "downloader/response_status_count/301": 2,
    "downloader/response_status_count/404": 1,
    "finish_reason": "finished",
    "finish_time": "2020-04-01 05:44:49",
    "item_scraped_count": 28,
    "log_count/DEBUG": 32,
    "log_count/INFO": 8,
    "memusage/max": 56471552,
    "memusage/startup": 56471552,
    "response_received_count": 2,
    "robotstxt/request_count": 1,
    "robotstxt/response_count": 1,
    "robotstxt/response_status_count/404": 1,
    "scheduler/dequeued": 2,
    "scheduler/dequeued/memory": 2,
    "scheduler/enqueued": 2,
    "scheduler/enqueued/memory": 2,
    "start_time": "2020-04-01 05:44:48"
  },
  "spider_name": "india_states"
}
```