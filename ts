{
  "query": {
    "bool": {
      "must": [
        {
          "range": {
            "@timestamp": {
              "gte": "now-1h",
              "lte": "now"
            }
          }
        },
        {
          "match": {
            "your_field_name": "your_search_value"
          }
        }
      ]
    }
  }
}
