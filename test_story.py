from src.story import Story_Manager, StoryNode

def main():
    """
    Main function to set up and run the story test.
    """

    # 1. Create a story instance
    my_story = Story_Manager()

    # 2. Create story nodes
    start_node = StoryNode("start", "You wake up in a mysterious forest. Two paths diverge in front of you.", "start_action")
    left_path = StoryNode("left", "You walk down the left path and find a peaceful, small village. You are safe!", "walk")
    right_path = StoryNode("right", "You walk down the right path and encounter a wild beast. It's dangerous!", "walk")

    # 3. Add choices to connect nodes
    start_node.add_choice("Take the left path.", "left")
    start_node.add_choice("Take the right path.", "right")

    # 4. Add nodes to the manager
    my_story.add_node(start_node)
    my_story.add_node(left_path)
    my_story.add_node(right_path)

    # 5. Set the starting node
    my_story.set_start_node("start")

    # 6. Run the story
    print("--- Starting Story Test ---")
    my_story.run()
    print("--- Story Test Finished ---")

if __name__ == "__main__":
    main()
