import { redirect } from '@sveltejs/kit';

export const redirectIfUnauthorized = async (isAuthorized: boolean) => {
	if (!isAuthorized) {
		throw redirect(302, '/auth/github/login');
	}
};
