from tavily import TavilyClient

# API キーを設定してクライアントを生成
tavily_client = TavilyClient(
    api_key="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"
)

# 検索クエリを実行
response = tavily_client.search(
    "明日の天気を教えて",
    include_images=False,
    include_image_descriptions=False
)
print(response["results"][0]["content"])