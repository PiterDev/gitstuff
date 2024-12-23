<script lang="ts">
	let { repoName, repoDesc }: { repoName: string; repoDesc: string } = $props()
</script>

<div class="main-div">Ello {repoName} <br /> {repoDesc}</div>

<style lang="scss">
	.main-div {
		background-color: green;
	}
</style>
