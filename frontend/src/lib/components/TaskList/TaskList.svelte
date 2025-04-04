<script lang="ts">
	import type { TaskListProps } from "../../types/TaskList";
	import Task from "./Task.svelte";

    let { tasks }: TaskListProps = $props();
</script>

{#each tasks as task}
    <Task {...task} />
    <!-- <div class="column">
        <span>{task.done ? "V" : "X"}</span>
        <p>{task.name}</p>
    </div> -->
{/each}

