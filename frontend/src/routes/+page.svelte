<script lang="ts">
	import Navigation from "$lib/components/Navigation/Navigation.svelte";

    let data = $props();
</script>

<main>
    <heading>
        <h1>Home</h1>
    </heading>
    <article>
        <section>
            <p>🚧Oops, there's nothing here!🚧</p>
            <a href="/dashboard">Go to dashboard</a>
        </section>
    </article>
</main>

<style lang="scss">

    h1 {
        margin: 0;
        padding: 0;
    }
    main {
        flex: 1;
        width: 100vw;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        gap: 1rem;
    }

    section {
        display: flex;
        flex-direction: column;
        gap: 0.5rem;
    }

    a {
        display: block;
        padding: 1rem;
        border-radius: 10rem;
        color: #000;
        text-decoration: none;
        background: #fff;
        border: 1px solid rgb(45, 45, 45);
    }
</style>