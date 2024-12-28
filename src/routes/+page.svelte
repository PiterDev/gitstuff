<script lang="ts">
	import { passive } from 'svelte/legacy'

	let authenticated = $state(false)
</script>

<div class="bg-gradient">
	{#if authenticated}
		<p>Authenticated successfully.</p>
		<br />
		<p>Try navigating to /repo/name-of-repo</p>
		<button> Try it out!</button>
	{:else}
		<button>Log in with GitHub</button>
	{/if}
</div>

<style lang="scss">
	.bg-gradient {
		min-height: 100vh;
		min-width: 100vw;

		background: rgb(0, 0, 0);
		background: linear-gradient(135deg, #000 0%, #15171d 70%, #21242b 100%);
		color: $text-darker;
	}

	button {
		outline: none;
		border: none;
		cursor: pointer;
		background-color: white;
		padding: 1rem 2rem;
		border-radius: 2rem;
		color: #000;
		// drop shadow 10% white x 4 y 4 blur 4px
	}
</style>
