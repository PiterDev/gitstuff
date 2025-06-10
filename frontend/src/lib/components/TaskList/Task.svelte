<script lang="ts">
	import type { Task } from "$lib/types/TaskList";

    import HeroiconsOutlineXCircle from '~icons/heroicons-outline/x-circle';
    import HeroiconsOutlineCheckCircle from '~icons/heroicons-outline/check-circle';
    import MdiGithub from '~icons/mdi/github';
	import CompletedCircle from "./CompletedCircle.svelte";

    let { name, done, url, owner, repo, issue_id, issue_state }: Task = $props();
    console.log(done);
    let doneState = $state(done);
    let onTimeout = false;

    async function onCheck() {
        if (onTimeout) return;

        doneState = true;
        // Wait for server to update
        const response = await fetch(`/api/issue/update`, {
            method: 'POST',
            body: JSON.stringify({
                owner,
                repo,
                id: issue_id,
                state: doneState ? 'closed' : 'open'
            })
        });

        onTimeout = true;
        setTimeout(() => {onTimeout = false}, 5000)

    }

    async function onUncheck() {
        if (onTimeout) return;

        doneState = false;
        // Wait for server to update
        const response = await fetch(`/api/issue/update`, {
            method: 'POST',
            body: JSON.stringify({
                owner,
                repo,
                id: issue_id,
                state: doneState ? 'closed' : 'open'
            })
        });

        onTimeout = true;
        setTimeout(() => {onTimeout = false}, 5000)
    }

</script>

<div class="task">
    <div class="left">
        <span class="icon">
            <!-- This warning can be ignored, typescript can't tell these are spread props -->
            <form>
                <CompletedCircle done={doneState} onCheck={onCheck} onUncheck={onUncheck} />
            </form>
        </span>
        <p class={doneState ? "done" : ""}>{name}</p>
    </div>

    <div class="right">
        <a href={url} target="_blank" rel="noopener noreferrer">
            <MdiGithub />
        </a>
    </div>
</div>

<style lang="scss">
    .task {
        display: flex;
        justify-content: start;
        align-items: center;
        gap: 1rem;
        background: #464646;
        justify-content: space-between;
        padding: 0.5rem 1rem;

        p {
            vertical-align: center;
        }

        p.done {
            text-decoration: line-through;
        }

        .left, .right {
            display: flex;
            align-items: center;
        }

        .left {
            gap: 1rem;
        }
        .icon {
            display: flex;
            align-items: center;
            justify-content: center;
        }
    }

    .task:nth-of-type(2n+1) {
        background: rgb(80, 80, 80);
    }  
</style>