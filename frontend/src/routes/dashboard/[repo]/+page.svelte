<script lang="ts">
	import TaskList from "$lib/components/TaskList/TaskList.svelte";
    let { data } = $props();
    
    let testTasks =  [
        {
            name: "Task 1",
            done: false,
            description: "This is a task description",
        },
        {
            name: "Task 2",
            done: true,
            description: "This is another task description",
        },
        {
            name: "Task 3",
            done: false,
            description: "This is a third task description",
        },
    ];
</script>

<main>
    <pre>
        {JSON.stringify(data, null, 2)}
    </pre>
    <h1>Dashboard</h1>
    <div class="main-box">
        <TaskList tasks={testTasks} />
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