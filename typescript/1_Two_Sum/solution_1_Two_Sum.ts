function twoSum(nums: number[], target: number): number[] {
    const d = new Map()

    for(let i = 0; i < nums.length; i++) {
        const remainder_to_search = target - nums[i]
        if(d.has(remainder_to_search)) {
            return [d.get(remainder_to_search), i]
        }
        d.set(nums[i], i)
    }
};