export type IssueList = {
	issues: Issue[];
};

export type Issue = {
	id: number;
	title: string;
	body: string;
	state: string;
	created_at: string;
	updated_at: string;
};
