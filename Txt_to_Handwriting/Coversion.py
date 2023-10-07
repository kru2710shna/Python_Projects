import pywhatkit as pw

txt = """
    High-Level purpose programming langauge. It's design philosophy 
    emphasis code redablity with it's use of significant 
    indentation.
    """
pw.text_to_handwriting(txt, "demo1.png" , [0,0,138])
print("\nEND\n")

