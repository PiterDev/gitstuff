<script lang="ts">
	import type { RepoPickerProps } from '$lib/types/RepoPicker';

	let { repos, onChange }: RepoPickerProps = $props();

	function handleChange(event: Event) {
		const target = event.target as HTMLSelectElement;
		const repo = repos.find((repo) => repo.repoName === target.value);
		if (repo) {
			onChange(repo);
		}
	}
</script>

<div class="repo-picker">
	<select name="repo" id="repo" onchange={handleChange}>
		{#each repos as repo}
			<option value={repo.repoName}>{repo.repoName}</option>
		{/each}
	</select>
</div>

<style lang="scss">
	select {
		padding: 1rem;
		border-radius: 1rem;
		background: #cbcbcb;
	}

	select option {
		padding: 5rem;
		background: gray;
	}
</style>