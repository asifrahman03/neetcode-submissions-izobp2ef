class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        if (nums == null || nums.length == 0) return new int[0];
        int[] result = new int[nums.length - k + 1];
        Deque<Integer> deque = new ArrayDeque<>();
        int check = 0;
        for (int i = 0; i < nums.length; i++) {
            // Remove elements outside the current window
            if (!deque.isEmpty() && deque.peek() < i - k + 1) {
                deque.poll();
            }

            // Remove elements that are smaller than the current element
            while (!deque.isEmpty() && nums[deque.peekLast()] < nums[i]) {
                deque.pollLast();
            }

            // Add the current element's index to the deque
            deque.offer(i);

            // Store the maximum value for the current window in the result array
            if (i >= k - 1) {
                result[check++] = nums[deque.peek()];
            }
        }
        return result;
    }
}
