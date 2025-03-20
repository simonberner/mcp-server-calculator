# basic import
from mcp.server.fastmcp import FastMCP
import math

# create a FastMCP instance
# (FastMCP Server manages connections, follows the MCP protocol, and routes messages.)
mcp = FastMCP('hello world')

# DEFINE TOOLS
# (Tools help the server perform operations)

# addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Addition of two numbers"""
    return a + b

# subtraction tool
@mcp.tool()
def sub(a: int, b: int) -> int:
    """Subtraction of two numbers"""
    return a - b

# multiplication tool
@mcp.tool()
def mul(a: int, b: int) -> int:
    """Multiplication of two numbers"""
    return a * b

# division tool
@mcp.tool()
def div(a: int, b: int) -> int:
    """Division of two numbers"""
    return a / b

# square root tool
@mcp.tool()
def sqrt(a: int) -> int:
    """Square root of a number"""
    return math.sqrt(a)

# power tool
@mcp.tool()
def pow(a: int, b: int) -> int:
    """Power of a number"""
    return a ** b

# cube root tool
@mcp.tool()
def cbrt(a: int) -> int:
    """Cube root of a number"""
    return a ** (1/3)

# factorial tool
@mcp.tool()
def factorial(a: int) -> int:
    """Factorial of a number"""
    return math.factorial(a)

# log tool
@mcp.tool()
def log(a: int) -> float:
    """Log of a number"""
    return float(math.log(a))

# remainder tool
@mcp.tool()
def remainder(a: int, b: int) -> int:
    """Remainder of two numbers division"""
    return a % b

# sin tool
@mcp.tool()
def sin(a: int) -> float:
    """Sin of a number"""
    return float(math.sin(a))

# cos tool
@mcp.tool()
def cos(a: int) -> float:
    """Cos of a number"""
    return float(math.cos(a))

# tan tool
@mcp.tool()
def tan(a: int) -> float:
    """Tan of a number"""
    return float(math.tan(a))

# DEFINE RESOURCES

# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello {name}!"

# Start the MCP server and allow communication via standard input/output (stdio).
if __name__ == "__main__":
    mcp.run(transports="stdio")