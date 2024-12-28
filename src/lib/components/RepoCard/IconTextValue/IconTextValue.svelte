<script lang="ts">
	import type { Component } from 'svelte'
	type ImgComponentProps = {
		height: number
		[key: string]: any
	}

	let {
		ImgComponent,
		key,
		value
	}: { ImgComponent: Component<ImgComponentProps>; key: string; value: string } = $props()
</script>

<div class="icon-text-value">
	<ImgComponent height={24} />
	<p class="key">{key}:</p>
	<p class="value">{value}</p>
</div>

<style lang="scss">
	.icon-text-value {
		display: flex;
		justify-content: center;
		align-items: center;
		gap: 0.5rem;
		font-size: 1rem;
	}

	.value {
		color: $text-light;
	}

	.key {
		color: $text-dark;
	}
</style>
