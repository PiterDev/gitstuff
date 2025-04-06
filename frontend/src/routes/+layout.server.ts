export const load = async ({ cookies }) => {
	const isAuthorized = cookies.get('token') !== undefined;
	return {
		isAuthorized: isAuthorized,
		token: cookies.get('token')
	};
};
