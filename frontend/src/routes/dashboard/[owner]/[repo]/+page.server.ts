import { BACKEND_API_URL } from '$env/static/private';
import { fetchWithAuth } from '$lib/util/api.js';

export const load = async ({ params, fetch, cookies }) => {
    const token = cookies.get('token');
    const { owner, repo } = params;

    const issues = await fetchWithAuth({
        fetch,
        cookies,
        endpoint: `${BACKEND_API_URL}api/repo_issues?repo_owner=${owner}&repo_name=${repo}&format=json`,
        method: 'GET',
        token,
        body: null
    });

    const repoInfo = await fetchWithAuth({
        fetch,
        cookies,
        endpoint: `${BACKEND_API_URL}api/repo?repo_owner=${owner}&repo_name=${repo}`,
        method: 'GET',
        token,
        body: null
    });

    return {
        issues,
        repo,
        repoInfo
    };
};
