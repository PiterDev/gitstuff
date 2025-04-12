import { redirect } from '@sveltejs/kit';

export const redirectIfUnauthorized = (isAuthorized: boolean) => {
	if (!isAuthorized) {
		throw redirect(302, '/auth/github/login');
	}
};
