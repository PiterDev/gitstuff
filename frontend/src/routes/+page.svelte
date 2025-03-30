<script lang="ts">
    let data = $props();
</script>

<h1>Welcome to SvelteKit + Django</h1>
<pre>
    {JSON.stringify(data, null, 2)}
</pre>

<style>
    h1 {
        font-size: 2.8em;
        text-transform: uppercase;
    }
</style>