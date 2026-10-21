class MealyMachine:
    def __init__(self):
        self.state = 'A'
        
    def transition(self, char):
        current_state = self.state
        next_state = 'TRAP'
        output = ''
        
        if current_state == 'A':
            if char == '/':
                next_state = 'B'
                output = 'b'
            elif char in ('a', '*'):
                next_state = 'TRAP'
                output = 'b'
                
        elif current_state == 'B':
            if char == '*':
                next_state = 'C'
                output = 'b'
            elif char in ('a', '/'):
                next_state = 'TRAP'
                output = 'b'
                
        elif current_state == 'C':
            if char in ('a', '/'):
                next_state = 'C'
                output = 'b'
            elif char == '*':
                next_state = 'D'
                output = 'b'
            else:
                next_state = 'TRAP'
                output = 'b'
                
        elif current_state == 'D':
            if char == '*':
                next_state = 'D'
                output = 'b'
            elif char == '/':
                next_state = 'E'
                output = 'a'
            elif char == 'a':
                next_state = 'C'
                output = 'b'
            else:
                next_state = 'TRAP'
                output = 'b'
                
        elif current_state == 'E':
            # Once comment ends at state E, further characters lead to TRAP
            next_state = 'TRAP'
            output = 'b'
            
        elif current_state == 'TRAP':
            next_state = 'TRAP'
            output = 'b'
            
        self.state = next_state
        return output

    def process(self, string):
        self.state = 'A'
        outputs = []
        for char in string:
            if char not in ('a', '*', '/'):
                self.state = 'TRAP'
                outputs.append('?')
                break
            out = self.transition(char)
            outputs.append(out)
            
        # A string is accepted if the final state is 'E'
        accepted = (self.state == 'E')
        return accepted, "".join(outputs)

# --- Testing with the examples from the image ---
machine = MealyMachine()

accepted_examples = [
    "/*a*/",
    "/**/",
    "/***/",
    "/*aaa*aaa*/",
    "/*a/a*/"
]

rejected_examples = [
    "/**",
    "/**/a/*aa*/",
    "aaa/**/aa",
    "/*/",
    "/**al",
    "//aaaa"
]

print("=== ACCEPTED EXAMPLES ===")
for s in accepted_examples:
    acc, out = machine.process(s)
    print(f"Input: {s:<15} | Accepted: {str(acc):<5} | Output: {out}")

print("\n=== REJECTED EXAMPLES ===")
for s in rejected_examples:
    acc, out = machine.process(s)
    print(f"Input: {s:<15} | Accepted: {str(acc):<5} | Output: {out}")