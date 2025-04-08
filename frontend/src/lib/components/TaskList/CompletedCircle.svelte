<script lang="ts">
    import HeroiconsOutlineXCircle from '~icons/heroicons-outline/x-circle';
    import HeroiconsOutlineCheckCircle from '~icons/heroicons-outline/check-circle';

    let { done }: { done: boolean } = $props();

    function toggle() {
        done = !done;
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

        :global(.checked) {
            color: green;
        }
    }


    button:active {
        transform: scale(0.9);
    }

</style>