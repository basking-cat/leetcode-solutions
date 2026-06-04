# Memo

- left/right side variant: move forward only one of left or right, "while left < right"
  - must check nums[left] == target (or nums[right] for right variant)
    after the loop, since one candidate remains unchecked
- both sides variant: move forward both, "while left <= right"
  - all candidates are checked inside the loop, no need to check after
