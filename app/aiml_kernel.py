
import aiml
import os

class AimlKernel:
    """A wrapper around the standard AIML kernel to manage state."""

    def __init__(self, aiml_path: str):
        """
        Initializes the AIML kernel, loads brain file if it exists,
        otherwise learns the AIML file set.
        """
        self._kernel = aiml.Kernel()
        self._is_brain_loaded = False
        brain_file = os.path.join(aiml_path, 'bot_brain.brn')

        if os.path.exists(brain_file):
            try:
                self._kernel.bootstrap(brainFile=brain_file)
                self._is_brain_loaded = True
                print('Brain loaded successfully.')
            except Exception as e:
                print(f"Error loading brain file: {e}. Learning from scratch.")

        if not self._is_brain_loaded:
            print('No brain found or error loading. Learning AIML files...')
            startup_file = os.path.join(aiml_path, 'startup.xml')
            if os.path.exists(startup_file):
                self._kernel.bootstrap(learnFiles=startup_file, commands="LOAD AIML B")
                self._kernel.saveBrain(brain_file)
                print('Learning complete and brain saved.')
            else:
                raise FileNotFoundError(f"Startup AIML file not found at {startup_file}")

    def get_response(self, user_input: str, session_id: str = 'default') -> str:
        """
        Gets a response from the AIML kernel for the given user input.
        """
        if not user_input:
            return 'Sorry, I did not receive a message.'
            
        # Set a default name if not known
        if not self._kernel.getPredicate('name', session_id):
           self._kernel.setPredicate('name', 'friend', session_id)

        response = self._kernel.respond(user_input, session_id)
        return response or "I'm not sure how to respond to that. Can you ask me something else?"
