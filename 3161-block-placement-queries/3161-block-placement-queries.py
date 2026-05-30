class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        coords = set([0])
        for q in queries:
            coords.add(q[1])
        coords = sorted(coords)
        compress = {v: i for i, v in enumerate(coords)}
        N = len(coords)

        tree = [0] * (4 * N)

        def update(node, start, end, idx, val):
            if start == end:
                tree[node] = val
                return
            mid = (start + end) // 2
            if idx <= mid:
                update(2*node, start, mid, idx, val)
            else:
                update(2*node+1, mid+1, end, idx, val)
            tree[node] = max(tree[2*node], tree[2*node+1])

        def query(node, start, end, l, r):
            if r < start or end < l:
                return 0
            if l <= start and end <= r:
                return tree[node]
            mid = (start + end) // 2
            return max(query(2*node, start, mid, l, r), query(2*node+1, mid+1, end, l, r))

        obstacle_seq = [0]

        def bs(k):
            lo, hi = 0, len(obstacle_seq) - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if obstacle_seq[mid] < k:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return hi, lo

        results = []
        for q in queries:
            if q[0] == 1:
                x = q[1]
                left, right = bs(x)
                left_obstacle = obstacle_seq[left]
                update(1, 0, N-1, compress[x], x - left_obstacle)

                if right < len(obstacle_seq):
                    right_obstacle = obstacle_seq[right]
                    update(1, 0, N-1, compress[right_obstacle], right_obstacle - x)

                obstacle_seq.insert(right, x)

            else:
                x, sz = q[1], q[2]
                left, _ = bs(x + 1)
                nearest_left = obstacle_seq[left]
                max_gap = max(query(1, 0, N-1, 0, compress[nearest_left]), x - nearest_left)
                results.append(max_gap >= sz)

        return results