# Release Note Summarization Agent

Release Note Agent uses [Dapr Agents](https://github.com/dapr/dapr-agents) and the remote [Github MCP Server](https://github.com/github/github-mcp-server)
to create a release note summary for a specific Github repository. 
This is often a manual task for [Dapr](https://github.com/dapr) maintainers which spans many repositories and many social media platforms.
This Github Action can apply to any repo, org, release tag and summarize the release information to be distributed to the supported social media platforms.

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

Example outputs:
Using OpenAI:
```bash
== APP == Dapr Summarizer(assistant):
== APP == Release summary: dapr/dapr-agents v0.10.5 (2025-12-16)
== APP == 
== APP == Highlights
== APP == - Features
== APP ==   - Expanded agent metadata: added agent type, registration_at, and component_name when using the Dapr chat client.
== APP ==   - Default agent stores discovery: agents can auto-discover default named stores for registry, memory, workflow state, and pub/sub to reduce required config.
== APP == - Reliability and fixes
== APP ==   - Added gRPC instrumentor to ensure W3C trace propagation to the Dapr sidecar.
== APP ==   - Improved type checking for MCP and toolbox functions.
== APP ==   - Ensured log level is passed to uvicorn; bumped durabletask-dapr dependency.
== APP ==   - Switched CODEOWNERS to team-based entries.
== APP ==   - Addressed high-severity security vulnerabilities in quickstarts.
== APP == - Docs and DevEx
== APP ==   - Added local development docs for Python packages and working with runtime changes.
== APP ==   - Reorganized hello-world quickstarts and related tests/readmes.
== APP ==   - Minor PR template wording cleanup.
== APP == - CI
== APP ==   - Introduced stale bot to clean up stale issues and PRs.
== APP == 
== APP == Merged PRs in this release window
== APP == - #309 Feat/default agent stores
== APP == - #308 sec: fix high security vulnerabilities in quickstarts
== APP == - #307 Fix/specify loglevel
== APP == - #306 fix: improve type checking for the mcp and toolbox functions
== APP == - #305 ci: add stale bot to clean up stale issues and PRs
== APP == - #304 feat: add component_name if using dapr chat client for agent metadata
== APP == - #303 style: update PR template wording
== APP == - #302 fix: add grpc instrumentor for w3c trace propagation to dapr sidecar
== APP == - #301 docs: add local dev docs for py pkgs + runtime changes
== APP == - #296 Refactor quickstarts: reorganized hello-world
== APP == 
== APP == Contributors in this release
== APP == - @CasperGN, @sicoyle, @bibryam
== APP == 
== APP == Full changelog
== APP == - https://github.com/dapr/dapr-agents/compare/v0.10.4...v0.10.5
== APP == 
== APP == What’s next (from Dapr org Project 92)
== APP == - #312 Revamp memory management of agents: separate short-term (workflow) and long-term (summarized) memory and simplify concepts ahead of v1.0.
== APP == - #348 Migrate to streaming pub/sub subscriptions: reduce infra overhead and improve reliability with persistent gRPC streams.
== APP == - #350 Enable Ollama in CI for integration tests: run Conversation Component tests without external providers by default.
```
Using Ollama:
```bash
== APP == Dapr Summarizer(assistant):
== APP == # Release Note Summary: dapr/dapr-agents - v1.5.0
== APP == 
== APP == ## Introduction
== APP == 
== APP == The latest release, v1.5.0, includes a range of improvements and bug fixes. This summary aims to provide an overview of the key features and changes introduced in this release.
== APP == 
== APP == ### Features
== APP == 
== APP == - **Improved Agent Configuration**: Enhanced agent configuration options for better customization and control.
== APP == - **Enhanced Health Checks**: Added more robust health checks to ensure agents are functioning correctly and providing accurate status updates.
== APP == - **New Metrics API**: Introduced a new metrics API for easier data collection and analysis.
== APP == - **Support for Multiple Platforms**: Expanded support for various platforms, including Azure Functions, AWS Lambda, and more.
== APP == 
== APP == ### Bug Fixes
== APP == 
== APP == - **Fixed Agent Crashes**: Resolved issues that caused agents to crash under specific conditions.
== APP == - **Addressed Network Connectivity Issues**: Improved agent behavior when encountering network connectivity problems.
== APP == - **Resolved Docker Build Errors**: Fixed errors that occurred during the build process for Docker images.
== APP == 
== APP == ## Upcoming Work Items (Git Project Board Number 92)
== APP == 
== APP == The following work items are scheduled for the next iteration:
== APP == 
== APP == 1. [URGENT] - Improve agent logging capabilities for better debugging support.
== APP == 2. [PRIORITY MEDIUM] - Enhance support for multi-tenant environments.
== APP == 3. [PRIORITY LOW] - Introduce a feature to monitor and report agent performance metrics.
== APP == 
== APP == ## Welcome New Contributors!
== APP == 
== APP == We would like to extend a warm welcome to our new contributors: @johnDoe, @janeSmith, and @newContributorX. Your contributions will greatly benefit the dapr community, and we are excited to have you on board. Thank you for your hard work and dedication.
== APP == 
== APP == ### Git Commit Messages
== APP == 
== APP == The following commits were made as part of this release:
== APP == 
== APP == - [commitHash] - Improved agent configuration options.
== APP == - [commitHash] - Enhanced health checks for agents.
== APP == - [commitHash] - Introduced new metrics API.
== APP == 
== APP == Note: Please replace the `[commitHash]` placeholders with the actual commit hashes.
```

## Disclaimers

1. You must use a model with tool calling capabilities to utilize the Github MCP Server tools.
2. The quality of the model has direct impact on the quality of the resulting summary.