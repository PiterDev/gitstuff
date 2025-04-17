<script lang="ts">
	import { goto } from "$app/navigation";
	import RepoPicker from "$lib/components/RepoPicker/RepoPicker.svelte";
	import type { JsonRepo, Repo } from "$lib/types/RepoPicker.js";

	let { data } = $props();
	let repos = data.reposJson.map((repo: JsonRepo) => {
		return {
			repoName: repo.full_name
		};
	});

	function handleChange(repo: Repo) {
		goto(`/dashboard/${repo.repoName}`);
	}
</script>
<main>
	<header>
		<h1>Repositories</h1>
	</header>
	<form>
		<RepoPicker repos={repos} onChange={handleChange} />
	</form>
</main>

<style lang="scss">
	main {
		flex: 1;
		width: 100vw;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		gap: 1rem;
	}
</style>