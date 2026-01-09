import asyncio
import logging
from os import environ
from dapr_agents import DurableAgent
from dapr_agents.workflow.runners import AgentRunner
from dapr_agents.tool.mcp.client import MCPClient
import base64

async def _load_mcp_tools() -> list:
    client = MCPClient()
    pat_token = environ.get('GITHUB_PAT', '')
    await client.connect_streamable_http(
        server_name="github",
        url="https://api.githubcopilot.com/mcp/",
        headers= {
             "Authorization": f"Bearer {pat_token}"
        },
    )
    return client.get_all_tools()


async def main():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    tools = await _load_mcp_tools()

    instructions_prompt = [
        "Respond clearly and concisely to summarize the release notes for the Git tag or branch provided.",
        f"You are running within the context of the Git owner/repository of: {environ.get('GITHUB_REPOSITORY', '')}.",
        "Use tools when appropriate to capture the corresponding commits for the release that needs to be summarized.",
        "If there are new contributors to the project, add a section to provide a welcoming and thankful shoutout for them.",
    ]

    git_owner_type = environ.get('GITHUB_OWNER_TYPE', '')
    git_project_num = environ.get('GITHUB_PROJECT_NUMBER', '')
    if git_owner_type and git_project_num:
        instructions_prompt += f"Utilize the Git Project board number {git_project_num} for Git Owner Type of {git_owner_type} to add 2-3 upcoming work items to the summary.",


    release_note_agent = DurableAgent(
        role="Release Note Summarizer",
        name="Dapr Summarizer",
        goal="Summarize the release notes provided",
        instructions=instructions_prompt,
        tools=tools,
    )

    # Create an AgentRunner to execute the workflow
    runner = AgentRunner()

    try:
        prompt = "Create the release note summary."

        # Run the workflow and wait for completion
        result = await runner.run(
            release_note_agent,
            payload={"task": prompt},
        )

        print(f"\nFinal Result:\n{result}\n", flush=True)

    except Exception as e:
        logger.error(f"Error running workflow: {e}", exc_info=True)
        raise
    finally:
        runner.shutdown(release_note_agent)
        exit(0)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
