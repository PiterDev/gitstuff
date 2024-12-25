<script lang="ts">
	import type { RepoData } from '$lib/util/repoData'
	import IconTextValue from './IconTextValue.svelte'

	// import svgs but as components
	import Issue from '$lib/assets/IssueIcon.svelte'
	import Star from '$lib/assets/StarIcon.svelte'
	import Eye from '$lib/assets/EyeIcon.svelte'
	import CalendarIcon from '$lib/assets/CalendarIcon.svelte'
	import UpArrow from '$lib/assets/UpArrow.svelte'

	let { name, description, icon, issues, last_commit }: RepoData = $props()
</script>

<div class="size-container">
	<div class="border-container">
		<div class="repo-info">Repo Info</div>

		<div class="main-box">
			<h1>Django</h1>
			<div class="icon-desc-container">
				<img src="https://avatars.githubusercontent.com/u/27804?v=4" alt="Django logo" />
				<p>The Web framework for perfectionists with deadlines.</p>
			</div>
			<div class="hsep"></div>
			<div class="stats-container">
				<h2>Repo Stats</h2>
				<div class="stats-list">
					<IconTextValue ImgComponent={Issue} key="Issues" value="123" />
					<IconTextValue ImgComponent={Star} key="Stars" value="123" />
					<IconTextValue ImgComponent={Eye} key="Watchers" value="123" />
					<IconTextValue ImgComponent={CalendarIcon} key="Last Commit" value="1 January 2023" />
				</div>
			</div>
			<div class="hsep"></div>
			<div class="vote-container">
				<UpArrow height={24} />
				<p>123</p>
			</div>
			<div class="links">
				<a href="">View on Github</a>
				<a>Visit Website</a>
			</div>
		</div>
	</div>
</div>

<style lang="scss">
	.size-container {
		min-width: 100vw;
		min-height: calc(100vh - 4rem);
		display: flex;
		justify-content: center;
		padding: 1rem;
	}

	.border-container {
		min-height: inherit;
		width: min(100%, 25rem);

		border: 2px #1e1e1e solid;
		border-radius: 1rem;
	}

	.repo-info {
		align-self: stretch;
		display: flex;
		justify-content: center;
		border-bottom: 2px #1e1e1e solid;
	}

	.main-box {
		min-height: inherit;
		width: inherit;

		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: space-evenly;

		.hsep {
			width: 30%;
			height: 0.25rem;
			background: #fff;
			border-radius: 1rem;
		}

		.icon-desc-container {
			display: flex;
			align-items: center;
			gap: 1rem;
			padding: 0 1rem;
			img {
				width: 128px;
				height: 128px;
			}
			p {
				font-size: 1rem;
			}
		}
		.stats-container {
			display: flex;
			flex-direction: column;
			align-items: center;
			gap: 1rem;
			h2 {
				font-size: 1.25rem;
				text-align: center;
			}

			.stats-list {
				display: flex;
				flex-direction: column;
				gap: 0.5rem;
			}
		}

		.vote-container {
			display: flex;
			justify-content: center;
			align-items: center;
			gap: 0.5rem;
		}

		.links {
			display: flex;
			flex-direction: column;
			gap: 0.5rem;

			a {
				text-align: center;
			}
		}
	}
</style>
