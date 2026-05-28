from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import Literal, TypedDict, Annotated, Optional
from pydantic import BaseModel, Field

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

json_schema = {
    "title":"Review",
    "type":"object",
    "properties":{
        "key_themes":{
            "type":"array",
            "items":{
                "type":"string"
            },
            "description":"Write all the key themes of the review"
        },
        "summary":{
            "type":"string",
            "description":"Write the summary of the review"
        },
        "sentiments":{
            "type":"string",
            "enum":["pos","neg"],
            "description":"Write the sentiments of the review either positive,negative or neutral"
        },
        "pros":{
            "type":["array", "null"],
            "item":{
                "type":"string"
            },
            "description":"Write down all the pros in a list"
        },
        "cons":{
            "type":["array", "null"],
            "item":{
                "type":"string"
            },
            "description":"Write down all the cons in a list"
        },
        "name":{
            "type":["string", "null"],
            "description":"Write the name of the reviewer"
        }
    },
    "required":["key_themes","summary","sentiments"]

}

structured_model = model.with_structured_output(json_schema)

result = structured_model.invoke("I recently bought the iPhone 16 Pro and after using it for a few days," 
" my overall experience has been quite impressive, though there are a few drawbacks as well. The first thing that" 
" stood out was the premium design and build quality. The phone feels extremely solid and luxurious in hand, with" 
" a sleek finish and comfortable grip despite being slightly heavy. The display is one of the biggest highlights" 
" — the screen is bright, sharp, and incredibly smooth thanks to the high refresh rate. Watching videos, scrolling " 
"through social media, and gaming all feel very fluid and immersive." 



"Performance-wise, the phone handles everything effortlessly. Apps open instantly, multitasking "
"is smooth, and even heavy games run without noticeable lag. I also noticed that the device manages" 
" heat better than many other phones, although it can become warm during long gaming sessions or while" 
" charging. The battery life is reliable and easily lasts a full day with normal to heavy usage, and " 
"the fast charging support is very convenient."

"The camera performance is excellent, especially in daylight conditions where the photos come out " 
"detailed, vibrant, and natural-looking. Portrait shots and video stabilization are particularly " 
"impressive. Low-light photography is also good, though sometimes the processing feels a bit artificial." 
"The front camera performs well for selfies and video calls, making it suitable for content creators "
"and regular users alike."

"On the software side, the user interface feels polished, clean, and easy to use. Animations are smooth,"
" and the overall experience feels premium. However, there are still a few downsides. The phone is expensive,"
" and some users may feel that the improvements over previous models are not revolutionary. Additionally," 
" accessories and repairs can also be costly."

"Overall, this phone delivers an excellent flagship experience with strong performance, a beautiful display," 
" reliable cameras, and premium build quality. While it has a few minor weaknesses such as heating during" 
" intensive tasks and high pricing, it still stands out as one of the best smartphones currently available "
"for users who want a powerful and polished device. ")


print(result)