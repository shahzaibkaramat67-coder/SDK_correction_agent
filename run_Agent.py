from model import modelfunction
from memory import Memory

# from model import client
from dotenv import load_dotenv
from Tools import search, research
from rich import print
import json

import os

load_dotenv()

memory = Memory()
print("memory", memory)


def emit(type, message):
    print(f"[{type}] {message}")


import re
import json

# def safe_json_parse(text):
#     text = text.strip()

#     # remove markdown fences
#     text = re.sub(r"```json|```", "", text)

#     # try parsing
#     return json.loads(text)


def run_agent(memory):
    print("WE ARE INSIDE THE AGENT FUNCTION NOW")

    while True:
        print("NOW WE ARE GOING TO RUN THE MODELFUNCTION HERE ")

        response = modelfunction(memory)
        print("response for the text or function call", response)
        # print("response for the text or without function call", response)
        messages = response.choices[0].message
        Tool = messages.tool_calls
        print("here are tool name", Tool)
        if not Tool:
            # print("here are tools")
            # print("RESPONSE:", response)
            # print("CHOICES:", response.choices)
            # print("MESSAGE:", response.choices[0].message)
            # print("CONTENT:", response.choices[0].message.content)
            return messages.content
        print("TOOL", Tool)
        name = Tool[0].function.name
        print("name :", name)
        memory.used_tool(name)
        print("name", name)
        arg = json.loads(Tool[0].function.arguments)
        print("age", arg)
        query = arg["query"]
        print("query", query)

        if Tool:
            if name == "search":
                print("this is search ")
                result = search(query=query, emit=emit)
                print("search_result", result)
                # search_result = "\n".join(
                #     f"title : {r['title']} \n URL : {r['url']} \n snippet  : {r['snippet']}"
                #     for r in search_result
                # )

                search_result = json.dumps({"Tool_name": name, "Tool_Result": result})

                print("search_final_result", search_result)
                memory.tool_memory("tool", Tool[0].id, search_result)
                print(
                    "memory show after update the search result : ", memory.get_memory()
                )
                continue
                # ✅ Fixed
            elif name == "research":
                print("this research funtion")
                source_memory = memory.get_memory()
                print("source_memory", source_memory)
                print("this research funtion 2", source_memory)
                research_result = research(
                    query=query, sources=source_memory, emit=emit
                )
                memory.tool_memory("tool", Tool[0].id, research_result)
        # else:
        #     print("RESPONSE:", response)
        #     print("CHOICES:", response.choices)
        #     print("MESSAGE:", response.choices[0].message)
        #     print("CONTENT:", response.choices[0].message.content)
        #     return response.choices[0].message.content


# from model import modelfunction
# from memory import Memory
# from dotenv import load_dotenv
# from Tools import search, researchexit
# import json, os

# load_dotenv()


# def emit(type, message):
#     print(f"[{type}] {message}")


# # def clean_json(text: str) -> str:
# #     text = text.strip()
# #     text = re.sub(r"^```json\s*", "", text)
# #     text = re.sub(r"^```\s*", "", text)
# #     text = re.sub(r"```$", "", text)
# #     return text.strip()


# def enteryPoint():
#     memory = Memory()
#     MAX_STEPS = 10

#     while True:
#         user_input = input("\nAsk Question: ").strip()
#         if user_input.lower() == "exit":
#             break

#         memory.add_memory("human", user_input)
#         step = 0

#         # ✅ Inner ReAct loop — Reason → Act → Observe → Repeat
#         while step < MAX_STEPS:
#             step += 1
#             raw = modelfunction(memory)

#             try:
#                 jsonResponse = json.loads(raw)
#             except json.JSONDecodeError:
#                 print("❌ Model returned invalid JSON:", raw)
#                 break

#             tool = jsonResponse.get("tool", "none")

#             if tool == "none":
#                 answer = jsonResponse.get("answer", "I don't know.")
#                 print(f"\n✅ FINAL ANSWER: {answer}")
#                 memory.add_memory("assistant", answer)
#                 break

#             elif tool == "search":
#                 result = search(jsonResponse["args"]["query"], emit=emit)
#                 memory.add_memory("tool", f"[SEARCH RESULT]\n{result}")

#             elif tool == "research":
#                 result = research(jsonResponse["args"]["query"], emit=emit)
#                 memory.add_memory("tool", f"[RESEARCH RESULT]\n{result}")

#             else:
#                 print(f"❌ Unknown tool: {tool}")
#                 break
#         else:
#             print("⚠️ Max steps reached without final answer.")
