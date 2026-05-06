#!/usr/bin/env python3
"""
A simple script to display "Good evening Goodwallers" with bright lighting effects
"""

def display_with_bright_lighting():
    """Display greeting with bright lighting effects using colored text"""
    
    # ANSI color codes for bright colors
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_WHITE = '\033[97m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    
    # Create a bright lighting effect with decorative elements
    lighting = f"{BRIGHT_YELLOW}{'✨' * 20}{RESET}"
    
    print("\n" + lighting)
    print(f"{BRIGHT_WHITE}{BOLD}{'=' * 50}{RESET}")
    print(f"{BRIGHT_CYAN}{BOLD}     💡 GOOD EVENING GOODWALLERS 💡     {RESET}")
    print(f"{BRIGHT_WHITE}{BOLD}{'=' * 50}{RESET}")
    print(lighting + "\n")
    
    # Additional bright welcome message
    welcome_messages = [
        f"{BRIGHT_GREEN}🌟 Welcome to the bright evening! 🌟{RESET}",
        f"{BRIGHT_YELLOW}⚡ Hope you're having a luminous day! ⚡{RESET}",
        f"{BRIGHT_CYAN}✨ Shining bright together! ✨{RESET}"
    ]
    
    for message in welcome_messages:
        print(message)
    
    print("\n" + lighting + "\n")

if __name__ == "__main__":
    display_with_bright_lighting()
