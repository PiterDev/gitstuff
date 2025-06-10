<script lang="ts">
    import TaskList from "$lib/components/TaskList/TaskList.svelte";
    import RepoInfo from "$lib/components/RepoInfo/RepoInfo.svelte";
    import AddRepoForm from "$lib/components/AddRepoForm/AddRepoForm.svelte";
    import type { Issue } from "$lib/types/Api.ts";
    import type { Task } from "$lib/types/TaskList.ts";
    let { data } = $props();

    let taskArray: Task[] = [];

    let issuesJson = data.issues;
    issuesJson.forEach((issue: Issue) => {
        taskArray.push({
            name: issue.title,
            done: issue.state === "closed" ? true : false,
            description: issue.body,
            url: issue.html_url,
            owner: issue.user.login,
            repo: data.repo,
            issue_id: issue.number,
            issue_state: issue.state,
        });
    });

    async function handleCreateRepo(event: CustomEvent<{ name: string; description: string }>) {
        const { name, description } = event.detail;
        try {
            const res = await fetch("/api/issue/create", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    owner: data.repoInfo.owner.login,
                    repo: data.repoInfo.name,
                    title: name,
                    body: description
                })
            });
        } catch (e) {
            alert("Failed to create issue.");
        }
    }
</script>

<main>
    <h1>Dashboard</h1>
    <RepoInfo repoInfo={data.repoInfo} />
    <h2 class="tasks-heading">Tasks</h2>
    <AddRepoForm on:create={handleCreateRepo} />
    <div class="main-box">
        <TaskList tasks={taskArray} />
    </div>
</main>

<style lang="scss">
    main {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .main-box {
        border-radius: 6px;
        border: 1px solid gray;
        max-width: 75rem;
        width: 100%;
        margin-top: 1.2rem;
        background: #232323;
    }
    .tasks-heading {
        margin: 1.5rem 0 0.5rem 0;
        font-size: 1.3rem;
        color: #fff;
        font-weight: 600;
        align-self: flex-start;
        max-width: 75rem;
        width: 100%;
        box-sizing: border-box;
    }
    :global(.add-repo-form) {
        max-width: 75rem;
        width: 100%;
        box-sizing: border-box;
    }
</style>