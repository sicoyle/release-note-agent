# Release Note Summarization Agent

TODO

## Prerequisites

- Python 3.11 (recommended)
- pip package manager
- OpenAI API Key if you want to use OpenAI

## Environment Setup

```bash
# Create a virtual environment
python3.11 -m venv .venv

# Activate the virtual environment 
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Configuration

The quickstart includes an OpenAI component configuration in the `components` directory. You have two options to configure your API key:

### Option 1: Using Environment Variables (Recommended)

1. Create a `.env` file in the project root and add your OpenAI API key:
```env
OPENAI_API_KEY=your_api_key_here
```

You can directly update the `key` in [components/openai.yaml](components/openai.yaml):
```yaml
apiVersion: dapr.io/v1alpha1
kind: Component
metadata:
  name: openai
spec:
  type: conversation.openai
  metadata:
    - name: key
      value: "OPENAI_API_KEY"
```

Replace `OPENAI_API_KEY` with your actual OpenAI API key.

Note: Many LLM providers are compatible with OpenAI's API (DeepSeek, Google AI, etc.) and can be used with this component by configuring the appropriate parameters. Dapr also has [native support](https://docs.dapr.io/reference/components-reference/supported-conversation/) for other providers like Google AI, Anthropic, Mistral, DeepSeek, etc.

2. Run the example with:
```bash
dapr run --app-id summarization_agent --resources-path ./components -- python release_note_agent.py
```

### Additional Components

The quickstart includes other necessary Dapr components in the `components` directory:

- `statestore.yaml`: Agent state configuration
- `workflowstate.yaml`: Workflow state configuration

Make sure Dapr is initialized on your system:

```bash
dapr init
```


## To run locally
You need to set the following env vars (modified appropriately):
- GITHUB_PAT='blah'
- GITHUB_REPOSITORY='dapr/dapr-agents'
- GITHUB_OWNER_TYPE='org'
- GITHUB_PROJECT_NUMBER='92'

Then,
```
cd release_note_agent
dapr run --app-id summarization_agent --resources-path ./components -- python release_note_agent.py
```