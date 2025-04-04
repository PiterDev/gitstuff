<script lang="ts">
	import type { Task } from "$lib/types/TaskList";

    import HeroiconsOutlineXCircle from '~icons/heroicons-outline/x-circle';
    import HeroiconsOutlineCheckCircle from '~icons/heroicons-outline/check-circle';
    import MdiGithub from '~icons/mdi/github';

    let { name, done }: Task = $props();
</script>

<div class="task">
    <span class="icon">
        {#if done}
            <HeroiconsOutlineCheckCircle />
        {:else}
            <HeroiconsOutlineXCircle />
        {/if}

    </span>
    <p>{name}</p>

    <MdiGithub />
</div>

<style lang="scss">
    .task {
        display: flex;
        justify-content: space-between;
        padding: 0.5rem;
        gap: 1rem;
        cursor: pointer;
        background: #464646;

        .icon {
            display: flex;
            align-items: center;
            justify-content: center;
        }
    }

    .task:nth-of-type(2n+1) {
        background: rgb(80, 80, 80);
    }
    
    .task:hover {
        background: #5d5d5d;
    }
    

</style>