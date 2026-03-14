class StoryNode:
    def __init__(self, node_id: str, text: str):
        self.node_id = node_id
        self.text = text
        # Dictionary mapping the choice description to the next node_id
        self.choices = {} 

    def add_choice(self, choice_text: str, next_node_id: str):
        self.choices[choice_text] = next_node_id

class Story:
    def __init__(self):
        self.nodes = {}
        self.current_node_id = None

    def add_node(self, node: StoryNode):
        self.nodes[node.node_id] = node

    def set_start_node(self, node_id: str):
        if node_id in self.nodes:
            self.current_node_id = node_id
        else:
            raise ValueError(f"Start node '{node_id}' does not exist.")

    def get_current_node(self) -> StoryNode:
        if self.current_node_id and self.current_node_id in self.nodes:
            return self.nodes[self.current_node_id]
        return None

    def make_choice(self, choice_index: int) -> bool:
        node = self.get_current_node()
        if not node:
            return False

        choices_list = list(node.choices.items())
        if 0 <= choice_index < len(choices_list):
            choice_text, next_node_id = choices_list[choice_index]
            self.current_node_id = next_node_id
            return True
        else:
            print("Invalid choice. Please try again.")
            return False
            
    def play(self):
        """A helper method to run the story loop in the console."""
        while self.current_node_id:
            node = self.get_current_node()
            print("\n" + "="*40)
            print(node.text)
            
            if not node.choices:
                print("\n--- The End ---")
                break
                
            print("\nChoices:")
            choices_list = list(node.choices.keys())
            for i, choice_text in enumerate(choices_list):
                print(f"{i + 1}. {choice_text}")
                
            choice_input = input("\nEnter the number of your choice: ")
            if choice_input.isdigit():
                self.make_choice(int(choice_input) - 1)
            else:
                print("Please enter a valid number.")