import { redirectIfUnauthorized } from '$lib/util/auth.js';

export const load = async ({ parent }) => {
	const { isAuthorized } = await parent();
	redirectIfUnauthorized(isAuthorized);
};
