<script lang="ts">
	import UpArrow from '$lib/assets/UpArrow.svelte'

	let clicked = $state(false)
</script>

<button type="button" class="vote-button" onclick={() => (clicked = !clicked)}>
	<UpArrow height={24} {clicked} />
</button>

<style lang="scss">
	.vote-button {
		all: unset; /* Resets default styles */
		cursor: pointer; /* Ensures the button is interactive */
		width: fit-content; /* Adapts to the content's size */
		height: fit-content;
		display: inline-flex; /* For centering SVG if needed */
		align-items: center;
		justify-content: center;
	}

	.vote-button:focus {
		border-radius: 1rem;
	}

	.vote-button:active {
		transform: scale(0.9);
		transition: ease-in-out 0.1s;
	}
</style>
