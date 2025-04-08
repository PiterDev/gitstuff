import type { PageLoad } from './$types';

export const load: PageLoad = async ({ url }) => {
	return {
		sessionExpired: url.searchParams.get('session_expired') === 'true'
	};
};
