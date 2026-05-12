class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[1]-x[0], reverse=True)

        total_energy_consumed_so_far = 0
        min_energy_so_far = 0

        for i in range(len(tasks)):
            actual = tasks[i][0]
            minimum = tasks[i][1]
            buffer = minimum - actual

            total_energy_consumed_so_far += actual
            min_energy_so_far = max(min_energy_so_far, total_energy_consumed_so_far + buffer)

        return min_energy_so_far
