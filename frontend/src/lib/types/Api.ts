export type IssueList = {
	issues: Issue[];
};

export type Issue = {
	number: number;
	title: string;
	body: string;
	state: string;
	created_at: string;
	updated_at: string;
	html_url: string;
	user: {
		login: string;
	};
};
