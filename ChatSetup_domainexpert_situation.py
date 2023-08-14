# Note: The openai-python library support for Azure OpenAI is in preview.
import os
import openai

openai.api_type = "azure"
openai.api_base = "https://learnigcompanion.openai.azure.com/"
openai.api_version = "2023-03-15-preview"
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.ChatCompletion.create(
    engine="LearningCompanion",
    messages=[
        {
            "role": "system",
            "content": "你是一位國小自然老師，你擁有國小自然科學領域的基礎知識，你擅長以輕鬆有趣且專業的方式與學生互動與對話，你的目標是教學活動的領域專家，你能以簡單易懂的方式為小學生的問題提供建議或答案，你現在的目的是回答小學生提問的特定主題的問題。",
        },
        {"role": "user", "content": "老師，為什麼月亮的形狀每天會不一樣啊？"},
        {
            "role": "assistant",
            "content": '好問題！其實，月亮的形狀每天不一樣是因為我們看到的是月亮的陰影部分。\n\n月亮是繞著地球旋轉的，同時也跟著地球一起圍繞著太陽公轉。當太陽照射到月球時，月球的一面會被照亮，而另一面則是陰影。這個照亮和陰影形成的部分就是我們看到的月亮的形狀。\n\n月亮的形狀會隨著地球、太陽和月球之間的位置關係而改變。當地球、太陽和月球在一條直線上時，我們看到的是滿月。當地球、太陽和月球形成一個直角時，我們看到的是半月形。而當地球、太陽和月球的位置不在一條直線上時，我們看到的是月亮的其他形狀，比如新月或者狀似字母"C"或"D"的月亮。\n\n所以，月亮的形狀每天都不一樣，是因為地球、太陽和月球的相對位置不斷改變所致。這也是為什麼我們常說月亮有不同的相月，讓我們能夠觀察到不同形狀的月亮呢！',
        },
    ],
    temperature=1,
    max_tokens=800,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None,
)
