<script lang="ts">
	import type { PageData } from './$types'
	import RepoCard from '$lib/components/RepoCard/RepoCard.svelte'

	let { data }: { data: PageData } = $props()
</script>

<RepoCard {...data} />
