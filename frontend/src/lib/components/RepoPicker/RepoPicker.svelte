<script lang="ts">
	import type { RepoPickerProps } from '$lib/types/RepoPicker';

	let { repos }: RepoPickerProps = $props();
</script>

<div class="repo-picker">
	<select name="repo" id="repo">
		{#each repos as repo}
			<option value={repo.repoName}>{repo.repoName}</option>
		{/each}
	</select>
</div>

