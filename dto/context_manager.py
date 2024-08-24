class ContextManager:
    def __init__(self):
        # Initialize the context array with some default strings (can be empty)
        self.context = [
            {
                # "filename": "example/vite/src/components/.context",
                # "context": "..",
            }
        ]
        self.inst = [
            {
                # "filename": "example/vite/src/components/ChatArea.tsx.inst",
                # "inst": "..",
            }
        ]

    def add_context(self, new_context):
        """Add a new string to the context array."""
        if isinstance(new_context, str):
            self.context.append(new_context)
        else:
            raise ValueError("Only strings can be added to context")

    def remove_context(self, context_to_remove):
        """Remove a string from the context array."""
        if context_to_remove in self.context:
            self.context.remove(context_to_remove)
        else:
            raise ValueError("The specified context does not exist in the array")

    def get_context(self):
        """Retrieve the current context array."""
        return self.context

    def clear_context(self):
        """Clear all context strings from the array."""
        self.context = []

    def set_inst(self, new_inst):
        """Add a new string to the inst array."""
        if isinstance(new_inst, str):
            self.context.append(new_inst)
        else:
            raise ValueError("Only strings can be added to inst")

    def remove_inst(self, inst_to_remove):
        """Remove a string from the context array."""
        if inst_to_remove in self.context:
            self.context.remove(inst_to_remove)
        else:
            raise ValueError("The specified intst does not exist in the array")

    def get_inst(self):
        """Retrieve the current context array."""
        return self.inst

    def clear_inst(self):
        """Clear all inst strings from the array."""
        self.inst = []
