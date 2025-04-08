<script lang="ts">
	import type { Task } from "$lib/types/TaskList";

    import HeroiconsOutlineXCircle from '~icons/heroicons-outline/x-circle';
    import HeroiconsOutlineCheckCircle from '~icons/heroicons-outline/check-circle';
    import MdiGithub from '~icons/mdi/github';
	import CompletedCircle from "./CompletedCircle.svelte";

    let { name, done }: Task = $props();
</script>

<div class="task">
    <div class="left">
        <span class="icon">
            <CompletedCircle done={done} />
        </span>
        <p>{name}</p>
    </div>

    <div class="right">
        <MdiGithub />
    </div>
</div>

<style lang="scss">
    .task {
        display: flex;
        justify-content: start;
        align-items: center;
        gap: 1rem;
        // cursor: pointer;
        background: #464646;
        justify-content: space-between;
        padding: 0.5rem 1rem;

        p {
            vertical-align: center;
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
    
    // .task:hover {
    //     background: #5d5d5d;
    // }
    

</style>