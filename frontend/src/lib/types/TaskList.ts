import type { HTMLAttributes } from 'svelte/elements';

export type Task = {
	name: string;
	description: string;
	done: boolean;
	url: string;
	owner: string;
	repo: string;
	issue_id: number;
	issue_state: string;
};

export type TaskListProps = {
	tasks: Task[];
};

export type CompletedCircleProps = {
	done: boolean;
	onCheck: () => void;
	onUncheck: () => void;
	// rest: HTMLAttributes<HTMLButtonElement> | undefined;
};
