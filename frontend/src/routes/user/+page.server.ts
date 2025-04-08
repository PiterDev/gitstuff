// +page.server.ts
import { redirect } from '@sveltejs/kit';

export const load = async ({ fetch, cookies }) => {
	const token = cookies.get('token');
	if (!token) {
		throw redirect(302, '/auth/github/login');
	}

	const res = await fetch('http://localhost:8000/api/user?format=json', {
		method: 'GET',
		headers: {
			'Content-Type': 'application/json',
			Authorization: `Token ${token}`
		}
	});

	const data = await res.json();

	if (data.status === '401') {
		// Token expired
		cookies.delete('token', { path: '/' });
		throw redirect(302, '/auth/github/login?session_expired=true');
	}

	return {
		data: data
	};
};
