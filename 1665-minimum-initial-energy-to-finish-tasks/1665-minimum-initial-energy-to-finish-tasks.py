class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        # tasks.sort(key=lambda x: x[1]-x[0], reverse=True)
        tasks_sortby_buffer = [(-(task[1]-task[0]), task[0], task[1]) for task in tasks]
        heapq.heapify(tasks_sortby_buffer)

        total_energy_consumed_so_far = 0
        min_initial_energy_so_far = 0

        while tasks_sortby_buffer:
            buffer, actual, minimum = heapq.heappop(tasks_sortby_buffer)
            buffer = -buffer
            total_energy_consumed_so_far += actual
            min_initial_energy_so_far = max(
                min_initial_energy_so_far,
                total_energy_consumed_so_far + buffer,
            )

        return min_initial_energy_so_far
