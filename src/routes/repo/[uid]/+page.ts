import { error } from '@sveltejs/kit'
import type { PageLoad } from './$types'

export const load: PageLoad = ({ params }) => {
	if (params.uid === 'django') {
		return {
			repoName: 'Django',
			repoDesc: "it's django"
		}
	} else {
		return {
			repoName: params.uid,
			repoDesc: 'idk what it is'
		}
	}

	error(404, 'Not found')
}
