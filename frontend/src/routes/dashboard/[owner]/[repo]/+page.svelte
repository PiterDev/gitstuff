<script lang="ts">
	import TaskList from "$lib/components/TaskList/TaskList.svelte";
	import type { Issue } from "$lib/types/Api.ts";
	import type { Task } from "$lib/types/TaskList.ts";
    let { data } = $props();
    
    let taskArray: Task[] = [];

    let issuesJson = data.issues;
    issuesJson.forEach((issue: Issue) => {
        console.log(issue);
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

</script>

<main>
    <h1>Dashboard</h1>
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
    }
</style>