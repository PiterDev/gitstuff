<script lang="ts">
	import type { RepoData } from '$lib/util/repoData'
	import IconTextValue from './IconTextValue/IconTextValue.svelte'

	// import svgs but as components
	import Issue from '$lib/assets/IssueIcon.svelte'
	import Star from '$lib/assets/StarIcon.svelte'
	import Eye from '$lib/assets/EyeIcon.svelte'
	import CalendarIcon from '$lib/assets/CalendarIcon.svelte'
	import VoteButton from './VoteButton/VoteButton.svelte'

	let { name, description, icon, issues, stars, watchers, last_commit, vote_count }: RepoData =
		$props()
</script>

<div class="size-container">
	<div class="border-container">
		<div class="repo-info gray-gradient">Repo Info</div>

		<div class="main-box">
			<h1>{name}</h1>
			<div class="icon-desc-container">
				<img src={icon} alt="Django logo" />
				<p>
					{description}
				</p>
			</div>
			<div class="hsep"></div>
			<div class="stats-container">
				<h2>Repo Stats</h2>
				<div class="stats-list">
					<IconTextValue ImgComponent={Issue} key="Issues" value={issues.toString()} />
					<IconTextValue ImgComponent={Star} key="Stars" value={stars.toString()} />
					<IconTextValue ImgComponent={Eye} key="Watchers" value={watchers.toString()} />
					<IconTextValue
						ImgComponent={CalendarIcon}
						key="Last Commit"
						value={last_commit.toLocaleDateString('en-US', {
							month: 'long',
							day: 'numeric',
							year: 'numeric'
						})}
					/>
				</div>
			</div>
			<div class="hsep"></div>
			<div class="vote-container">
				<h2>Repo Votes</h2>
				<div class="vote-counter">
					<VoteButton />
					<p>{vote_count}</p>
				</div>
			</div>
			<div class="links">
				<a href="google.com">View on Github</a>
				<a href="google.com">Visit Website</a>
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
		// background: $test-var;
	}

	.border-container {
		margin: 0.1rem 0;

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
		padding: 0.5rem;
		border-radius: 1rem 1rem 0 0;

		background: rgb(0, 0, 0);
		background: linear-gradient(180deg, rgba(0, 0, 0, 1) 0%, rgb(8, 8, 8) 100%);
		color: $text-darker;
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
			flex-direction: column;
			gap: 1rem;
			padding: 0 1rem;
			text-align: center;
			img {
				width: 128px;
				height: 128px;
			}
			p {
				font-size: 1rem;
				color: $text-dark;
			}
		}
		.stats-container {
			display: flex;
			flex-direction: column;
			align-items: center;
			gap: 1rem;

			color: $text-dark;

			.stats-list {
				display: flex;
				flex-direction: column;
				gap: 0.5rem;
			}
		}

		.vote-container {
			display: flex;
			flex-direction: column;
			gap: 1rem;
			.vote-counter {
				display: flex;
				justify-content: center;
				align-items: center;
				gap: 0.5rem;
			}
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

	@media (min-width: 831px) {
		.size-container {
			min-height: auto;
			min-width: auto;
			padding: 0;
		}

		h1 {
			padding-top: 4rem;
		}

		.border-container {
			width: min(100%, 50rem);
			margin: 2rem 0;

			.main-box {
				min-height: auto;
				justify-content: start;

				gap: 4rem;

				.icon-desc-container {
					flex-direction: row;
					p {
						max-width: 50ch;
						text-align: start;
					}
					// max-width: 25rem;
				}

				.links {
					padding-bottom: 2rem;
				}
			}
		}
	}

	@media (max-height: 900px), (max-width: 300px) {
		.border-container {
			margin: 2rem 0;
		}
		.main-box {
			justify-content: start;
			gap: 4rem;
		}

		.links {
			padding-bottom: 2rem;
		}
	}
</style>
