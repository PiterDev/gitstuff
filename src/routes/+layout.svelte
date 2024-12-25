<script lang="ts">
	import '../global.scss'
</script>

<slot />

<!-- <style lang="scss">
	// CSS Reset
	// "Borrowed" some code from https://www.joshwcomeau.com/css/custom-css-reset/
	:global(*) {
		margin: 0;
	}

	:global(*, *::before, *::after) {
		box-sizing: border-box;
	}

	:global(body) {
		line-height: 1.5;
		-webkit-font-smoothing: antialiased;
		background-color: black;
		color: #fff;

		font-family: 'Inter', serif;
	}
	:global(input, button, textarea, select) {
		font: inherit;
	}
	:global(p, h1, h2, h3, h4, h5, h6) {
		overflow-wrap: break-word;
	}
	:global(p) {
		text-wrap: pretty;
	}
	:global(h1, h2, h3, h4, h5, h6) {
		text-wrap: balance;
	}
</style> -->
