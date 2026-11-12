from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import JsonOutputParser

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash",temperature=0.7)

# Simple Prompt

prompt = "Suggest me a skill that is required as a Data Scientist"
response = llm.invoke(prompt)
print("Suggested Skill:\n", response.content)

# Create a Prompt Template

template = "Give me one skill that are required as a {occupation}. Please provide a concise response."
prompt_template = PromptTemplate.from_template(template)

filled_prompt = prompt_template.format(occupation = "Data Scientist")

response = llm.invoke(filled_prompt)
print("Suggested Skill:\n", response.content)


# StrOutputParser

prompt = "Suggest me three skill that is required as a Data Scientist"
llm_response = llm.invoke(prompt)

out_parser = StrOutputParser()

parsed_response = out_parser.parse(llm_response.content)

print(parsed_response)

# JsonOutputParser

parser = JsonOutputParser()

prompt = """
Suggest me three skills that is required as a Data Scientist.

Return your answer in JSON:

{
  "summary": "...",
  "skill_list": [...],
  "description": [...]
}
"""

response = llm.invoke(prompt)

result = parser.parse(response.content)

print(result)


# Without Chain and Parse

review = """
《环形物语》，一部六年前的科幻美剧，每集各自承载一则独立完整的小故事。
有着沉郁温柔的悲伤底色，清冷雪原、朦胧雾境、矗立旷野的环形高塔构成每一帧都极具诗意的唯美画面。
在这里，时间是非线性的，灵魂可以置换，时间能够静止，平行时空亦能交汇……不同奇幻设定分开来看自成篇章，人物线索彼此穿插伏笔，最后所有散落的命运轨迹收拢交织，完成一场圆满的闭环。
剥开科幻的外壳，整部剧的内核其实是普通人最质朴、最真挚的情感体验：孩童对母亲的执念、少年对人生选择的懊悔、恋人想要定格爱意的贪心、老人直面衰老与离别的坦然……在这片神奇的土地上，
世间规则被轻轻打破：时间不再单向流淌，过去与未来可以重叠相撞；两个少年误入机器完成灵魂置换，彻底改写人生；一枚手环便可冻结时间，让相爱之人独享永恒瞬间；
平行时空里的两个自我相遇，互相完成救赎。在环形轮回之中，几乎没有不可能发生的奇迹。
可真的如此吗？"Noting impossible"最终也只是一场温柔的自我慰藉。"The Loop"也许可以扭曲时空、制造奇遇，却没有逆转遗憾、改变过去的能力。我们可以穿越岁月重逢已故的亲人；
可以交换身份体验另一种人生；可以把心动的瞬间永久封存，却没办法抹平离别带来的空洞，修复早已碎裂的亲密关系，擦掉过往所有的过错与伤痛。兜兜转转走完命运的圆环，我们依旧要接受既定的失去，明白破碎无法复原，时光不能倒流。
所有的科幻设定都只是外壳，《环形物语》最终所呈现的，是离别、成长、思念、和解这一切最平凡的人间情绪。
在唯美忧伤的基调里，在这清冷朦胧的小镇上，我们一次次回环经历，终于知道，人生的遗憾无可回头。带着残缺走完人生的圆环，就是环形留给观众最温柔的答案。
"""

# Step 1: Translate to English
translate_prompt = PromptTemplate.from_template(
    "Translate the following review into English:\n\n{review}"
)

translate_response = llm.invoke(
    translate_prompt.format(review=review)
)

english_review = translate_response.content

print("English Review:")
print(english_review)

# Step 2: Summarize
summary_prompt = PromptTemplate.from_template(
    "Summarize the following review in one sentence:\n\n{review}"
)

summary_response = llm.invoke(
    summary_prompt.format(review=english_review)
)

summary = summary_response.content

print("\nSummary:")
print(summary)


# With Langchain Chain and Parse

review = """
《环形物语》，一部六年前的科幻美剧，每集各自承载一则独立完整的小故事。
有着沉郁温柔的悲伤底色，清冷雪原、朦胧雾境、矗立旷野的环形高塔构成每一帧都极具诗意的唯美画面。
在这里，时间是非线性的，灵魂可以置换，时间能够静止，平行时空亦能交汇……不同奇幻设定分开来看自成篇章，人物线索彼此穿插伏笔，最后所有散落的命运轨迹收拢交织，完成一场圆满的闭环。
剥开科幻的外壳，整部剧的内核其实是普通人最质朴、最真挚的情感体验：孩童对母亲的执念、少年对人生选择的懊悔、恋人想要定格爱意的贪心、老人直面衰老与离别的坦然……在这片神奇的土地上，
世间规则被轻轻打破：时间不再单向流淌，过去与未来可以重叠相撞；两个少年误入机器完成灵魂置换，彻底改写人生；一枚手环便可冻结时间，让相爱之人独享永恒瞬间；
平行时空里的两个自我相遇，互相完成救赎。在环形轮回之中，几乎没有不可能发生的奇迹。
可真的如此吗？"Noting impossible"最终也只是一场温柔的自我慰藉。"The Loop"也许可以扭曲时空、制造奇遇，却没有逆转遗憾、改变过去的能力。我们可以穿越岁月重逢已故的亲人；
可以交换身份体验另一种人生；可以把心动的瞬间永久封存，却没办法抹平离别带来的空洞，修复早已碎裂的亲密关系，擦掉过往所有的过错与伤痛。兜兜转转走完命运的圆环，我们依旧要接受既定的失去，明白破碎无法复原，时光不能倒流。
所有的科幻设定都只是外壳，《环形物语》最终所呈现的，是离别、成长、思念、和解这一切最平凡的人间情绪。
在唯美忧伤的基调里，在这清冷朦胧的小镇上，我们一次次回环经历，终于知道，人生的遗憾无可回头。带着残缺走完人生的圆环，就是环形留给观众最温柔的答案。
"""

# Prompt 1
translate_prompt = PromptTemplate.from_template(
    "Translate the following review into English:\n\n{review}"
)

# Prompt 2
summary_prompt = PromptTemplate.from_template(
    "Summarize the following review in one sentence:\n\n{review}"
)

parser = StrOutputParser()

# Build the first chain
translation_chain = translate_prompt | llm | parser

# Build the second chain
summary_chain = summary_prompt | llm | parser

# Execute sequentially
english_review = translation_chain.invoke(
    {"review": review}
)

summary = summary_chain.invoke(
    {"review": english_review}
)

print("English Review:")
print(english_review)

print("\nSummary:")
print(summary)