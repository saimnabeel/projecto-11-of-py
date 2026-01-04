from colorama import Fore, Style, init
import random
import time

init(autoreset=True)

def show_welcome():
    """Display welcome screen with neon colors"""
    print(Fore.MAGENTA + Style.BRIGHT + "=" * 50)
    print(Fore.CYAN + Style.BRIGHT + "    ✨ WELCOME TO THE NEON DICE GAME ✨")
    print(Fore.MAGENTA + Style.BRIGHT + "=" * 50)
    print(Fore.LIGHTGREEN_EX + "\n🎲 Press ENTER to roll the dice...\n")
    input()

def roll_animation():
    """Show rolling animation with neon effects and return final result"""
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "🎲 Rolling dice", end="", flush=True)
    for i in range(3):
        time.sleep(0.5)
        print(Fore.LIGHTYELLOW_EX + ".", end="", flush=True)
    print("\n")
    
    # Decide the final result first
    final_result = random.randint(1, 6)
    
    # Show random numbers during animation with cycling neon colors
    colors = [Fore.LIGHTCYAN_EX, Fore.LIGHTMAGENTA_EX, Fore.LIGHTYELLOW_EX, 
              Fore.LIGHTGREEN_EX, Fore.LIGHTRED_EX]
    for i in range(19):
        number = random.randint(1, 6)
        color = colors[i % len(colors)]
        print(color + Style.BRIGHT + f"  ⚡ {number} ⚡", end="\r", flush=True)
        time.sleep(0.08)
    
    # Show the final result at the end
    color = colors[19 % len(colors)]
    print(color + Style.BRIGHT + f"  ⚡ {final_result} ⚡", end="\r", flush=True)
    time.sleep(0.3)
    print("\n")
    return final_result

def main():
    show_welcome()
    
    while True:
        result = roll_animation()
        
        print(Fore.LIGHTGREEN_EX + Style.BRIGHT + f"{'=' * 50}")
        print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + f"✨ YOU ROLLED: {result} ✨")
        print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + f"{'=' * 50}\n")
        
        again = input(Fore.LIGHTCYAN_EX + "🎲 Roll again? (yes/no): ").lower()
        if again != "yes" and again != "y":
            print(Fore.LIGHTRED_EX + Style.BRIGHT + "\n✨ Thanks for playing! Goodbye! ✨\n")
            break

if __name__ == "__main__":
    main()
    