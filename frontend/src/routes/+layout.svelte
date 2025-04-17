<script lang="ts">
	import Navigation from "$lib/components/Navigation/Navigation.svelte";
    import "$lib/styles/global.scss";
    let { children } = $props();
</script>

<div class="page">
    <Navigation />
    <div class="children">{@render children()}</div>
</div>

<style lang="scss">
    .page {
        display: flex;
        flex-direction: column;
        min-height: 100vh;
    }
    .children {
        flex: 1;
        display: flex;
        flex-direction: column;
    }
</style>