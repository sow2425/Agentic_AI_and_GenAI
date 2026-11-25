from fastmcp import FastMCP
from google import genai

mcp=FastMCP("Gemini Calculator")

client=genai.Client(api_key="AIzaSyA3koXS7uL32NHX5evLxfxKNPRVluxhRUs")
@mcp.tool()
def ask_gemini(questions:str):
    response=client.models.generate_contents(
        model="gemini-2.5-flash",
        content=questions
    )
    return response.text

@mcp.tool()
def calculator(a:float,b:float,opertion:str):
    if opertion=="add":
        return a+b
    if opertion=="sub":
        return a-b
    
if __name__=="__main__":
    mcp.run()