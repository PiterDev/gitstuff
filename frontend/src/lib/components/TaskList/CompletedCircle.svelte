<script lang="ts">
    import HeroiconsOutlineXCircle from '~icons/heroicons-outline/x-circle';
    import HeroiconsOutlineCheckCircle from '~icons/heroicons-outline/check-circle';
	import type { HTMLAttributes } from 'svelte/elements';
	import type { CompletedCircleProps } from '$lib/types/TaskList';
    


    let { done, onCheck, onUncheck}: CompletedCircleProps = $props();

    function toggle() {
        done = !done;
        if (done) onCheck();
        else onUncheck();
    }
</script>

{#if done}
    <button class="circle checked">
        <HeroiconsOutlineCheckCircle onclick={toggle} />
    </button>
{:else}
    <button class="circle">
        <HeroiconsOutlineXCircle onclick={toggle} color="green" />
    </button>
{/if}

<style lang="scss">
    :global(svg) {
        color: #fff;
        width: 1.5rem;
        height: 1.5rem;
    }

    :global(svg):hover {
        color: #989898;
    };

    button {
        outline: none;
        border: none;
        background: none;
        margin: 0;
        padding: 0;
        width: 2rem;
        height: 2rem;


        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
    }


    button:active {
        transform: scale(0.9);
    }

</style>