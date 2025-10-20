# First_Chat_Bot
* Creating my first simple chat bot using very minimal code

## Block Diagram:

Input from PDF document -->
Data is being divided into Chunks -->
Open AI extension to convert that Chunks to Embeddings -->
Embeddings are stored in the Vector Store

-----------------------------------------------------------

From UI when a user searches any question, It will create that _query into *chunks* and *compare* that in the *vector store* and results are populated in the UI.

### Starting the Application:
As I am running the code from Github Codespace the command to run the `Streamlit` Application is: `streamlit run /workspaces/First_Chat_Bot/chatbot.py`

For running the `Streamlit` Application in localhost: `streamlit run <location_of_file_in_system>`
