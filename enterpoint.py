from memory import Memory
from run_Agent import run_agent

memory = Memory()


def enteryPoint():

    while True:

        user_input = input("\nAsk Question : ").strip()

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        memory.add_memory("user", user_input)

        print("\n[MEMORY]")
        print(memory.get_memory())

        try:
            print("WE ARE ENTRING INTO THE RUN_AGENT FUNCTION")
            response = run_agent(memory)
            print("WE ARE EXITING FROM THE RUN_AGENT FUNCTION")
            memory.add_memory("assistant", response)
            print("response", response)

        except Exception as e:
            print(f"\n[ERROR IS SHOWING HERE] {e}")
