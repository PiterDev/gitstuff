import { error } from '@sveltejs/kit'
import type { PageLoad } from './$types'

export const load: PageLoad = ({ params }) => {
	if (params.uid === 'django') {
		return {
			name: 'django',
			description: "it's django",
			icon: 'https://avatars.githubusercontent.com/u/27804?v=4',
			issues: 296,
			stars: 123,
			watchers: 123,
			last_commit: new Date('2024-12-20T13:18:10Z'),
			vote_count: 123
		}
	}
	// else {
	// 	return {
	// 		name: params.uid,
	// 		desc: 'idk what it is',
	// 		icon: 'https://static.wikia.nocookie.net/amogus/images/c/cb/Susremaster.png/revision/latest?cb=20210806124552',
	// 		issues: 420,
	// 		last_commit: new Date()
	// 	}
	// }

	error(404, 'Not found')
}
